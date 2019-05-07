#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 14:01:15 2019

@author: Eric Allen
Last Modified: 7 May 2019 at 11:59AM

Sample script for mapping in cartopy. 

This is a world projection with your pictures plotted as red circles on the map.

The figure is saved to your computer as set in:
     USER_DEFINED_VARIABLES for PLOT_PATH

Added for most areas of the world. I spent like 2 minutes doing this,
    so spend some time and make them artistic.
    
"""

#%% MAP:SAMPLE MAP
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import os

def map_data(longitude,latitude,usr_vars):
    
    #%% Map the World
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    
# TO ZOOM IN ON AN AREA
#ax.set_extent([WESTERN_LONGITUDE, EASTERN_LONGITUDE, SOUTHERN_LATITUDE, NORTHERN_LATITUDE],\
    #ccrs.PlateCarree())

    ax.plot(longitude, latitude, 'o', color='r', transform=ccrs.PlateCarree())
    
    ax.stock_img()
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS, linestyle=':')

    plt.savefig(os.path.join(usr_vars['PLOT_PATH'], "World.jpeg"))
    plt.show()
    plt.close
    
    #%% Map the United States
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    
    # TO ZOOM IN ON AN AREA
    ax.set_extent([-126., -66., 24., 51], ccrs.PlateCarree())

    ax.plot(longitude, latitude, 'o', color='r', transform=ccrs.PlateCarree())
    
    ax.stock_img()
    ax.coastlines()
    ax.add_feature(cfeature.STATES, linestyle=':')

    plt.savefig(os.path.join(usr_vars['PLOT_PATH'], "USA.jpeg"))
    plt.show()
    plt.close()
    
    
    #%% Map Europe
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    
    # TO ZOOM IN ON AN AREA
    ax.set_extent([-10., 38., 33., 70], ccrs.PlateCarree())

    ax.plot(longitude, latitude, 'o', color='r', transform=ccrs.PlateCarree())
    
    ax.stock_img()
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS, linestyle=':')

    plt.savefig(os.path.join(usr_vars['PLOT_PATH'], "Europe.jpeg"))
    plt.show()
    plt.close()
    
    #%% Map Australia
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    
    # TO ZOOM IN ON AN AREA
    ax.set_extent([100, 170, -45, 10], ccrs.PlateCarree())

    ax.plot(longitude, latitude, 'o', color='r', transform=ccrs.PlateCarree())
    
    ax.stock_img()
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS, linestyle=':')

    plt.savefig(os.path.join(usr_vars['PLOT_PATH'], "Australia.jpeg"))
    plt.show()
    plt.close()
    
    
    #%% Map Africa
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    
    # TO ZOOM IN ON AN AREA
    ax.set_extent([-20, 60, -40, 38], ccrs.PlateCarree())
    ax.plot(longitude, latitude, 'o', color='r', transform=ccrs.PlateCarree())
    
    ax.stock_img()
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS, linestyle=':')

    plt.savefig(os.path.join(usr_vars['PLOT_PATH'], "Africa.jpeg"))
    plt.show()
    plt.close()
    
    #%% Map South America
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    
    # TO ZOOM IN ON AN AREA
    ax.set_extent([-95, -30, -68, 13], ccrs.PlateCarree())

    ax.plot(longitude, latitude, 'o', color='r', transform=ccrs.PlateCarree())
    
    ax.stock_img()
    ax.coastlines()
    ax.add_feature(cfeature.STATES, linestyle=':')

    plt.savefig(os.path.join(usr_vars['PLOT_PATH'], "SouthAmerica.jpeg"))
    plt.show()
    plt.close()    
    
    
    
    #%% Map Asia
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    
    # TO ZOOM IN ON AN AREA
    ax.set_extent([30, 179.9, 0, 80], ccrs.PlateCarree())

    ax.plot(longitude, latitude, 'o', color='r', transform=ccrs.PlateCarree())
    
    ax.stock_img()
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS, linestyle=':')

    plt.savefig(os.path.join(usr_vars['PLOT_PATH'], "Asia.jpeg"))
    plt.show()
    plt.close()

