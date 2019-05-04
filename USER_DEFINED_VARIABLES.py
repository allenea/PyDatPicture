#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 13:04:10 2019

@author: Eric Allen


You may need to adjust the 13 following parameters as needed (and two optional parameters outside this file).
    This should help serve as a guide for how to set these variables.


The DEFAULT SETTINGS are for a recursive search of the default Pictures folder location for windows/os x users with NO QUALITY CONTROL.
If this is not the case then you will need to adjust some or all of the variables below marked with the ## TODO . The number next to it
is associated with the numbers below to guide you through the process. Variables #2 and #6 will depend on what operating system you are using.
    - For windows users it is assumed that you are on the C: drive.
    - For OS X users it is assumed that you are on the /Users/ directory.



###############################################################################
VARIABLE GUIDE


1. EXTRACT_PHOTO_METADATA
    - Required
    - Default Value:
        > True
    - Data Type: Boolean (True/False)
    - Options:
        - True - I want to create the data file with EXIFTOOL.
        - False - I already have the data file and only want to process the data.
    
    
2. INPUT_PIC_DIRECTORY
    - Required
    - Data Type: String
    - File path to where your photos are located.
        - Examples below

    
3. POST_FILENAME
    - Required
    - Data Type: String
    - Filename ending in .csv where you will store the final processed metadata.
        - ex. ImageMetadata_final.csv
         
4. POST_PROCESSED_DATA
    - Required
    - Default Value:
        > INPUT_PIC_DIRECTORY+POST_FILENAME
    - Data Type: String (ending in .csv)
    - File Path and Filename you want to save the final processed metadata.
        - Contains: Time, Latitude, Longitude
        - Examples below
        
5.  RAW_FILE 
    - Required - If providing your own raw data file.
    - Data Type: String
    - Filename ending in .csv where you will store the final processed metadata.
        - ex. ImageMetadata_raw.csv
        
        
6. RAW_METADATA_FILE
    - Required - If providing your own raw data file.
    - Data Type: String
    - Default Value - depends on operating system:
        > RAW_METADATA_FILE = Path("/","Users", USER_ID, "Pictures", RAW_FILE)  #macos
        > RAW_METADATA_FILE = os.path.join( "C:", "Users", USER_ID, "Pictures", RAW_FILE)  #windows
    - File Path and Filename of your raw metadata file created by EXIFTOOL.
        - Examples below
 
    
