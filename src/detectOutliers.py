#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 21:00:52 2019

@author: Eric Allen
Last Modified: 7 May 2019 at 11:56AM

Modified my data_randomness program that I wrote in Spatial Stats for research
to eliminate "random" points or outliers that are likely not places I've been.

Returns csv file without the "random points" - allows the user to control what
outliers are included.

- For example I've been to Newport News,VA and Niagara Falls
    but they were considered outliers. I've never been to China - remove.
"""

import numpy as np
from math import sin, cos, sqrt, asin,radians
import pandas as pd
import geopy
import geopy.geocoders
from geopy.geocoders import Nominatim

def detectOutliers(data,usr_vars,geo_fmt="degrees", percentile="99th"):
    #Data
    Longitude = list(data['Longitude'])
    Latitude = list(data['Latitude'])
    Date_Time = list(data['Date_Time'])
    
    #output file
    final_qc_file = usr_vars['OUTLIER_QC_METADATA_FILE']
    
    #Setup geocoder
    geopy.geocoders.options.default_user_agent = 'my_app/1'
    geopy.geocoders.options.default_timeout = 100
    geolocator = Nominatim()
        
    #reverse geocode function that will be called
    def reverse_geocode(Latitude,Longitude):
        latlonstr = str(Latitude)+" , "+str(Longitude)
        Address, (lats, longs) = geolocator.reverse(latlonstr)   
        return Address        
    
    n = len(Latitude)
    d_list = []
    
    nearestNeighbor = []
    #Loop through the data to calculate the distances for all points.
    #Keep only the nearest neighbor (min) for each in k loop
    for k in range(n):
        if geo_fmt == "dms":
            ltdeg =float(Latitude[k].split(".")[0])
            ltmin = float(Latitude[k].split(".")[1])
            ltsec = float(Latitude[k].split(".")[2])
            lgdeg = float(Longitude[k].split(".")[0])
            lgmin = float(Longitude[k].split(".")[1])
            lgsec = float(Longitude[k].split(".")[2])
            ddlong = lgdeg + lgmin / 60.0 + lgsec / 3600.0
            ddlat = ltdeg + ltmin / 60.0 + ltsec / 3600.0

        elif geo_fmt == "degrees":
            ddlong = Longitude[k]
            ddlat = Latitude[k]
    
        #Calculate the distance for all points at each point. keep all distances
        # in stDistance for that point to then identify the minimum
        stDistance=[]
        for j in range(n):
            if k != j:
                if geo_fmt == "dms":
                    ltdeg2 =float(Latitude[j].split(".")[0])
                    ltmin2 = float(Latitude[j].split(".")[1])
                    ltsec2 = float(Latitude[j].split(".")[2])
                    lgdeg2 = float(Longitude[j].split(".")[0])
                    lgmin2 = float(Longitude[j].split(".")[1])
                    lgsec2 = float(Longitude[j].split(".")[2])
                    ddlong2 = lgdeg2 + lgmin2 / 60.0 + lgsec2 / 3600.0
                    ddlat2 = ltdeg2 + ltmin2 / 60.0 + ltsec2 / 3600.0

                elif geo_fmt == "degrees":
                    ddlong2 = Longitude[j]
                    ddlat2 = Latitude[j]
                    
                #Haversine - in decimal degrees --> Radians in haversine
                d = haversine(ddlong, ddlat, ddlong2, ddlat2)
                
                #Law of Cosine
                #d = acos(((sin(rlat)*sin(rlat2))+(cos(rlat)*cos(rlat2)*\
                        # cos(rlong-rlong2))))
                
                stDistance.append(d)
                d_list.append(d) #distance list
                
        #Find Nearest for that point
        nearestNeighbor.append(min(stDistance))
    
    #Calculate stats on the dataset   
    Mean = np.mean(d_list)
    MeanNearest = np.mean(nearestNeighbor)
    StandardDeviation = np.std(d_list)
    STDNearest = np.std(nearestNeighbor)
    
    
    print("\n",len(Latitude)," locations")
    print("Units: Kilometers")
    print("-----------------")
    print("Mean Distance:                         %10.3f"%Mean)
    print("Mean Nearest Neighbor:                 %10.3f"%MeanNearest)
    print("Standard Deviation Distance:           %10.3f"%StandardDeviation)
    print("Standard Deviation Nearest Neightbor:  %10.3f"%STDNearest)
    print()
    
    #Get out of range value to identify outliers
    OUT_OF_RANGE = get_out_of_range_value(percentile,MeanNearest,STDNearest)
    
    #Print Info to Console
    print("USING PERCENTILE: ", percentile)
    print("OUT OF RANGE VALUE: ", OUT_OF_RANGE)
    
    outHEADER = ["Date_Time", "Longitude", "Latitude"]

    #Figure out what to keep and what to QC
    OUT_DATA = np.zeros((len(Latitude),len(outHEADER)), dtype = object)
    count = 0
    for idx in range(len(nearestNeighbor)):
        if nearestNeighbor[idx] >= OUT_OF_RANGE:
            #Out of range: Get Users Feedback to Confirm
            print()
            address = reverse_geocode(Latitude[idx],Longitude[idx])
            print(address)
            response = get_response()
            answer = user_response(response)
            if answer is False:
                continue
            elif answer is True:
                # SAVE GOOD DATA
                OUT_DATA[count,0] = Date_Time[idx]
                OUT_DATA[count,1] = Longitude[idx]
                OUT_DATA[count,2] = Latitude[idx]
                count +=1
            else:
                print("INVALID RESPONSE.... Continuing....")
        else:
            # SAVE GOOD DATA
            OUT_DATA[count,0] = Date_Time[idx]
            OUT_DATA[count,1] = Longitude[idx]
            OUT_DATA[count,2] = Latitude[idx]
            count +=1
    
    
    #Trim down to the size actually used      
    OUT_DATA = OUT_DATA[:count,:]
    print("Number of Unique Pictures with Geolocation after QC: ", count)
    df = pd.DataFrame(OUT_DATA,columns=outHEADER)
    df.to_csv(final_qc_file,index=False)
    return df

############ FUNCTIONS CALLED BY detectOutlairs ###############################

def get_response():
    response = str(input("Are you sure you want to remove the location above"+\
                         " from your final picture dataset: (yes) or (no)\n"))
    return response
    
def user_response(response):
    response = (response.lower()).strip()
    if "yes" == response:
        return False
    elif "no" == response:
        return True
    else:
        print("Invalid Reponse.... Enter (  yes  ) or (  no  )")
        new_response = get_response() 
        return user_response(new_response)
    
    
#FUNCTIONS
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in radians...)
    
    units
    INPUT: Decimal Degrees
    OUTPUT: Kilometers
    
    return distance in kilometers
    """
    # PUT IT IN RADIANS -- originally was passing radians but this is easier.     
    lon1, lat1, lon2, lat2 = map(radians, (lon1, lat1, lon2, lat2))
    
    # haversine formula 
    dlon = lon2 - lon1
    dlat = lat2 - lat1 
    
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    
    c =asin(sqrt(a)) 
    
    #Radius of Earth in kilometers. Multiply by 1000 for meters. 3956 for miles
    r = 6371. 
    
    return 2 * c * r


def get_percentile_value(percentile):
    """Options Below"""
    percentile_z_key = {"1st":-2.326, "2.5th":-1.960, "5th":-1.645,\
                        "10th":-1.282, "25th":-0.675, "50th":0,\
                        "75th":0.675, "90th":1.282, "95th":1.645,\
                        "97.5th":1.960, "99th":2.326}
    try:
        value = percentile_z_key[percentile]
    except:
        print("Invalid Percentile Option: Using Default of 99th percentile.\n",\
              "Continuing....")
        value = percentile_z_key["99th"]
        
    return value

def get_out_of_range_value(percentile,MeanNearest,STDNearest):
    return MeanNearest + get_percentile_value(percentile)*(STDNearest) 
