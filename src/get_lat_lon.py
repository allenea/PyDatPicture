#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 00:38:19 2019

@author: Eric Allen
Last Modified: 7 May 2019 at 11:58AM

parses the lat/lon information to covert from DMS to DD adjusted for reference.
"""

def getLatLon(lat,lon,lat_ref, lon_ref):
    """
    Takes the string for latitude and longitude. 
    Parses it to extract the necessary elements to calculate in decimal degrees.
    Then applies the reference variable.
    
    INPUT (SINGLE VALUE)
        lat - (str) Latitude
        lon - (str) Longitude
        lat_ref - (str) Reference Latitude (N/S)
        lon_ref - (str) Reference Longitude (E/W)
        
    OUTPUT:
        ddlat - (float) Decimal Degree Latitude 
        ddlon - (float) Decimal Degree Longitude 
    """
    try:
        #Latitude
        tmp1 = str(lat).split("deg")
        latDeg = tmp1[0]
        tmp2 = tmp1[1].split("'")
        latMin = tmp2[0]
        tmp3 = tmp2[1].split('"')
        latSec = tmp3[0]
        
        #Longitude
        tmp12 = str(lon).split("deg")
        lonDeg = tmp12[0]
        tmp22 = tmp12[1].split("'")
        lonMin = tmp22[0]
        tmp32 = tmp22[1].split('"')
        lonSec = tmp32[0]
    except:
        return None, None
    
    #Convert to Decimal Degrees
    ddlat = float(latDeg) + float(latMin) / 60.0 + float(latSec) / 3600.0
    ddlon = float(lonDeg) + float(lonMin) / 60.0 + float(lonSec) / 3600.0 
    
    #Apply reference variables 
    if "South" in lat_ref:
        ddlat = ddlat * -1
        
    if "W" in lon_ref:
        ddlon = ddlon * -1
            
    return ddlat, ddlon