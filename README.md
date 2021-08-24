# Modeling Water Flow Using Lidar Data And A Custom Built Python Module
## Introduction
This project seeks to model the relief of a farm owned by AgriTech in Iowa, USA, using publicly available data from USGS 3DEP project. This project is also a case study which leads to the creation of a python package which fetch, transform and visualize publicly available satellite and Lidar data by interacting with public APIs.

This package abstracts process from the querying, retrieval, conversion of coordinate systems, creating Digital Elevation Models to the visualization of produced images in both 2d and 3d.
## Modules
There are 5 modules in all. They are <b>reference</b>, <b>get_region module</b>, <b>pipeline</b>, <b>visualize</b> and <b>process_to_viz</b> modules. This package is built on pdal, geopandas, pandas, numpy, rasterio, matplotliband shapely

## Installation
