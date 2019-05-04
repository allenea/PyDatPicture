#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 20:45:32 2019

@author: Eric Allen
Last Modified: May 4, 2019 12:52AM

This program extracts geolocation data from photos (returns a csv) and then this program takes that
csv and cleans the data returning a second csv with all photos that have geographic information.

Calls pDP_Setup to make sure that you have everything installed.

You are free to modify this code under the GNU General Public License v3.0

OUTPUT (CSV FILE):
    Date_Time - (str) YYYY-mm-dd HH:MM:SS (Depends on device time at photo)
    Latitude - (float) Decimal Degrees (Negative values are South)
    Longitude - (float) Decimal Degrees (Negative values are West)
    * Address -  (str) Reverse geocoded address (REQUIRES PAID API or LIMITED ACCESS) (OPTIONAL)
    
    
    The later in the night it gets, the sloppier my code is becoming but this should work.
"""

from pDP_Setup import setup_pyDatPicture
import sys

isSetUp = setup_pyDatPicture()

if isSetUp == False:
    print("ERROR: THE REQUIRED SOFTWARE IS NOT INSTALLED ON YOUR MACHINE.\nFollow pyDatPicture documentation to proceed.")
    sys.exit(0)
else:
    import getpass
    import os
    from pathlib import Path
    import numpy as np
    import pandas as pd
    #import datetime as dt ## CALLED IN reformat_time
    from reformat_time import reformatTime
    from get_lat_lon import getLatLon
    from get_image_data import getImageData

USER_ID = getpass.getuser()
OS_SYSTEM = sys.platform

#%% USER DEFINED VARIABLES - SEE DOCUMENTATION
#pyDatPicture assumes that the user is running from their picture directory on their local machine
########################### EDIT THESE AS NECESSARY ###################################################

## TODO - Get the data (True)? Already have the data(False)?
EXTRACT_PHOTO_METADATA = False


## TODO - Where are your pictures located? Provide the directory.
if OS_SYSTEM == "darwin":  #APPLE- MAC
    INPUT_PIC_DIRECTORY = os.path.join("/","Users", USER_ID, "Pictures")  #macos
    
elif OS_SYSTEM == "win32": #MICROSOFT - WINDOWS
    INPUT_PIC_DIRECTORY = os.path.join( "C:", "Users", USER_ID,"Pictures")  #windows
else: #linux,?
    print("You have not provided an accurate path to the INPUT_PIC_DIRECTORY.  If you are a linux user please set this yourself on line 60." )
    sys.exit(0)
#INPUT_PIC_DIRECTORY = '/Users/'+USER_ID+'/Pictures/' or '/Users/yourusername/Pictures/'   #macos


## TODO - Final output file name: -  Time, Latitude, Longitude
POST_FILENAME = "ImageMetadata_final.csv" 


## TODO - Output file location
POST_PROCESSED_DATA = INPUT_PIC_DIRECTORY+POST_FILENAME


# DO YOU ALREADY HAVE THE PHOTO METADATA? (include Path and filename)
if EXTRACT_PHOTO_METADATA == False:
    
    RAW_FILE = "ImageMetadata_raw.csv"
        
    ## RAW_METADATA_FILE = "/Users/"+USER_ID+"/Pictures/ImageMetadata_raw.csv"  or "/Users/yourusername/Pictures/ImageMetadata_raw.csv" #macos
    
    ## TODO - NAME FILE AND PATH TO THE FILE, IF YOU ALREADY HAVE ONE 
    # - macOS
    if OS_SYSTEM == "darwin": # APPLE - MAC
        RAW_METADATA_FILE = Path("/","Users", USER_ID, "Pictures", RAW_FILE)  #macos
    
    # - Windows
    elif OS_SYSTEM == "win32": # MICROSOFT - WINDOWS
        RAW_METADATA_FILE = os.path.join( "C:", "Users", USER_ID, "Pictures", RAW_FILE)  #windows
        
    else: # Linux,?
        print("You have not provided an accurate path to the raw photo metadata.\nIf you have not retrieved the data, set EXTRACT_PHOTO_METADATA to True." )
        sys.exit(0)
        
else:
    # GET METADATA IF NEEDED    
    RAW_METADATA_FILE = getImageData(INPUT_PIC_DIRECTORY)

## TODO - SET QUALITY CONTROL OPTIONS
# Quality Control 1: Remove Photos - Speed & Altitude
REMOVE_PHOTOS_TAKEN_BY_PLANE = False

# Quality Control 2: Remove Photos - By Device
ONLY_MY_DEVICES = False
MY_DEVICES = []   #MY_DEVICES = ["iPhone 5","iPhone 6","iPhone X", "HERO4 Silver"]  ## EXAMPLE
##########################################################################################

## PRINT OUT USER INFORMATION
print("USER AND RUN INFORMATION")
print("------------------------")
print("SETUP SUCCESSFUL: ",isSetUp)
print("ASSUMED USER_ID: ", USER_ID)
print("ASSUMED OS_SYSTEM: ", OS_SYSTEM)
print()
print("EXTRACT_PHOTO_METADATA: ", EXTRACT_PHOTO_METADATA)
print("INPUT_PIC_DIRECTORY: ", INPUT_PIC_DIRECTORY)
print("POST_FILENAME: ", POST_FILENAME)
print("POST_PROCESSED_DATA: ", POST_PROCESSED_DATA)
print("REMOVE_PHOTOS_TAKEN_BY_PLANE: ", REMOVE_PHOTOS_TAKEN_BY_PLANE)
print("ONLY_MY_DEVICES: ", ONLY_MY_DEVICES)
print("MY_DEVICES: ", MY_DEVICES)
print();print()


#%%###################### MAIN PROGRAM ######################
#Make sure the pictures directory exists and is properly input
if os.path.isdir(INPUT_PIC_DIRECTORY) is False:
    print("You provided an invaid path to your photos. Please check and try again.")
    sys.exit(0)
    
if RAW_METADATA_FILE == "":
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
metadata = pd.read_csv(RAW_METADATA_FILE, dtype=ddtypes) #, low_memory=False)
metadata = metadata.fillna("")
headers  = metadata.columns.tolist()
print(headers); print();


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
    if REMOVE_PHOTOS_TAKEN_BY_PLANE == True and GPSSpeed[idx] != "" and GPSAltitude[idx] != "":
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
print("Number of Pictures with geolocation: ",count)

outHEADER = ["Time", "Longitude", "Latitude"]
dfwrite = pd.DataFrame(keep_data,columns=outHEADER)
dfsort = dfwrite.sort_values(['Time'])
df_drop = dfsort.drop_duplicates()
df = pd.DataFrame(df_drop,columns=outHEADER)
print("Number of Unique Pictures with geolocation: ", len(df))
df.to_csv(POST_PROCESSED_DATA,index=False)


#%% Reverse geocode to get location address
"""  MUST PAY FOR API... The free API (Nominatim) kicks me out of their server after a few hundred calls.
## OPTIONAL - REVERSE FIND ADDRESS FROM COORDINATES  ... This can be done in ArcGIS Pro for with your Pro Account (and much quicker).  
## FYI: Using ArcGIS Pro account it costs 40 credits per 1,000 geocodes.

if 'Anaconda' in sys.version:
    import conda.cli
    if 'geopy' in sys.modules:  import geopy.geocoders
    else:   conda.cli.main('conda', 'install',  '-y', 'geopy')

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
df_w_Address.to_csv(POST_PROCESSED_DATA,index=False)
"""

#%% MAP:SAMPLE MAP
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

ax.plot(df['Longitude'], df['Latitude'], 'o', color='r', transform=ccrs.PlateCarree())

ax.stock_img()
ax.coastlines()

plt.show()