#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 13:58:29 2019

@author: Eric Allen
Last Modified: 7 May 2019 at 11:56AM

Prints out important information to the console. 

This should help you find your files and see if/where something might be going
wrong so you can fix it in the main file (calls the core.py which runs when it 
has all the necessary info.
"""

def print_info(usr_vars, isSetUp,USER_ID,OS_SYSTEM):
    ## PRINT OUT USER INFORMATION
    print("USER AND RUN INFORMATION")
    print("------------------------")
    print("SETUP SUCCESSFUL: ",isSetUp)
    print("ASSUMED USER ID: ", USER_ID)
    print("ASSUMED OS SYSTEM: ", OS_SYSTEM)
    print()
    print("EXTRACT PHOTO METADATA: ", usr_vars['EXTRACT_PHOTO_METADATA'])
    print()
    print("INPUT PICTURES DIRECTORY: ", usr_vars['INPUT_PIC_DIRECTORY'])
    print("OUTPUT DIRECTORY: ", usr_vars['OUTPUT_DIRECTORY'])
    print()
    print("RAW FILENAME: ",usr_vars['RAW_FILE'])
    print("RAW METADATA FILE: ",usr_vars['RAW_METADATA_FILE'])
    print("DO RECURSIVE: ", usr_vars['DO_RECURSIVE'])
    print()
    print("POST FILENAME: ", usr_vars['POST_FILE'])
    print("POST PROCESSED DATA: ", usr_vars['POST_PROCESSED_DATA'])
    print()
    print("REVERSE GEOCODE: ", usr_vars['REVERSE_GEOCODE'])
    print("GEOCODE FILENAME: ", usr_vars['GEOCODE_FILE'])
    print("GEOCODE METADATA FILE: ", usr_vars['GEOCODE_METADATA_FILE'])
    print()
    print("DETECT OUTLIERS: ", usr_vars['DETECT_OUTLIERS'])
    print("PERCENTILE: ", usr_vars['PERCENTILE'])
    print("OUTLIERS FILENAME: ", usr_vars['OUTLIERS_FILE'])
    print("OUTLIER QC METADATA FILE: ", usr_vars['OUTLIER_QC_METADATA_FILE'])
    print()
    print("REMOVE PHOTOS TAKEN BY PLANE: ", usr_vars['REMOVE_PHOTOS_TAKEN_BY_PLANE'])
    print("ONLY USE SELECT DEVICES: ", usr_vars['SELECT_DEVICES'])
    print("DEVICES: ", usr_vars['DEVICES'])
    print()
    print("MAP IT: ", usr_vars['MAPIT'])
    print("MY MAP: ", usr_vars["MY_MAP"])
    print("PLOT PATH: ", usr_vars['PLOT_PATH'])
    
    if usr_vars["MY_MAP"] == True:
        print("MAP_DATA_FILE: ", usr_vars['MAP_DATA_FILE'])
        print("MAP DATA PATH: ",usr_vars['MAP_DATA_PATH'])
        print("MAPPING FILE: ",usr_vars['MAPPING_FILE'])
        print("MAPPING PROGRAM: ",usr_vars['MAPPING_PROGRAM'])
    else:
        pass
    
    print()
    print()
    print("PyDatPicture was developed by Eric Allen - Meteorologist and Programmer",\
          "\n(Follow on Twitter: @THE_Eric_Allen)")
    print()
    print()

    
