#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 13:02:02 2019

@author: ericallen

BEFORE YOU BEGIN:
    - Download/Install Anaconda 3  -> Use Spyder for programming. Install the required libraries from the documentation.
            This program might be able to install the necessary conda libraries but it's untested.
    - Download/Install EXIFTOOLS - Phil Harvey
    
    - edit USER_DEFINED_VARIABLES as needed: Often times the default should suffice.
        One additional change can be made on line 26 (MARKED WITH TODO) for raw data file name/path.
    
TO RUN:
    
    python main.py           from the command line
    Click the Green "Play" button in Anaconda/Spyder




This program extracts geolocation data from photos (returns a csv) and then this program takes that
csv and cleans the data returning a second csv with all photos that have geographic information.

You are free to modify this code under the GNU General Public License v3.0

OUTPUT (CSV FILE):
    Date_Time - (str) YYYY-mm-dd HH:MM:SS (Depends on device time at photo)
    Latitude - (float) Decimal Degrees (Negative values are South)
    Longitude - (float) Decimal Degrees (Negative values are West)
    * Address -   OPTIONAL IN A LIMITED CAPACITY-Free (str) Reverse geocoded address (OR WITH PAID API)

"""

import sys
import os
import pyDatPicture as pyDat
from map_it import map_data
from reverse_geocode import reverse_geocode
from detectOutliers import detectOutliers
from get_image_data import getImageData


def main(usr_vars):
    
    if usr_vars['EXTRACT_PHOTO_METADATA'] == True:
        getImageData(usr_vars['INPUT_PIC_DIRECTORY'], usr_vars['RAW_METADATA_FILE'], recursive=usr_vars['DO_RECURSIVE']) 
    else:
        if not os.path.exists(usr_vars['RAW_METADATA_FILE']):
            print("RAW_METADATA_FILE: ",usr_vars['RAW_METADATA_FILE'],"\nCould not be found. Check and Try Again.")
            sys.exit(0)
        else:
            pass

    # Process the data with quality control routines to give you a csv file with a list of time,longitude,latitude 
    data = pyDat.pyDatPicture(usr_vars)

    if usr_vars['DETECT_OUTLIARS'] == True:   
        ## USES LIMITED GEOCODING
        QCd_data = detectOutliers(data,usr_vars,geo_fmt="degrees",percentile=usr_vars['PERCENTILE'])
        
    if usr_vars['REVERSE_GEOCODE'] == True:
        # LIMITED TO 100 GEOCODES... Use on specific and limited pictures 
        reverse_geocode(usr_vars)
        
    if usr_vars['MAPIT'] == True:
        # Python Mapping of Data
        map_data(QCd_data['Longitude'],QCd_data['Latitude'],usr_vars['PLOT_PATH'])
    
    print("\n\npyDatPicture Complete")