7. DO_RECURSIVE
    - Optional
    - HIGHLY RECOMMEND THAT YOU LEAVE AS TRUE FOR THE BEST RESULTS
    - Data Type: Boolean
        - True: Search all folders and subfolders (if they exist.. doesn't matter)
        - False: Search ONLY the immediate folder
               
    
8. REMOVE_PHOTOS_TAKEN_BY_PLANE
    - Required
    - Data Type: String
    - Default Value:
        > False
    - Reason: If you are a meteorologist like me or just enjoy looking at clouds (from time to time), then 
        sometimes you have taken pictures from the airplane which are not
        representative of places that you have been.
    - Options:
        - True - Remove photos collected above 1000m and while the recorded speed is greater
            than 75 km per hour (10 kmh ~ 6 mph).
            - The exact criteria can be modified in the script
        - False - Keep all photos regardless of altitude and speed.
        
        
9. ONLY_MY_DEVICES
    - Required
    - Data Type: Boolean
    - Default Value:
        > False
    - Reason: This option gives you the opportunity to quality control what pictures are included.
        You may have downloaded or been sent photos that you did not take but are stored in your photos
        library (i.e. AirDrop, Internet, Social Media, SMS, iMessage, etc.).
    - Options:
        - True - Use only the photos from the list of approved devices.
            > MY_DEVICE
        - False - Use photos from all devices regardless of origin.
        
        
10. MY_DEVICES
    - Required
    - Data Type: List of Strings
    - Default Value:
        > []
    - The default value ( [] ) should always be used if ONLY_MY_DEVICES is False.
    - Check the available Models from the RAW_METADATA_FILE before setting this variable. 
        A unique list of devices will be output to the console at runtime after the metadata has been extracted.
        I would advice using this feature sparingly and to wait until you have seen the post-processed data.
    - Example:
        > MY_DEVICES = ["iPhone 5","iPhone 6","iPhone X", "HERO4 Silver"] # True
        > MY_DEVICES = [] # False
  
11. MAPIT
    - Required
    - Default Value:
        > True
    - Data Type: Boolean (True/False)
    - Options:
        - True - I want to map my data.
        - False - I do not want to map my data.
        
        
12. PLOT_FILE_NAME
    - Optional
    - Data Type: String
    - Default Value:
        > 'sample_plot_pictures.jpg'
    - Ideally you will write your own code to map your data in python, but this is a sample to get you started
        with a world view.... Just having it save to the source pictures folder for now.
        

13. REVERSE_GEOCODE
    - Required
    - Default Value:
        > False
    - Data Type: Boolean (True/False)
    - Options:
        - True - I want to reverse geocode up to 100 pictures to get the address where it was taken.
        - False - I do not want to reverse geocode.
        
        
OPTIONALS OUTSIDE OF THIS FILE (in src folder):               
    ** Line 26 in get_image_data.py is an optional user defined variable.  I have it set to be consistent
    but if you already have a file at that location and want to run this again, then move the file elsewhere
    or change the filename and/or path in raw_data.It's saving it to the same folder you are searching.
    
    ** Line 76 in reverse_geocode.py is an optional user defined variable. I have it set to be consistent
    but if you already have a file and want to run this again, then move that file elsewhere or change the
    filename or path in reverse_geocode.py. It's saving it to the same folder you are saving the normal output.
    
    
    Add the optionals and the recursive option in the future....
"""

### EXAMPLES (causing unicode error in the comment section)

#2 - (macOS)   ex. /Users/yourusername/Photos/
#2 - (Windows) ex. C:\Program Files\WindowsApps.
#2 - (Windows) ex. C:\Users\your_cpu_name\Pictures\
#2 - (macOS)   ex. INPUT_PIC_DIRECTORY = '/Users/'+USER_ID+'/Pictures/' or '/Users/yourusername/Pictures/'
#2 - (Windows) ex. INPUT_PIC_DIRECTORY = "C:\Users\"+USER_ID+"\Pictures\" or "C:\Users\yourusername\Pictures\"

#4 - (macOS)   ex. /Users/your_cpu_name/Documents/ImageMetadata_final.csv
#4 - (Windows) ex. C:\Users\your_cpu_name\Documents\ImageMetadata_final.csv
#4 - (Windows) ex. INPUT_PIC_DIRECTORY = "C:\Users\"+USER_ID+"\Pictures\ImageMetadata_final.csv"
#4 - (macOS)   ex. INPUT_PIC_DIRECTORY = '/Users/'+USER_ID+'/Pictures/ImageMetadata_final.csv'

#6 - (macOS)   ex. /Users/yourusername/Documents/ImageMetadata_raw.csv
#6 - (Windows) ex. C:\Users\yourusername\Documents\ImageMetadata_raw.csv        
#6 - (macOS)   ex. RAW_METADATA_FILE = "/Users/"+USER_ID+"/Pictures/ImageMetadata_raw.csv"
#6 - (Windows) ex. RAW_METADATA_FILE = "C:\Users\"+USER_ID+"\Pictures\ImageMetadata_raw.csv"
 

#%% USER DEFINED VARIABLES - SEE DOCUMENTATION
########################### EDIT THESE AS NECESSARY ###################################################
import getpass, sys, os
from pathlib import Path
from src.get_image_data import getImageData


def user_variables():
    USER_ID = getpass.getuser()
    OS_SYSTEM = sys.platform
    
    ## TODO - 1. EXTRACT_PHOTO_METADATA
    EXTRACT_PHOTO_METADATA = True
    
    ## TODO - 2. INPUT_PIC_DIRECTORY
    # FOR APPLE-OS X USERS
    if OS_SYSTEM == "darwin":  #APPLE- MAC
        INPUT_PIC_DIRECTORY = Path("/","Users", USER_ID, "Pictures")  #macos
        
    # FOR WINDOWS USERS
    elif OS_SYSTEM == "win32": #MICROSOFT - WINDOWS
        INPUT_PIC_DIRECTORY = Path( "C:", "Users", USER_ID,"Pictures")  #windows
        
    # FOR LINUX USERS   
    else: #linux,?
        print("You have not provided an accurate path to the INPUT_PIC_DIRECTORY.  If you are a linux user please set this yourself on line 60." )
        sys.exit(0)
        
    
    ## TODO - 3. POST_FILENAME
    POST_FILENAME = "ImageMetadata_final.csv" 
    
    
    ## TODO - 4. POST_PROCESSED_DATA
    POST_PROCESSED_DATA = os.path.join(INPUT_PIC_DIRECTORY, POST_FILENAME)
    
    
    ## TODO - 5. RAW_METADATA_FILE
    RAW_FILE = "ImageMetadata_raw.csv"
        
        
    # DO YOU ALREADY HAVE THE PHOTO METADATA? (include Path and filename)
    if EXTRACT_PHOTO_METADATA == False:
        
        # DOESN'T MATTER... SET IT TO WHAT YOU USED
        DO_RECURSIVE = True

        ## TODO - 6. NAME FILE AND PATH TO THE FILE, IF YOU ALREADY HAVE ONE 
        # FOR APPLE-OS X USERS
        if OS_SYSTEM == "darwin": # APPLE - OS X
            RAW_METADATA_FILE = Path("/","Users", USER_ID, "Pictures", RAW_FILE)  #macos
        
        # FOR WINDOWS USERS
        elif OS_SYSTEM == "win32": # MICROSOFT - WINDOWS
            RAW_METADATA_FILE = Path( "C:", "Users", USER_ID, "Pictures", RAW_FILE)  #windows
        
        # FOR LINUX USERS       
        else: # Linux,?
            print("You have not provided an accurate path to the raw photo metadata.\nIf you have not retrieved the data, set EXTRACT_PHOTO_METADATA to True." )
            sys.exit(0)
    
    else:
        #True is the default and searches folders and subfolders. False only searches the immediate folder.
        ## TODO 7: DO_RECURSIVE
        DO_RECURSIVE = True
        
        # GET METADATA IF NEEDED   -  DO NOT TOUCH  - SAVES FILE TO PICTURE DIRECTORY
        RAW_METADATA_FILE = getImageData(INPUT_PIC_DIRECTORY,RAW_FILE,recursive=DO_RECURSIVE) 
    
    
    ## TODO - 8. REMOVE_PHOTOS_TAKEN_BY_PLANE
    REMOVE_PHOTOS_TAKEN_BY_PLANE = False        # Quality Control 1: Remove Photos - Speed & Altitude
    
    
    ## TODO - 9. ONLY_MY_DEVICES
    ONLY_MY_DEVICES = False                     # Quality Control 2: Remove Photos - By Device
    
    
    ## TODO - 10. MY_DEVICES (if ONLY_MY_DEVICES is True)
    MY_DEVICES = []
    
    ## TODO - 11. MAPIT
    MAPIT = True
    
    ## TODO - 12. PLOT_PATH (ONLY IF YOU ARE PLOTTING WITH THE SAMPLE SCRIPT - WORLD VIEW)
    PLOT_FILE_NAME = 'sample_plot_pictures.jpg'
    PLOT_PATH = os.path.join(INPUT_PIC_DIRECTORY, PLOT_FILE_NAME)
    
    ## TODO - 13. REVERSE GEOCODE
    REVERSE_GEOCODE = False # THIS IS LIMITED TO 100 PHOTOS. Use knowing what is involved. Better geocoders can  be paid and implemented.
    
    
    ##################### DO NOT TOUCH BELOW #####################
    # dictionary with mixed keys
    user_vars = {'EXTRACT_PHOTO_METADATA' : EXTRACT_PHOTO_METADATA, 'INPUT_PIC_DIRECTORY' : INPUT_PIC_DIRECTORY, 'POST_FILENAME' : POST_FILENAME,\
               'POST_PROCESSED_DATA' : POST_PROCESSED_DATA, 'RAW_FILE' : RAW_FILE, 'RAW_METADATA_FILE' : RAW_METADATA_FILE,\
               'REMOVE_PHOTOS_TAKEN_BY_PLANE':REMOVE_PHOTOS_TAKEN_BY_PLANE,'ONLY_MY_DEVICES':ONLY_MY_DEVICES,'MY_DEVICES':MY_DEVICES,\
               'PLOT_PATH':PLOT_PATH,'MAPIT':MAPIT,'REVERSE_GEOCODE':REVERSE_GEOCODE,'DO_RECURSIVE':DO_RECURSIVE}
    
    return user_vars