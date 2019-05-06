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
import cartopy.feature as cfeature
import os

def map_data(longitude,latitude,plt_name):
    
    #%% WORLD
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    
    # TO ZOOM IN ON AN AREA
    #ax.set_extent([WESTERN_LONGITUDE, EASTERN_LONGITUDE, SOUTHERN_LATITUDE, NORTHERN_LATITUDE], ccrs.PlateCarree())

    ax.plot(longitude, latitude, 'o', color='r', transform=ccrs.PlateCarree())
    
    ax.stock_img()
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS, linestyle=':')

    plt.savefig(os.path.join(plt_name, "World.jpeg"))
    plt.show()
    plt.close
    
    #%% USA
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    
    # TO ZOOM IN ON AN AREA
    ax.set_extent([-126., -66., 24., 51], ccrs.PlateCarree())

    ax.plot(longitude, latitude, 'o', color='r', transform=ccrs.PlateCarree())
    
    ax.stock_img()
    ax.coastlines()
    ax.add_feature(cfeature.STATES, linestyle=':')

    plt.savefig(os.path.join(plt_name, "USA.jpeg"))
    plt.show()
    plt.close()
    
    
    #%% EUROPE
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    
    # TO ZOOM IN ON AN AREA
    ax.set_extent([-10., 38., 33., 70], ccrs.PlateCarree())

    ax.plot(longitude, latitude, 'o', color='r', transform=ccrs.PlateCarree())
    
    ax.stock_img()
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS, linestyle=':')

    plt.savefig(os.path.join(plt_name, "Europe.jpeg"))
    plt.show()
    plt.close()
    
    #%% AUSTRALIA
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    
    # TO ZOOM IN ON AN AREA
    ax.set_extent([100, 170, -45, 10], ccrs.PlateCarree())

    ax.plot(longitude, latitude, 'o', color='r', transform=ccrs.PlateCarree())
    
    ax.stock_img()
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS, linestyle=':')

    plt.savefig(os.path.join(plt_name, "Australia.jpeg"))
    plt.show()
    plt.close()
    
    
    #%% AFRICA
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    
    # TO ZOOM IN ON AN AREA
    ax.set_extent([-20, 60, -40, 38], ccrs.PlateCarree())
    ax.plot(longitude, latitude, 'o', color='r', transform=ccrs.PlateCarree())
    
    ax.stock_img()
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS, linestyle=':')

    plt.savefig(os.path.join(plt_name, "Africa.jpeg"))
    plt.show()
    plt.close()
    
    #%% South America
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    
    # TO ZOOM IN ON AN AREA
    ax.set_extent([-95, -30, -68, 13], ccrs.PlateCarree())

    ax.plot(longitude, latitude, 'o', color='r', transform=ccrs.PlateCarree())
    
    ax.stock_img()
    ax.coastlines()
    ax.add_feature(cfeature.STATES, linestyle=':')

    plt.savefig(os.path.join(plt_name, "SouthAmerica.jpeg"))
    plt.show()
    plt.close()    
    
    
    
    #%% Asia
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    
    # TO ZOOM IN ON AN AREA
    ax.set_extent([30, 179.9, 0, 80], ccrs.PlateCarree())

    ax.plot(longitude, latitude, 'o', color='r', transform=ccrs.PlateCarree())
    
    ax.stock_img()
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS, linestyle=':')

    plt.savefig(os.path.join(plt_name, "Asia.jpeg"))
    plt.show()
    plt.close()   

