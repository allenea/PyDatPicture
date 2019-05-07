#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 14:21:41 2019

@author: Eric Allen
Last Modified: 7 May 2019 at 11:55AM

***** LIMITED TO FILES WITH LESS THAN 100 data points.******

Take specific + limited points you want analysed and pass them to this program

## OPTIONAL - REVERSE FIND ADDRESS FROM COORDINATES

## FYI: Using Python most require payment, but Nominatim is free for now

## FYI: Using ArcGIS Pro account (much quicker and easier) it costs
             40 credits per 1,000 geocodes and requires a Pro account.  

"""
# Reverse geocode to get loc. address - NOT INC BUT HERE IS SOME STARTER CODE
import pandas as pd
import numpy as np
import geopy
import geopy.geocoders
from geopy.geocoders import Nominatim

def reverse_geocode(usr_vars):
    #Setup geocoder
    geopy.geocoders.options.default_user_agent = 'my_app/1'
    geopy.geocoders.options.default_timeout = 100
    geolocator = Nominatim()
    
    #### READ IN THE DATA (INITIALIZE DTYPES)
    float64 = np.float64
    ddtypes = {"Date_Time": str, "Longitude":float64,"Latitude":float64}
    
    metadata = pd.read_csv(usr_vars['POST_PROCESSED_DATA'], dtype=ddtypes) 
                                                         #, low_memory=False)
    IN_DATA = np.array(metadata)
    
    #HARD LIMIT OF 100 GEOCODES PERMITTED (First 100)...
    if len(IN_DATA) > 100:
        IN_DATA = IN_DATA[:100,:]
    
    #Initialize
    OUT_DATA = np.zeros((len(IN_DATA),4), dtype = object)
    OUT_DATA[:,0] = IN_DATA[:,0]
    OUT_DATA[:,1] = IN_DATA[:,1]
    OUT_DATA[:,2] = IN_DATA[:,2]
    
    geocode_file = usr_vars['GEOCODE_METADATA_FILE']
    
    outHEADER = ["Date_Time", "Longitude", "Latitude","Address"]
    
    #Loop through and geocode
    for idy in range(len(OUT_DATA)):
        latlonstr = str(OUT_DATA[idy][2])+" , "+str(OUT_DATA[idy][1])
        OUT_DATA[idy][3], (latitude, longitude) = geolocator.reverse(latlonstr)
        #print(OUT_DATA[idy][3])
        
    #Return Output File
    df_w_Address = pd.DataFrame(OUT_DATA,columns=outHEADER)
    df_w_Address.to_csv(geocode_file,index=False)
    return df_w_Address