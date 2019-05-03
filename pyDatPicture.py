#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Before you begin:
    1. Download EXIFTOOL: http://owl.phy.queensu.ca/~phil/exiftool/
        http://owl.phy.queensu.ca/~phil/exiftool/install.html    
        
        
    2. Download Python 3.6
        https://www.python.org/downloads/
        https://www.anaconda.com/distribution/#download-section (I personally like Anaconda)
        
    3. Install Numpy for Python
        https://scipy.org/install.html
        conda install -c anaconda numpy 

    4. Install Pandas for Python
        https://pandas.pydata.org/pandas-docs/stable/install.html  (you may need some additional packages... see link)
        conda install -c anaconda pandas 

    5. Install Datetime for Python
        https://pypi.org/project/DateTime/
        conda install -c trentonoliphant datetime 

    6. Grant Python/Anconda Full Disk Access (to allow it to access the Photos App on macOS)
        https://macpaw.com/how-to/full-disk-access-mojave
"""


#%% USER DEFINED VARIABLES - SEE DOCUMENTATION

#True  = I want to create the data file
#False = I already have the data file
EXTRACT_PHOTO_METADATA = False   ### You don't want to do this everytime if you can avoid it (takes time)

# Where are your pictures located? Provide the directory.
INPUT_PIC_DIRECTORY = '/Users/username/Pictures/'

# Final output file: -  Time, Latitude, Longitude
POST_FILENAME = "ImageMetadata_final.csv" 
POST_PROCESSED_DATA = INPUT_PIC_DIRECTORY+POST_FILENAME

# DO YOU ALREADY HAVE THE PHOTO METADATA? (include Path and filename)
RAW_METADATA_FILE = "/Users/username/Pictures/ImageMetadata_raw.csv"

# Quality Control 1: Remove Photos - Speed & Altitude
REMOVE_PHOTOS_TAKEN_BY_PLANE  = True # PRESET TO FALSE FOR GENERAL USE

# Quality Control 2: Remove Photos - By Device
ONLY_MY_DEVICES = False
MY_DEVICES = []
#MY_DEVICES = ["iPhone 5","iPhone 6","iPhone X", "HERO4 Silver"]


#%%
"""
Created on Sun Apr 28 20:45:32 2019

@author: Eric Allen
Last Modified: May 2, 2019 8:52PM


This program extracts geolocation data from photos (returns a csv) and then this program takes that
csv and cleans the data returning a second csv with all photos that have geographic information.

NOTHING BELOW THIS POINT SHOULD NEED TO BE TOUCHED.


You are free to modify this code under the GNU General Public License v3.0

OUTPUT (CSV FILE):
    Date_Time - (str) YYYY-mm-dd HH:MM:SS (Depends on device time at photo)
    Latitude - (float) Decimal Degrees (Negative values are South)
    Longitude - (float) Decimal Degrees (Negative values are West)
    * Address -  (str) Reverse geocoded address (REQUIRES PAID API or LIMITED ACCESS) (OPTIONAL)
