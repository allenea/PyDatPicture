#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 19:17:02 2019

@author: ericallen

THIS FILE BETWEEN THE rows of ############ make any changes that will impact 
how the run is done. Otherwise the default settings will be used.
"""

# Execute main() function

import sys
import getpass
import os
import user_variables as uv
from print_run_info import print_info
from core import main

def set_user_vars():
    
    # Get Systems Info
    USER_ID = getpass.getuser()
    OS_SYSTEM = sys.platform

    my_run = uv.USER_DEFINED_VARIABLES()
    
    #DEFAULT VARIABLES
    my_run.get_default_data()
    
###################### EDIT BETWEEN HERE TO CHANGE VARIABLES ##################
    
    #Default: True
    my_run.EXTRACT_PHOTO_METADATA = True
    
    #### Default: Pictures directory/folder for Windows and Mac users
    ####          (/Users/username/Pictures/)
    #my_run.INPUT_PIC_DIRECTORY = "/Users/"+getpass.getuser()+"/Desktop/TEST/"
    
    #Default: Where you run the code
    #my_run.OUTPUT_DIRECTORY = "/Users/"+getpass.getuser()+"/Desktop/"
    my_run.OUTPUT_DIRECTORY = os.path.abspath("../Output")

    #Default: "ImageMetadata_raw.csv"
    #my_run.RAW_FILE = "test_ImageMetadataRaw.csv"
    
    #Default: "ImageMetadata_geocode.csv"
    #my_run.GEOCODE_FILE = "test_ImageMetadata_geocode.csv"
    
    #Default: "ImageMetadata_remove_outliers.csv"
    #my_run.OUTLIARS_FILE = "test_ImageMetadata_remove_outliers.csv"
    
    #Default: "ImageMetadata_final.csv"
    #my_run.POST_FILE = "test_ImageMetadata_final.csv"

    #Default: True
    #my_run.DETECT_OUTLIARS = False

    #### Default: "99th"
    """
    Preset Options = 1st, 2.5th, 5th, 10th, 25th, 50th, 75th, 90th, 95th, 
                    97.5th, 99th
    """
    #my_run.PERCENTILE = "95th"
    
    #Default: True
    #my_run.REMOVE_PHOTOS_TAKEN_BY_PLANE = False
    
    #Default: False
    #my_run.SELECT_DEVICES = True
    
    #Default: []
    #my_run.DEVICES = ["iPhone X"]
    
    #Default: True
    #my_run.DO_RECURSIVE = False
    
    #Default: True
    #my_run.MAPIT = False
    
    #Default: False
    #my_run.MY_MAP = True
    
    #Default: ImageMetadata_final.csv
    #my_run.MAP_DATA_FILE = "ImageMetadata_final.csv"
    
    #Default: OUTPUT_DIRECTORY/Data/ Path
    #my_run.MAP_DATA_PATH = "/Users/"+getpass.getuser()+"/Documents/GitHub/PyDatPicture/output/Data/"

    #Default: The main PyDatPicture directory where the sample script is kept
    #my_run.MAPPING_PROGRAM = os.path.abspath("../")

    #Default: OUTPUT_DIRECTORY +'/Figures/'
    my_run.PLOT_PATH = os.path.join(my_run.OUTPUT_DIRECTORY,"Figures")
    
    #Default: False
    #my_run.REVERSE_GEOCODE = True
    
    ## INCLUDE THESE IF YOU CHANGE THE OUTPUT_DIRECTORY
    
    #Default: OUTPUT_DIRECTORY +'/Data/'+ POST_FILE
    my_run.PROCESSED_DATA = os.path.join(my_run.OUTPUT_DIRECTORY,"Data")
    
    #Default: OUTPUT_DIRECTORY +'/Data/'+ RAW_FILE
    my_run.RAW_METADATA_FILE = os.path.join(my_run.PROCESSED_DATA,\
                                            my_run.RAW_FILE)

    my_run.GEOCODE_METADATA_FILE = os.path.join(my_run.PROCESSED_DATA,\
                                                my_run.GEOCODE_FILE)

    #Default: OUTPUT_DIRECTORY +'/Data/'+ OUTLIARS_FILE
    my_run.OUTLIAR_QC_METADATA_FILE = os.path.join(my_run.PROCESSED_DATA,\
                                                   my_run.OUTLIARS_FILE)

    #Default: POST_PROCESSED_DATA +'/Data/'+ POST_FILE
    my_run.POST_PROCESSED_DATA = os.path.join(my_run.PROCESSED_DATA,\
                                              my_run.POST_FILE)
                                            
###############################################################################
    
    
    #FINAL VARIABLES
    myvars = my_run.status_variables()

    print_info(myvars, isSetUp, USER_ID, OS_SYSTEM)
    
    return myvars


if __name__ == '__main__':
    
    from pDP_Setup import setup_pyDatPicture
    
    isSetUp = setup_pyDatPicture()
    
    if isSetUp == False:
        print("ERROR: THE REQUIRED SOFTWARE IS NOT INSTALLED ON YOUR MACHINE.",\
              "\nFollow PyDatPicture documentation to proceed.")
        sys.exit(0)
    else:
        myvars = set_user_vars()

    main(myvars)