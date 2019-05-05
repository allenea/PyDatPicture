#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 20:45:32 2019

@author: Eric Allen
Last Modified: May 4, 2019 3:30PM

This file uses the extracted geolocation data from photos and cleans the data,
      returning a second csv with all photos that have geographic information.

You are free to modify this code under the GNU General Public License v3.0

OUTPUT (CSV FILE):
    Date_Time - (str) YYYY-mm-dd HH:MM:SS (Depends on device time at photo)
    Longitude - (float) Decimal Degrees (Negative values are West)
    Latitude - (float) Decimal Degrees (Negative values are South)

"""
#%% LOAD SOFTWARE
import sys
import os
import numpy as np
import pandas as pd
from src.reformat_time import reformatTime
from src.get_lat_lon import getLatLon

def pyDatPicture(usr_vars):
    """ 
    INPUT: A dictionary with all the USER_VARIABLES
    OUTPUT: A csv file with time,longitude,latitude
    RETURNS: Pandas DataFrame with the output data
    """
    
    #Make sure the pictures directory exists and is properly input
    if os.path.isdir(usr_vars['INPUT_PIC_DIRECTORY']) is False:
        print("You provided an invaid path to your photos. Please check and try again.")
        sys.exit(0)
        
    if usr_vars['RAW_METADATA_FILE'] == "":
        print("You have not provided an accurate path to the raw photo metadata.\nIf you have not retrieved the data, set EXTRACT_PHOTO_METADATA to True." )
        sys.exit(0)
        
    # Specify or replace dtype = ddtypes  with low_memory=False... works either way but declaring is a little more efficient
    float64 = np.float64
    # If any of these change your best bet is to remove this and set low_memory=False where the file is being read in below
    ddtypes = {"SourceFile": str, "Model":str,\
                    "DateTimeOriginal":object, "GPSDateStamp":object,\
                    "GPSTimeStamp":object, "GPSLatitude":object,\
                    "GPSLatitudeRef":str, "GPSLongitude": object,\
                    "GPSLongitudeRef":str, 'GPSAltitude':object, 'GPSAltitudeRef':str, 'GPSSpeed':float64,\
                    'GPSSpeedRef':str, 'GPSTrack':object, 'GPSTrackRef':object, 'GPSImgDirection':float64, 'GPSImgDirectionRef':str}
    
    # READ IN THE DATA
    metadata = pd.read_csv(usr_vars['RAW_METADATA_FILE'], dtype=ddtypes) #, low_memory=False)
    metadata = metadata.fillna("")
    headers  = metadata.columns.tolist()
    print(headers); print();
    
    ## VARIABLES
    """ NOT INCLUDED IN THE RAW DATA
    ## [ -Common ] variables
    #FileName = metadata['FileName']
    #FileSize = metadata['FileSize']
    #ImageSize = metadata['ImageSize']
    #Quality = metadata['Quality']
    #FocalLength = metadata['FocalLength']
    #ShutterSpeed = metadata['ShutterSpeed']
    #Aperture = metadata['Aperture']
    #ISO = metadata['ISO']
    #WhiteBalance = metadata['WhiteBalance']
    #Flash = metadata['Flash']
    """
    SourceFile =  metadata['SourceFile']
    Model = metadata['Model']
    DateTimeOriginal = metadata['DateTimeOriginal'].astype(str)
    
    
    print("Unique Devices on File: ", list(set(Model)))
    print("\nAny unrecognized devices MAY have been recieved/downloaded via AirDrop, Internet, Social Media, SMS, iMessage, etc.\n")
    
    """ THESE VARIABLES ARE ALL AVAILABLE - SELECT VARIABLES ARE USED"""
    # [ -gps: ]  options 
    #GPSDate = metadata['GPSDateStamp'].astype(str)
    #GPSTime = metadata['GPSTimeStamp'].astype(str)
    GPSLat = metadata['GPSLatitude'].astype(str)
    GPSLon = metadata['GPSLongitude'].astype(str)
    GPSLatRef = metadata['GPSLatitudeRef']
    GPSLonRef = metadata['GPSLongitudeRef']
    
    GPSSpeed= metadata['GPSSpeed']
    #GPSSpeedRef= metadata['GPSSpeedRef']
    GPSAltitude= metadata['GPSAltitude']
    #GPSAltitudeRef= metadata['GPSAltitudeRef']
    #GPSTrack= metadata['GPSTrack']
    #GPSTrackRef= metadata['GPSTrackRef']
    #GPSImgDirection= metadata['GPSImgDirection']
    #GPSImgDirectionRef= metadata['GPSImgDirectionRef']
    
    
    keep_data = np.zeros((len(GPSLon),3), dtype = object)
    count = 0
    for idx in range(len(SourceFile)):
        
        #Check for geographic data
        if GPSLat[idx] != "" or GPSLon[idx] != "":
            ddlat, ddlon = getLatLon(GPSLat[idx],GPSLon[idx],GPSLatRef[idx],GPSLonRef[idx])
            dtime = reformatTime(DateTimeOriginal[idx])
        else:
            continue
        
        #QC Check for speed and altitude: IF > 75KMH and ABOVE 1000m ASL
        if usr_vars['REMOVE_PHOTOS_TAKEN_BY_PLANE'] == True and GPSSpeed[idx] != "" and GPSAltitude[idx] != "":
            if float(GPSSpeed[idx]) > 75 and float(GPSAltitude[idx].split("m")[0])>1000:
                continue
            
        #QC Check for device: If not on list of my devices then don't include.
        if usr_vars['ONLY_MY_DEVICES'] == True:
            if Model[idx] not in usr_vars['MY_DEVICES']:
                continue
            
        # SAVE GOOD DATA
        keep_data[count,0] = dtime
        keep_data[count,1] = ddlon
        keep_data[count,2] = ddlat
        count +=1
    
    #Trim down to the size actually used      
    keep_data = keep_data[:count,:]
    print("Number of Pictures with geolocation: ",count)
    
    outHEADER = ["Date_Time", "Longitude", "Latitude"]
    dfwrite = pd.DataFrame(keep_data,columns=outHEADER)
    dfsort = dfwrite.sort_values(['Date_Time'])
    df_drop = dfsort.drop_duplicates()
    df = pd.DataFrame(df_drop,columns=outHEADER)
    print("Number of Unique Pictures with geolocation: ", len(df))
    df.to_csv(usr_vars['POST_PROCESSED_DATA'],index=False)
    
    
    return df