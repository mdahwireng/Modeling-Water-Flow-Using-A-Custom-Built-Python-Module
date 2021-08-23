import rasterio as rio
from rasterio.plot import show, show_hist
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def viz_raster(tif_path):
    image_data = rio.open(tif_path)
    fig, ax = plt.subplots(figsize=(5, 5))

    # use imshow so that we have something to map the colorbar to
    image_hidden = ax.imshow(image_data, 
                            cmap='Greys', 
                            vmin=-30, 
                            vmax=30)

    # plot on the same axis with rio.plot.show
    image = rio.plot.show(image_data, 
                        transform=image_data.transform, 
                        ax=ax, 
                        cmap='Greys', 
                        vmin=-30, 
                        vmax=30)

    # add colorbar using the now hidden image
    fig.colorbar(image_hidden, ax=ax)

def plot_raster_(tifile: str, img_save_path,title='', notebook=False):
    """
    Plots raster tif image both in log scale(+1) and original verion
    """
    spr_tif = tifile
    raster_spr = rio.open(spr_tif)
    spr_data = raster_spr.read(1)
    fig, (axlog, axorg) = plt.subplots(1, 2, figsize=(14,7))
    im1 = axlog.imshow(np.log1p(spr_data)) 

    plt.title("{}".format(title), fontdict = {'fontsize': 15})  
    plt.axis('off')
    plt.colorbar(im1, fraction=0.03)
    if notebook:
      fig.savefig(img_save_path)
      plt.show()
    else:
      fig.savefig(img_save_path)


def viz_contour(tif_path,img_path,title,notebook=False):
    image_data = rio.open(tif_path)
    fig, (axrgb, axhist) = plt.subplots(1, 2, figsize=(14,7))
    show((image_data), cmap='Greys_r', contour=True, ax=axrgb, title=title)
    show_hist(image_data, bins=50, histtype='stepfilled',
          lw=0.0, stacked=False, alpha=0.3, ax=axhist)
    if notebook:
      fig.savefig(img_path)
      plt.show()   
    else:
      fig.savefig(img_path)


def viz_3d(csv_path,title, img_save_path,skip_val=None, notebook=False):
    points = pd.read_csv(csv_path)
    
    if skip_val:
        filter = [True if i%skip_val==0 else False for i in range(len(points))]
        points = points[filter]

    fig = plt.figure()
    fig.set_size_inches(18.5, 10.5)
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points['X'],   
            points['Y'],   
            points['Z'],   
            c=points['Z'],
            cmap='terrain',
            marker=",",
                alpha=0.02)
    ax.axis('auto')
    ax.set_title(title)

    if notebook:
      plt.show()
      fig.savefig(img_save_path)

    else:
      fig.savefig(img_save_path)