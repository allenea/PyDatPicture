#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 13:58:29 2019

@author: ericallen

Prints out important information to the console. This should help you find your files and see if/where
something might be going wrong so you can fix it in the USER_DEFINED_VARIABLE file.
"""

def print_info(usr_vars, isSetUp,USER_ID,OS_SYSTEM):
    ## PRINT OUT USER INFORMATION
    print("USER AND RUN INFORMATION")
    print("------------------------")
    print("SETUP SUCCESSFUL: ",isSetUp)
    print("ASSUMED USER_ID: ", USER_ID)
    print("ASSUMED OS_SYSTEM: ", OS_SYSTEM)
    print()
    print("EXTRACT_PHOTO_METADATA: ", usr_vars['EXTRACT_PHOTO_METADATA'])
    print("INPUT_PIC_DIRECTORY: ", usr_vars['INPUT_PIC_DIRECTORY'])
    print("RAW_FILE: ",usr_vars['RAW_FILE'])
    print("RAW_METADATA_FILE: ",usr_vars['RAW_METADATA_FILE'])
    print()
    print("POST_FILENAME: ", usr_vars['POST_FILENAME'])
    print("POST_PROCESSED_DATA: ", usr_vars['POST_PROCESSED_DATA'])
    print("REMOVE_PHOTOS_TAKEN_BY_PLANE: ", usr_vars['REMOVE_PHOTOS_TAKEN_BY_PLANE'])
    print("ONLY_MY_DEVICES: ", usr_vars['ONLY_MY_DEVICES'])
    print("MY_DEVICES: ", usr_vars['MY_DEVICES'])
    print("DETECT_OUTLIARS: ", usr_vars['DETECT_OUTLIARS'])
    print()
    print("MAPIT: ", usr_vars['MAPIT'])
    print("PLOT_PATH: ", usr_vars['PLOT_PATH'])
    print("REVERSE_GEOCODE: ", usr_vars['REVERSE_GEOCODE'])
    print("DO_RECURSIVE: ", usr_vars['DO_RECURSIVE'])
    print()
    print("pyDatPicture was developed by Eric Allen (Twitter: @THE_Eric_Allen)")
    print();print()