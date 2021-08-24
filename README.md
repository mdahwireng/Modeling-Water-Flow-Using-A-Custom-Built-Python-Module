# Modeling Water Flow Using Lidar Data And A Custom Built Python Module
## Introduction
This project seeks to model the relief of a farm owned by AgriTech in Iowa, USA, using publicly available data from USGS 3DEP project. This project is also a case study which leads to the creation of a python package which fetch, transform and visualize publicly available satellite and Lidar data by interacting with public APIs.

This package abstracts process from the querying, retrieval, conversion of coordinate systems, creating Digital Elevation Models to the visualization of produced images in both 2d and 3d.
## Modules
There are 5 modules in all. They are <b>reference</b>, <b>get_region module</b>, <b>pipeline</b>, <b>visualize</b> and <b>process_to_viz</b> modules. This package is built on pdal, geopandas, pandas, numpy, rasterio, matplotliband shapely

### reference module
This module contains a class called CreateReference. This class creates and pickle-save a geodataframe for the comparison of boundaries to check which region the boundary passed falls in.


| methods     | Mthd desc                                                                                                                                      | arguments      | Arg type | Description                                                                              |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------|----------------|----------|------------------------------------------------------------------------------------------|
| __init__    | Initiatilzes class                                                                                                                             | regfile_path   | string   | Path to a text file with the names of all regions with data on AWS cloud                 |
|             |                                                                                                                                                | prefix         | string   | The leading common string to all the paths leading to names of hosted data on AWS cloud  |
|             |                                                                                                                                                | tail           | string   | The trailing common string to all the paths leading to names of hosted data on AWS cloud |
| get_df_dict | This method creates and saves (if save=True) dictionary of region names, year, path, and bounds {'name':[], 'year':[], 'path':[], 'bounds':[]} | save_path      | string   | path to save genrated dictionary                                                         |
|             |                                                                                                                                                | save           | bolean   | true to save the dictionary false, not to.                                               |
| get_gdf     | This method creates and saves a geodataframe of all regions and their boundaries                                                               | path_to_save   | string   | path to save generated geodataframe                                                      |
| run_all     | This method runs all the methods in this class and saves the geodataframe and reference dictionary                                             | dict_save_path | string   | path to save generated dataframe                                                         |


### get_region module
This module contains a class called class RetrieveRegion. This class takes bounds and crs from users and returns a region the bounds given by user falls in.

| methods    | Mthd desc                                                                                                      | arguments    | Arg type | Description                                       |
|------------|----------------------------------------------------------------------------------------------------------------|--------------|----------|---------------------------------------------------|
| __init__   | This takes a list containing a list of bounds [minx, miny, maxx, maxy] and a string for the crs ESGP:xxxxxx''' | bnds         | list     | Boundaries for region of interest                 |
|            |                                                                                                                | crs          | string   | EPSG code for coordinate reference system of bnds |
| get_region | This method checks for regions in which the bounds fall in                                                     | No arguments | -        | -                                                 |

### pipeline module
This module contains a function called get_raster_terrain.  This function queries, retrieve and pre-process point cloud data using a pipeline parsed to it

| function           | func desc                                                                                      | arguments     | Arg type | Description                                                      |
|--------------------|------------------------------------------------------------------------------------------------|---------------|----------|------------------------------------------------------------------|
| get_raster_terrain | This function queries, retrieve and pre-process point cloud data using a pipeline parsed to it | file_path     | string   | Path to use to access file with data on cloud                    |
|                    |                                                                                                | bounds        | string   | Sting of boundaries in the format ‘([minx, maxx],[miny,maxy]]}’  |
|                    |                                                                                                | csv_path      | string   | Path to save the output of the pre-processing in a csv file      |
|                    |                                                                                                | tiff_path     | string   | Path to save the output of the generated DEM from pre-processing |
|                    |                                                                                                | pipeline_path | string   | Path to structured pdal pipe line in json format                 |

### visualize module
This module contains plot_raster_, viz_contour and viz_3d functions

|function|func desc|arguments|Arg type|Description|
|:---:|:---:|:---:|:---:|:---:|
|viz_contour|This function plots a contour of DEM|tif_path|string|Path to image to be visualised|
| | |img_path|string|Path to save generated image|
| | |title|string|Title to be displayed on plot|
| | |notebook|Boolean|True to indicate the function is being run in a notebook, false for otherwise|
|viz_3d|This fuction plots a 3d plots from x,y and z values from a parsed csv file|csv_path|sring|Path to csv file with data from preprocessing|
| | |title|string|Title to be displayed on plot|
| | |img_save_path|string|Path to save generated image|
| | |skip_val|int|Factor to reduce the number of samples to be plotted|
| | |notebook|Boolean|True to indicate the function is being run in a notebook, false for otherwise|
|plot_raster_|
| |Plots raster tif image both in log scale(+1) and original verion|tifile|string|Path to image to be visualised|
| | |img_save_path|string|Path to save generated image|
| | |title|string|Title to be displayed on plot|
| | |notebook|Boolean|True to indicate the function is being run in a notebook, false for otherwise|

### Process_to_viz module
This module contains a class called class ProcessToViz. This class This class encapsulate all the process from retrieval of data to visualization

| methods    | Mthd desc                                        | arguments         | Arg type | Description                                                      |
|------------|--------------------------------------------------|-------------------|----------|------------------------------------------------------------------|
| __init__   | Initiatilzes class                               | bnds              | list     | Boundaries for region of interest                                |
|            |                                                  | crs               | string   | EPSG code for coordinate reference system of bnds                |
|            |                                                  | csv_path          | string   | Path to save the output of the pre-processing in a csv file      |
|            |                                                  | tiff_path         | string   | Path to save the output of the generated DEM from pre-processing |
|            |                                                  | pipeline_path     | string   | Path to structured pdal pipeline in json format                  |
| ret_reg    | Retrieves Region information from reference data | No arguments      | -        | -                                                                |
| ret_data   | Retrieves and pre-process cloud data             | No arguments      | -        | -                                                                |
| viz        | This visualizes the produced tif from ret_data   | contour_save_path | string   | Path to save generated contour visualization image               |
|            |                                                  | viz_3d_save_path  | string   | Path to save 3d visualized DEM image                             |
|            |                                                  | raster_save_path  | string   | Path to save generated raster colour image                       |
| run_to_viz | This runs all processes including visualization  | contour_save_path | string   | Path to save generated contour visualization image               |
|            |                                                  | viz_3d_save_path  | string   | Path to save 3d visualized DEM image                             |
|            |                                                  | raster_save_path  | string   | Path to save generated raster colour image                       |



## Installation
