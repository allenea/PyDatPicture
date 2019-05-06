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
    #my_run.EXTRACT_PHOTO_METADATA = False
    
    #Default: Pictures directory/folder for Windows and Mac users (/Users/username/Pictures/)
    #my_run.INPUT_PIC_DIRECTORY = "/Users/"+getpass.getuser()+"/Documents/Pictures/"
    
    #Default: Where you run the code
    #my_run.OUTPUT_DIRECTORY = "/Users/"+getpass.getuser()+"/Desktop/"
    my_run.OUTPUT_DIRECTORY = os.path.abspath("../Output") #ERIC'S

    #Default: "ImageMetadata_raw.csv"
    #my_run.RAW_FILE = "newNameImageMetadataRaw.csv"
    
    #Default: "ImageMetadata_final.csv"
    #my_run.POST_FILE = "ImageMetadata_out_newname.csv"

    #Default: True
    #my_run.DETECT_OUTLIARS = False

    #Default: "99th"
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
    #my_run.REVERSE_GEOCODE = True
    
    ## INCLUDE THESE IF YOU CHANG THE OUTPUT_DIRECTORY
    
    #Default: OUTPUT_DIRECTORY +'/Data/'+ POST_FILE
    my_run.PROCESSED_DATA = os.path.join(my_run.OUTPUT_DIRECTORY,"Data")
    
    #Default: OUTPUT_DIRECTORY +'/Data/'+ RAW_FILE
    my_run.RAW_METADATA_FILE = os.path.join(my_run.PROCESSED_DATA, my_run.RAW_FILE)


    #Default: POST_PROCESSED_DATA +'/Data/'+ POST_FILE
    my_run.POST_PROCESSED_DATA = os.path.join(my_run.PROCESSED_DATA,my_run.POST_FILE)
                                            
                                            
    #Default: OUTPUT_DIRECTORY +'/Figures/'
    my_run.PLOT_PATH = os.path.join(my_run.OUTPUT_DIRECTORY,"Figures")
    
    
###############################################################################
    #FINAL VARIABLES
    myvars = my_run.status_variables()

    print_info(myvars, isSetUp, USER_ID, OS_SYSTEM)
    
    return myvars


if __name__ == '__main__':
    
    from pDP_Setup import setup_pyDatPicture

    
    isSetUp = setup_pyDatPicture()
    
    if isSetUp == False:
        print("ERROR: THE REQUIRED SOFTWARE IS NOT INSTALLED ON YOUR MACHINE.\nFollow pyDatPicture documentation to proceed.")
        sys.exit(0)
    else:
        myvars = set_user_vars()

    main(myvars)