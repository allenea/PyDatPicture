#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:38:15 2019

@author: Eric Allen
Last Modified: 7 May 2019 at 2:91PM

You must use this file with function call definition to create your own maps.

If you have multiple maps with multiples files call them all from this routine
by passing the necessary data to each.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import os

def map_data(usr_vars):
    float64 = np.float64
    ddtypes = {"Date_Time": str, "Longitude":float64,"Latitude":float64}
    plot_data = pd.read_csv(usr_vars['MAP_DATA_PATH'], dtype=ddtypes)
    latitude = plot_data['Latitude']
    longitude = plot_data['Longitude']

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    
    # TO ZOOM IN ON AN AREA
    ax.set_extent([-126., -66., 24., 51], ccrs.PlateCarree())

    ax.plot(longitude, latitude, 'o', color='r', transform=ccrs.PlateCarree())
    
    ax.stock_img()
    ax.coastlines()
    ax.add_feature(cfeature.STATES, linestyle=':')

    plt.savefig(os.path.join(usr_vars['PLOT_PATH'], "MyMap.jpeg"))
    plt.show()
    plt.close()