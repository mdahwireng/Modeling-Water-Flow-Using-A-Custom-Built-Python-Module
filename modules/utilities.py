
import geopandas as gpd
from shapely.geometry import Polygon

def create_grid(bnds=None, crs=None, address=None):
    '''This takes a list containing a list of bounds [minx, miny, maxx, maxy] and a string for the crs ESGP:xxxxxx or only an address'''
    print('RetrieveRegion initialized...')
    
    try:
        if address:
            print('Address parsed. Geocoding initialized...')
            try:
                espg_val = 3857
                grid = gpd.tools.geocode(address, provider='nominatim', user_agent="flow_modeling_app")
                grid.to_crs(epsg=espg_val, inplace=True)
                grid['geometry']=grid['geometry'].buffer(200).envelope
            
            except Exception as e:
                print('Error: {}'.format(e))
        
        else:
            try:
                espg_val = int(crs.split(':')[-1])
                    
                MINX, MINY, MAXX, MAXY = bnds
                poly = Polygon(((MINX, MINY), (MINX, MAXY), (MAXX, MAXY), (MAXX, MINY), (MINX, MINY)))
                grid = gpd.GeoDataFrame([poly], columns=["geometry"])
                grid.set_crs(epsg=espg_val, inplace=True)
                
                if espg_val != 3857:
                    grid.to_crs(epsg=3857, inplace=True)

            except Exception as e:
                print('Error: {}'.format(e))
        
        bnds_ = grid.bounds.loc[0]
        bnds_lst = [[bnds_['minx'], bnds_['maxx']], [bnds_['miny'], bnds_['maxy']]]

        return espg_val, grid, bnds_lst

    except Exception as e:
        print('Error: {}'.format(e))


def find_region(ref_gdf, input_gdf):
    '''This method checks for regions in which the bounds fall in '''
    filter = ref_gdf['geometry'].contains(input_gdf['geometry'][0])
    if filter.sum() > 1:
        print('Match acquired!')
        match_idx = list(ref_gdf[filter].index)
        match_row = ref_gdf.loc[match_idx[0]]
        out_dict={'region':match_row['name'], 'path':match_row['path']}
        return out_dict

    else:
        print('Entered bounds did not fall in any of the regions')