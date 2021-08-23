from get_region import RetrieveRegion
from pipeline import get_raster_terrain
from visualize import plot_raster_, viz_contour, viz_3d


class ProcessToViz():
    '''This class encapsulate all the process from retrieval of data to visualization'''
    def __init__(self, bnds, crs, csv_save_path, tiff_save_path, pipeline_path) -> None:
        self.bnds = bnds
        self.crs = crs
        self.csv_save_path = csv_save_path
        self.tiff_save_path = tiff_save_path
        self.pipeline_path = pipeline_path


    def ret_reg(self):
        '''Retrieves Region information from reference data'''
        ret = RetrieveRegion(bnds=self.bnds, crs=self.crs)
        ret_dict = ret.get_region()
        f_p = ret_dict['path']
        bds = '(' + str(ret_dict['bounds'][0]) + ',' + str(ret_dict['bounds'][1]) + ')'

        self.f_p = f_p
        self.bds = bds

    def ret_data(self):
        '''Retrieves and preprocess data'''
        get_raster_terrain(file_path=self.f_p ,bounds=self.bds , csv_path=self.csv_save_path , tiff_path=self.tiff_save_path, pipeline_path=self.pipeline_path)

    def viz(self, contour_save_path, viz_3d_save_path, raster_save_path):
        '''This visualizes the produced'''
        viz_contour(tif_path=self.tiff_save_path, img_path=contour_save_path, title='DEM', notebook=True)
       
        viz_3d(csv_path=self.csv_save_path, title='DEM', img_save_path=viz_3d_save_path)
        
        plot_raster_(tifile=self.tiff_save_path, title='DEM', img_save_path=raster_save_path, notebook=True)

    def run_to_viz(self, contour_save_path, viz_3d_save_path, raster_save_path):
        '''This runs all processes including visualization'''
        self.ret_reg()
        self.ret_data()
        self.viz(contour_save_path=contour_save_path, viz_3d_save_path=viz_3d_save_path, raster_save_path=raster_save_path)