"""


import pandas as pd
import numpy as np
import datetime as dt
import sys
import os

def getImageData(input_dir,recursive=True):
    """
    This function retrieves the metadata and stores it in a csv file.
    
    INPUT:
        input_dir - (str) path to the input directory
    OUTPUT:
        output_file - (str) output filename ... This can be changed by the user but is set internally.
        
        ! A csv file containing the metadata for the photos - INTERNAL PROCESS
    """
    
    #This file stores the raw data from your picture (including location)
    output_file = 'ImageMetadata_raw' # SAVED IN RUN DIRECTORY... UNLESS YOU SPECIFY A PATH

    # Check to see if the user wants to search all files and sub-folders
    if recursive == True: r = "-r"
    else: r = ""
    
    if ".csv" in output_file:  print('Your Output File Is: ' + output_file)
    else:
        if "." in output_file: output_file = output_file.split(".")[0] + ".csv"
        else:   output_file = output_file + ".csv"
        print('Your New Output File Is: ' + output_file)
   
    print("\nSTORING THE FOLLOWING DATA: Source File, Model DateTimeOriginal, GPSDateStamp, GPSTimeStamp, "+
          "GPSLatitude, GPSLatitudeRef, GPSLongitude, GPSLongitudeRef, GPSAltitude, GPSAltitudeRef, "+
          "GPSSpeed, GPSSpeedRef, GPSTrack, GPSTrackRef, GPSImgDirection, GPSImgDirectionRef")
    
    print("\nSome Warnings/Errors are Okay\n")
    
    command = ["exiftool -csv "+r+ " -ee "+input_dir+" -SourceFile -Model "+\
              "-DateTimeOriginal -gps:GPSDateStamp -gps:GPSTimeStamp -gps:GPSLatitude "+\
              "-gps:GPSLatitudeRef -gps:GPSLongitude -gps:GPSLongitudeRef -gps:GPSAltitude "+\
              "-gps:GPSAltitudeRef -gps:GPSSpeed -gps:GPSSpeedRef -gps:GPSTrack -gps:GPSTrackRef "+\
              "-gps:GPSImgDirection -gps:GPSImgDirectionRef > "+output_file]
           ###"-gps:GPSImgDirection -gps:GPSImgDirectionRef ./> "+output_file]

    
    print(command[0])
    
    os.system(command[0])
    return output_file


def getLatLon(lat,lon,lat_ref, lon_ref):
    """
    Takes the string for latitude and longitude. Parses it to extract the necessary elements to
    calculate decimal degrees. Then applies the reference variable.
    
    INPUT (SINGLE VALUE)
        lat - (str) Latitude
        lon - (str) Longitude
        lat_ref - (str) Reference Latitude (N/S)
        lon_ref - (str) Reference Longitude (E/W)
        
    OUTPUT:
        ddlat - (float) Decimal Degree Latitude 
        ddlon - (float) Decimal Degree Longitude 
    """
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
    
    #Convert to Decimal Degrees
    ddlat = float(latDeg) + float(latMin) / 60.0 + float(latSec) / 3600.0
    ddlon = float(lonDeg) + float(lonMin) / 60.0 + float(lonSec) / 3600.0 
    
    #Apply reference variables 
    if "South" in lat_ref:
        ddlat = ddlat * -1
        
    if "W" in lon_ref:
        ddlon = ddlon * -1
            
    return ddlat, ddlon

def reformatTime(date_time):
    """
    Reformats date to a YYYY-mm-dd HH:MM:SS format. Which I prefer
    
    INPUT
       date_time - (str) as formatted from the metadata
     OUPUT
         fmtTime - (str) reformatted string with date/time info
    """
    # Process Time: Not critical but I like the more traditional Format
    if date_time  != "":
        try:
            dt_tuple = dt.datetime.strptime(date_time,"%Y:%m:%d %H:%M:%S")
            fmtTime = dt_tuple.strftime("%Y-%m-%d %H:%M:%S")
        except:
            print("INVALID TIME")
            fmtTime = "NaN"
    else:
        print("Missing Date/Time")
        fmtTime = "NaN"
    return fmtTime




###################### MAIN PROGRAM ######################


#Make sure the pictures directory exists and is properly input
if os.path.isdir(INPUT_PIC_DIRECTORY) is False:
    print("You provided an invaid path to your photos. Please check and try again.")
    sys.exit(0)

#Check to see if the metadata file is provided if EXTRACT_PHOTO_METADATA is False
if EXTRACT_PHOTO_METADATA == False and RAW_METADATA_FILE == "":
    print("You have not provided an accurate path to the raw photo metadata.\nIf you have not retrieved the data, set EXTRACT_PHOTO_METADATA to True." )
    sys.exit(0)
    
# GET METADATA IF NEEDED    
if EXTRACT_PHOTO_METADATA == True:
    RAW_METADATA_FILE = getImageData(INPUT_PIC_DIRECTORY)
else: pass


 #%%   
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
metadata = pd.read_csv(RAW_METADATA_FILE, dtype=ddtypes) #, low_memory=False)
metadata = metadata.fillna("")
headers  = metadata.columns.tolist()
print(headers)
print()
## VARIABLES

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

SourceFile =  metadata['SourceFile']
Model = metadata['Model']
DateTimeOriginal = metadata['DateTimeOriginal'].astype(str)



print("Unique Devices on File: ", list(set(Model)))
print("\nAny unrecognized devices MAY have been recieved/downloaded (via AirDrop, Internet, Social Media, SMS, iMessage, etc.\n")


# [ -gps: ]  options
GPSDate = metadata['GPSDateStamp'].astype(str)
GPSTime = metadata['GPSTimeStamp'].astype(str)
GPSLat = metadata['GPSLatitude'].astype(str)
GPSLon = metadata['GPSLongitude'].astype(str)
GPSLatRef = metadata['GPSLatitudeRef']
GPSLonRef = metadata['GPSLongitudeRef']

GPSSpeed= metadata['GPSSpeed']
GPSSpeedRef= metadata['GPSSpeedRef']
GPSAltitude= metadata['GPSAltitude']
GPSAltitudeRef= metadata['GPSAltitudeRef']
GPSTrack= metadata['GPSTrack']
GPSTrackRef= metadata['GPSTrackRef']
GPSImgDirection= metadata['GPSImgDirection']
GPSImgDirectionRef= metadata['GPSImgDirectionRef']


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
    if REMOVE_PHOTOS_TAKEN_BY_PLANE == True and GPSSpeed[idx] != "" and GPSAltitude[idx] !="":
        if float(GPSSpeed[idx]) > 75 and float(GPSAltitude[idx].split("m")[0])>1000:
            continue
        
    #QC Check for device: If not on list of my devices then don't include.
    if ONLY_MY_DEVICES == True:
        if Model[idx] not in MY_DEVICES:
            continue
        
        
    # SAVE GOOD DATA
    keep_data[count,0] = dtime
    keep_data[count,1] = ddlon
    keep_data[count,2] = ddlat
    count +=1

#Trim down to the size actually used      
keep_data = keep_data[:count,:]

outHEADER = ["Time", "Longitude", "Latitude"]
dfwrite = pd.DataFrame(keep_data,columns=outHEADER)
dfsort = dfwrite.sort_values(['Time'])
df_drop = dfsort.drop_duplicates()
df = pd.DataFrame(df_drop,columns=outHEADER)
df.to_csv(POST_PROCESSED_DATA,index=False)


"""  MUST PAY FOR API... The free API (Nominatim) kicks me out of their server after a few hundred calls.
## OPTIONAL - REVERSE FIND ADDRESS FROM COORDINATES  ... This can be done in ArcGIS Pro for with your Pro Account (and much quicker).  
import geopy.geocoders
from geopy.geocoders import Nominatim
geopy.geocoders.options.default_user_agent = 'my_app/1'
geopy.geocoders.options.default_timeout = 13000
geolocator = Nominatim()


lst_df = df_drop.values.tolist()
for idy in range(len(lst_df)):
    latlonlst = str(lst_df[idy][2])+" , "+str(lst_df[idy][1])
    lst_df[idy][3], (latitude, longitude) = geolocator.reverse(latlonlst)
    time.sleep(2)
df_w_Address = pd.DataFrame(lst_df,columns=outHEADER)
"""
#%%
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1,
                     projection=ccrs.PlateCarree())

ax.plot(df['Longitude'], df['Latitude'], 'o', color='r', transform=ccrs.PlateCarree())

ax.stock_img()
ax.coastlines()


plt.show()





