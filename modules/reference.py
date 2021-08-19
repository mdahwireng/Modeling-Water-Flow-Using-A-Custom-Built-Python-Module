import json
import urllib.request as urllib
import pickle
import geopandas as gpd
import pandas as pd
from shapely.geometry import Polygon


class CreateReference():
    '''This class creates and pickle save a geodataframe for the comparison of boundaries to check which region the boundary passed falls in'''

    def __init__(self, regfile_path, prefix='https://s3-us-west-2.amazonaws.com/usgs-lidar-public/', tail='/ept.json') -> None:
        if type(regfile_path) not in [str]:
            raise TypeError("regfile_path is not in the required format. Must be a string")

        if type(prefix) not in [str]:
            raise TypeError("prefix is not in the required format. Must be a string")

        if type(tail) not in [str]:
            raise TypeError("tail is not in the required format. Must be a string")

        self.pre = prefix
        self.tail = tail
        self.regfile = regfile_path


    def get_df_dict(self, save_path=None, save=True) -> None:
        '''This method creates and saves (if save=True) dictionary of region names, year, path, and bounds {'name':[], 'year':[], 'path':[], 'bounds':[]}'''
        if save:
            if save_path == None:
                raise ValueError('save_path should be entered when save is set to True')
            if type(save_path) not in [str]:
                raise TypeError("save_path is not in the required format. Must be a string")
        
        pre = self.pre
        tail = self.tail
        
        counter = 0

        gdf_dict ={'name':[], 'year':[], 'path':[], 'bounds':[]}
        counter = 0
        with open('filename.txt') as f:
            for line in f:
                line_ = line.strip('/\n')
                gdf_dict['name'].append(line_)
                year = line_.split('_')[-1]
                gdf_dict['year'].append(year)
                path = pre + line_ + tail
                gdf_dict['path'].append(path)
                try:
                    j_res = json.load(urllib.urlopen(path))
                    bounds = j_res['bounds']
                except:
                    bounds = None
                gdf_dict['bounds'].append(bounds)
                counter += 1
                if counter%100 == 0:
                    print('\nCounter: {}'.format(counter))
        if save:
            file_name = 'gdf_dict.pkl'
            full = save_path+'/'+file_name
            out = open(full,'wb')
            pickle.dump(gdf_dict, out)
            out.close()
            print('Dictionary saved as {} to {}'.format(file_name, save_path))
        self.gdf_dict = gdf_dict

        def get_gdf(self, path_to_save):
            '''This method creates and saves a geodataframe of all regions and their boundaries'''
            if type(path_to_save) not in [str]:
                raise TypeError("path_to_save is not in the required format. Must be a string")
            
            gdf_dict = self.gdf_dict

            df = pd.DataFrame(gdf_dict)

            df.dropna(axis=0, inplace=True)
            df.reset_index(drop=True, inplace=True)

            polygons =[]
            for bound in df['bounds']:
                MINX, MINY, MAXX, MAXY = [bound[0],bound[1], bound[3],bound[4]] 
                polygon = Polygon(((MINX, MINY), (MINX, MAXY), (MAXX, MAXY), (MAXX, MINY)))
                polygons.append(polygon)

            df['geometry'] = polygons
            gdf = gpd.GeoDataFrame(df, geometry='geometry', crs="EPSG:3857")
            gdf.to_crs(epsg=4326, inplace=True)
            f_name = 'geo_data.pkl'
            f_full = path_to_save+'/'+f_name
            geo_data = open(f_full,'wb')
            pickle.dump(gdf, geo_data)
            geo_data.close()