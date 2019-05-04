#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 14:21:41 2019

@author: ericallen

***** LIMITED TO FILES WITH LESS THAN 100 data points.******


## OPTIONAL - REVERSE FIND ADDRESS FROM COORDINATES

## FYI: Using Python most require payment, but Nominatim is free for the time being

## FYI: Using ArcGIS Pro account (much quicker and easier) it costs
             40 credits per 1,000 geocodes and requires a Pro account. 

"""
# Reverse geocode to get location address --- NOT INCLUDED BUT HERE IS SOME STARTER CODE
import pandas as pd
import numpy as np
import sys

def reverse_geocode(usr_vars):
    
    if 'Anaconda' in sys.version:
        import conda.cli
        try:     
            import geopy
            import geopy.geocoders
            from geopy.geocoders import Nominatim
        except:
            if 'geopy' in sys.modules:
                import geopy.geocoders
                from geopy.geocoders import Nominatim
            else:
                conda.cli.main('conda', 'install',  '-y', 'geopy')
                try:
                    import geopy.geocoders
                    from geopy.geocoders import Nominatim
                except:
                    sys.exit(0)
    else:
        try:
            import geopy
            import geopy.geocoders
            from geopy.geocoders import Nominatim
        except:
            if 'geopy' in sys.modules:  pass 
            else:   print("GEOPY MODULE NOT INSTALLED")
            sys.exit(0)
    
    geopy.geocoders.options.default_user_agent = 'my_app/1'
    geopy.geocoders.options.default_timeout = 100
    geolocator = Nominatim()
    
    
    #### ACTUAL REVERSE GEOCODE STARTS HERE
    float64 = np.float64
    ddtypes = {"Date_Time": str, "Longitude":float64,"Latitude":float64}
    
    # READ IN THE DATA
    metadata = pd.read_csv(usr_vars['POST_PROCESSED_DATA'], dtype=ddtypes) #, low_memory=False)
    IN_DATA = np.array(metadata)
    
    if len(IN_DATA) > 100:
        IN_DATA = IN_DATA[:100,:]
    
    OUT_DATA = np.zeros((len(IN_DATA),4), dtype = object)
    OUT_DATA[:,0] = IN_DATA[:,0]
    OUT_DATA[:,1] = IN_DATA[:,1]
    OUT_DATA[:,2] = IN_DATA[:,2]
    
    geocode_file = usr_vars['POST_PROCESSED_DATA'].replace(".csv","_geocode.csv")
    outHEADER = ["Time", "Longitude", "Latitude","Address"]
    
    
    
    for idy in range(len(OUT_DATA)):
        latlonstr = str(OUT_DATA[idy][2])+" , "+str(OUT_DATA[idy][1])
        OUT_DATA[idy][3], (latitude, longitude) = geolocator.reverse(latlonstr)
        print(OUT_DATA[idy][3])
        
    df_w_Address = pd.DataFrame(OUT_DATA,columns=outHEADER)
    df_w_Address.to_csv(geocode_file,index=False)
    return df_w_Address