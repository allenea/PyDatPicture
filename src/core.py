#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 13:02:02 2019

@author: Eric Allen
Last Modified: 7 May 2019 at 12:30PM

"""

import sys
import os
import pyDatPicture as pyDat
from reverse_geocode import reverse_geocode
from detectOutliers import detectOutliers
from get_image_data import getImageData


def main(usr_vars):
    
    if usr_vars['EXTRACT_PHOTO_METADATA'] == True:
        
        getImageData(usr_vars['INPUT_PIC_DIRECTORY'],\
                     usr_vars['RAW_METADATA_FILE'],\
                     recursive=usr_vars['DO_RECURSIVE']) 
    
    else:
        if not os.path.exists(usr_vars['RAW_METADATA_FILE']):
            print("RAW_METADATA_FILE: ",usr_vars['RAW_METADATA_FILE'],\
                  "\nCould not be found. Check and Try Again.")
            sys.exit(0)
        else:
            pass

    # Process the data with quality control routines to give you a csv file
    #   with a list of time,longitude,latitude 
    data = pyDat.pyDatPicture(usr_vars)

    ## USES LIMITED GEOCODING
    if usr_vars['DETECT_OUTLIARS'] == True:   
        # SO WE CAN REDEFINE DATA FOR MAPPING IN CASE DETECT_OUTLIARS ISN'T USED
        datatmp = data 
        del data
        
        data = detectOutliers(datatmp,usr_vars,geo_fmt="degrees",\
                                  percentile=usr_vars['PERCENTILE'])
        
    if usr_vars['REVERSE_GEOCODE'] == True:
        # LIMITED TO 100 GEOCODES... Use on specific and limited pictures 
        reverse_geocode(usr_vars)
        
    if usr_vars['MAPIT'] == True:
        # Python Mapping of Data
        """ 
        PROVIDING YOUR OWN MAPPING PROGRAM? YOU <MUST> DO IT IN THE TEMPLATE FILE 
        PROVIDED BY PyDatPicture maintaining the function call as provided and
        set the variables to point to where that .py file is stored and where 
        the data is located.
        
        This program must be located in the path of MAPPING_PROGRAM
        """

        if usr_vars["MY_MAP"] == True:
            sys.path.append(usr_vars['MAPPING_PROGRAM'])
            from my_pyDatPicture_mapping import map_data
            map_data(usr_vars)

        else:
            from map_it import map_data
            map_data(data['Longitude'],data['Latitude'],usr_vars)
    
    print("\n\npyDatPicture Complete")
