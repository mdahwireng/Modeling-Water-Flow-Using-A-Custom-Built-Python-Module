
import geopandas as gpd
from shapely.geometry import Polygon

def create_grid(bnds, crs):
    espg_val = int(crs.split(':')[-1])
        
    MINX, MINY, MAXX, MAXY = bnds
    poly = Polygon(((MINX, MINY), (MINX, MAXY), (MAXX, MAXY), (MAXX, MINY), (MINX, MINY)))
    grid = gpd.GeoDataFrame([poly], columns=["geometry"])
    grid.set_crs(epsg=espg_val, inplace=True)
    
    if espg_val != 3857:
        grid.to_crs(epsg=3857, inplace=True)
    
    bnds_ = grid.bounds.loc[0]
    bnds_lst = [[bnds_['minx'], bnds_['maxx']], [bnds_['miny'], bnds_['maxy']]]

    return espg_val, grid, bnds_lst