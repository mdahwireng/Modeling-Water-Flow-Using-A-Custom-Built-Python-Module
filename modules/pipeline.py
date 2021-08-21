import json
import pdal

def get_raster_terrain(file_path ,bounds , geojson_path , tiff_path,pipeline_path):
    
    with open(pipeline_path) as json_file:
        the_json = json.load(json_file)
        
        
    the_json['pipeline'][0]['bounds']=bounds
    the_json['pipeline'][0]['filename']=file_path
    the_json['pipeline'][8]['filename']=geojson_path
    the_json['pipeline'][7]['filename']=tiff_path
    
    pipeline = pdal.Pipeline(json.dumps(the_json))
    
    try:
        
        exxec = pipeline.execute()
        metadata = pipeline.metadata
        
    except RuntimeError as e :
        print(e)
        pass
      