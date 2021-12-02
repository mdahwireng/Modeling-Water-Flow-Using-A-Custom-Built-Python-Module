import pandas as pd
import geopandas as gpd
import pickle
from shapely.geometry import Polygon

from modules.utilities import create_grid

class RetrieveRegion():
    '''This class takes bounds and crs from users and returns a region the bounds given by user falls in'''
    def __init__(self, bnds, crs) -> None:
        '''This takes a list containing a list of bounds [minx, miny, maxx, maxy] and a string for the crs ESGP:xxxxxx'''
        print('RetrieveRegion initialized...')
        
        self.crs = crs
        self.ref_gdf = pickle.load( open( "data/geo_data.pkl", "rb" ))
        self.bnds, self.espg_val, self.input_gdf = create_grid(bnds=bnds, crs=crs)



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