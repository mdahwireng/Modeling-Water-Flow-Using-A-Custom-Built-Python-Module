import pandas as pd
import geopandas as gpd
import pickle
from shapely.geometry import Polygon

from modules.utilities import create_grid, find_region

class RetrieveRegion():
    '''This class takes bounds and crs from users and returns a region the bounds given by user falls in'''
    def __init__(self, bnds, crs) -> None:
        '''This takes a list containing a list of bounds [minx, miny, maxx, maxy] and a string for the crs ESGP:xxxxxx'''

        self.crs = crs
        self.ref_gdf = pickle.load( open( "data/geo_data.pkl", "rb" ))
        self.bnds, self.espg_val, self.input_gdf = create_grid(bnds=bnds, crs=crs)


    def get_region(self):
        '''This method checks for regions in which the bounds fall in '''

        out_dict = find_region(ref_gdf=self.ref_gdf, input_gdf=self.input_gdf)
        
        if out_dict:
            out_dict['bounds'] = self.bnds

            return out_dict