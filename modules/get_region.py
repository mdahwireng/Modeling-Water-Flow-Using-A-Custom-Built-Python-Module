import pandas as pd
import geopandas as gpd
import pickle
from shapely.geometry import Polygon



class RetrieveRegion():
    '''This class takes bounds and crs from users and returns a region the bounds given by user falls in'''
    def __init__(self, bnds, crs) -> None:
        '''This takes a list containing a list of bounds [minx, miny, maxx, maxy] and a string for the crs ESGP:xxxxxx'''
        print('RetrieveRegion initialized...')

        espg_val = int(crs.split(':')[-1])
        
        MINX, MINY, MAXX, MAXY = bnds
        poly = Polygon(((MINX, MINY), (MINX, MAXY), (MAXX, MAXY), (MAXX, MINY), (MINX, MINY)))
        grid = gpd.GeoDataFrame([poly], columns=["geometry"])
        grid.set_crs(epsg=espg_val, inplace=True)
        
        if espg_val != 3857:
            grid.to_crs(epsg=3857, inplace=True)
        
        bnds_ = grid.bounds.loc[0]
        bnds_lst = [[bnds_['minx'], bnds_['miny']], [bnds_['maxx'], bnds_['maxy']]]
        
        self.bnds = bnds_lst
        self.crs = crs
        self.espg_val=espg_val
        self.input_gdf = grid
        self.ref_gdf = pickle.load( open( "data/geo_data.pkl", "rb" ))



    def get_region(self):
        '''This method checks for regions in which the bounds fall in '''
        filter = self.ref_gdf['geometry'].contains(self.input_gdf['geometry'][0])
        if filter.sum() > 1:
            print('Match acquired!')
            match_idx = list(self.ref_gdf[filter].index)
            match_row = self.ref_gdf.loc[match_idx[0]]
            out_dict={'region':match_row['name'], 'path':match_row['path'], 'bounds':self.bnds}
            return out_dict

        else:
            print('Entered bounds did not fall in any of the regions')