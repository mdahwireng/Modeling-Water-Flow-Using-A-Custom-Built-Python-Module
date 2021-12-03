import pickle

from modules.utilities import create_grid, find_region

class RetrieveRegion():
    '''This class takes bounds and crs from users and returns a region the bounds given by user falls in'''
    def __init__(self, bnds=None, crs=None, address=None) -> None:
        '''This takes a list containing a list of bounds [minx, miny, maxx, maxy] and a string for the crs ESGP:xxxxxx'''

        self.crs = crs

        with open( "data/geo_data.pkl", "rb" ) as file:
            self.ref_gdf = pickle.load(file)
        
        self.espg_val, self.input_gdf, self.bnds = create_grid(bnds=bnds, crs=crs, address=address)


    def get_region(self):
        '''This method checks for regions in which the bounds fall in '''

        out_dict = find_region(ref_gdf=self.ref_gdf, input_gdf=self.input_gdf)
        
        if out_dict:
            out_dict['bounds'] = self.bnds

            return out_dict