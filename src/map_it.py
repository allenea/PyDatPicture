#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 14:01:15 2019

@author: ericallen

Sample script for mapping in cartopy. 

This is a world projection with your pictures plotted as red circles on the map.
The figure is saved to your computer as set in USER_DEFINED_VARIABLES
"""

#%% MAP:SAMPLE MAP
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

def map_data(longitude,latitude,plt_name):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    
    ax.plot(longitude, latitude, 'o', color='r', transform=ccrs.PlateCarree())
    
    ax.stock_img()
    ax.coastlines()
    
    plt.savefig(plt_name)
    plt.show()
