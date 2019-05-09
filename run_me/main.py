#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 19:17:02 2019

@author: Eric Allen
Last Modified: 8 May 2019 3:50PM

You are free to modify this code under the GNU General Public License v3.0
<See license contained in the PyDatPicture repository/folder for more info>


NOT FOR COMMERCIAL-USE WITHOUT WRITTEN CONSENT FROM THE AUTHOR
THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHOR(S) BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION 
WITH THE SOFTWARE OR THE DEALINGS OF THE SOFTWARE.


BEFORE YOU BEGIN:
    - Download/Install Anaconda 3 (PYTHON 3)
        Use Spyder for programming. 
            - Install the required libraries from the documentation.
            - This program might be able to install the necessary conda
                libraries but it's untested.
    - Download/Install EXIFTOOLS - Phil Harvey
    
    - set user variables in your main file that calls the this file as needed: 
        Often times the default should suffice.
    - No other changes should be required in the code.
    
TO RUN:
    python main.py           from the command line
    Click the Green "Play" button in Anaconda/Spyder


This program extracts geolocation data from photos. That file can be processed
to quality control your data to weed out pictures that you might not have taken 
but for some reason have... This will most accurately show where you've been in
the world. You have an opportunity to save files at every point

## OUTPUT FILES

1. RAW_METADATA_FILE (what is extracted from your photos by exiftools)

2. POST_PROCESSED_DATA (what is returned from the pyDatPicture file only
                        accounting for REMOVE_PHOTOS_TAKEN_BY_PLANE or by
                        the DEVICE that took the picture if SELECT_DEVICES is
                        turned on. The Date, Time, Latitude, and Longitude is
                        corrected for the reference (N/S, E/W) and saved as
                        a numeric number. Date/Time is reformatted.)

3.GEOCODE_METADATA_FILE (Is the data (not to exceed 100 without modifying the
                         code, should only be done if you have a paid API.) that
                         is returned after using latitude and longitude to get
                         a physical address of the locations from your 
                         POST_PROCESSED_DATA file. It is recommended that you
                         create a folder with select photos not to exceed 100
                         and run this program on that set of data. The API will
                         kick you off with too many calls).

4.OUTLIER_QC_METADATA_FILE (This is a really neat feature that uses spatial
                            analysis and statistics to figure out and predict
                            pictures that were taken at places you may/may not
                            have visisted before. Maybe you downloaded a picture
                            off the internet or a friend sent you a picture from
                            their trip to somewhere you haven't been. If this
                            happens, the address is show and then the PROGRAM
                            ALLOWS YOU TO DECIDE IF THE PICTURE'S LOCATION
                            WILL BE INCLUDED IN THE FINAL OUTPUT by typing
                            yes (delete/remove) or no (keep) into the
                            command line/console when prompted. This is the last
                            step in the program once it's about ~99% finished)).

*** THESE 4 files are returnedas CSV files with a header row including the
    following headers 

5. Output/Figures/ (Includes pictures created with either the template mapping
                    program or if you modify the the mapping program, your maps.
                    You have the opportunity to change where the program is
                    looking for the data to be mapped and where the have your
                    mapping routines(code) saved. These are not set by default
                    and must be done in the main.py by changing the class variable
                    value, from where you are running the code.)


OUTPUT (CSV FILE):
    Date_Time - (str) YYYY-mm-dd HH:MM:SS (Depends on device time at photo)
    Latitude - (float) Decimal Degrees (Negative values are South)
    Longitude - (float) Decimal Degrees (Negative values are West)
    * Address -   OPTIONAL IN A LIMITED CAPACITY-Free (str) 
                    Reverse geocoded address (OR WITH PAID API)

In this file between the rows of ############
    make any changes to configure for your data otherwise default settings will
    be used... Follow along with console output for more information. 
"""
import sys
import getpass
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import src.user_variables as uv
from src.print_run_info import print_info
from src.core import main

def set_user_vars():
    
    # Get Systems Info
    USER_ID = getpass.getuser()
    OS_SYSTEM = sys.platform

    my_run = uv.USER_DEFINED_VARIABLES()
    
    #DEFAULT VARIABLES
    my_run.get_default_data()
    
###################### EDIT BETWEEN HERE TO CHANGE VARIABLES ##################
    
    """EXTRACT_PHOTO_METADATA
    Default: True   -> Get Data
    Alternative: False -> Use an existing datafile created by PyDatPicture
    """
    my_run.EXTRACT_PHOTO_METADATA = True
    
    
    """INPUT_PIC_DIRECTORY
    Default: Pictures directory/folder for Windows and Mac users
                 (/Users/username/Pictures/)
                 
                 getpass.getuser() -> your computer account login username
                 
                 You can also just put the root directory for your machine and
                 it will just search everything, but that takes more time.
    """
    #my_run.INPUT_PIC_DIRECTORY = "/Users/"+getpass.getuser()+"/Desktop/TEST/"
    
    
    """OUTPUT_DIRECTORY
    Where the output data (figures and data) will be saved
    
    Default: os.path.abspath("../Output")  -> ./PyDatPicture/Output/
    """
    my_run.OUTPUT_DIRECTORY = os.path.abspath("../Output")
    
    
    """RAW_FILE (see above)
    #1. Text Data extracted from EXIFTOOL

    Default: "ImageMetadata_raw.csv"
    """
    #my_run.RAW_FILE = "test_ImageMetadataRaw.csv"
    
    """POST_FILE (see above)
    #2. Text Data -> Numerical Data

    Default: "ImageMetadata_final.csv"
    """
    #my_run.POST_FILE = "test_ImageMetadata_final.csv"
    
    
    """GEOCODE_FILE (see above)
    #3. Numerical Data With Address Associated With the Coordinates

    Default: "ImageMetadata_geocode.csv"
    """
    #my_run.GEOCODE_FILE = "test_ImageMetadata_geocode.csv"
    
    
    """OUTLIERS_FILE (see above)
    #4. Numerical Data after all Quality Control

    Default: "ImageMetadata_remove_outliers.csv"
    """
    #my_run.OUTLIERS_FILE = "test_ImageMetadata_remove_outliers.csv"
    
    
    """DETECT_OUTLIERS
    Will also use PERCENTILE to determine what is an outlier.
    
    Default: True  -> Use spatial analysis to predict places you haven't been 
                        (if any) from the data and allow you to decide what to use
                        
    Alternative: False -> Use whatever data is there
    """
    #my_run.DETECT_OUTLIERS = False
    
    
    """PERCENTILE
    Default: "99th" (as type string) -> Detect outside of the 99th percentile
    
    Preset Options = 1st, 2.5th, 5th, 10th, 25th, 50th, 75th, 90th, 95th, 
                    97.5th, 99th
    """
    #my_run.PERCENTILE = "95th"
    
    
    """REMOVE_PHOTOS_TAKEN_BY_PLANE
    Default: True -> remove photos taken above 8000m or 
                      going faster than 75kmh and at above 1000m
                    
    Alternative: False -> Include all pictures regardless of altitude or speed
    """
    #my_run.REMOVE_PHOTOS_TAKEN_BY_PLANE = False
    
    
    """SELECT_DEVICES
    Default: False -> Use all devices
    Alternative: True -> Use selcted devices defined by DEVICES below
    """
    #my_run.SELECT_DEVICES = True
    
    
    """DEVICES
    Default: [] -> Empty List
    Alternative: -> List of strings with acceptable models 
    """
    #my_run.DEVICES = ["iPhone X"]
    
    
    """DO_RECURSIVE
    Default: True  -> Search All Folders and Subfolders
    Alternative: False -> Search ONLY the immediate directory 
    """
    #my_run.DO_RECURSIVE = False
    
    
    """REVERSE_GEOCODE 
    This is limited to the first 100 coordinates. Suggested you select certain
    pictures < 100 and then pass that raw data to PyDatPicture with this turned
    to True
    
    Default: False -> Do not reverse geocode
    Alternative: True -> Reverse geocode the data (not to exceed 100)
    """
    #my_run.REVERSE_GEOCODE = True
    
    
    """MAPIT
    Default: True -> Map the data
    Alternative: False -> Do not map any of the data
    """
    #my_run.MAPIT = False
    
    
    """MY_MAP
    #Default: False -> Use the default maps
    Alternative: True -> Provide your own mapping code in the
                    my_PyDatPicture_mapping.py program provided with your
                    either the current data or with prior data created by 
                    PyDatPicture
    """
    #my_run.MY_MAP = True
    
    
    """MAP_DATA_FILE
    You can specify with output PyDatPicture data file you want mapped.
    
                Here you should give the file name
                
    #Default: ImageMetadata_final.csv
    """
    #my_run.MAP_DATA_FILE = "ImageMetadata_final.csv"
    
    
    """MAP_DATA_PATH
    If MY_MAP is True then you have an opportunity to provide a separate source
        of data created by PyDatPicture. 
        
            Here you should give the path the the data file
            
    #Default: OUTPUT_DIRECTORY/Data/ Path
    """
    #my_run.MAP_DATA_PATH = "/Users/"+getpass.getuser()+"/Documents/GitHub/PyDatPicture/output/Data/"
    
    
    """MAPPING_PROGRAM
        If MY_MAP is True then you have an opportunity to provide your own 
        mapping/plotting code for PyDatPicture provided within the template
        my_pyDatPicture_mapping.
        
        Provide the path to the directory that holds my_pyDatPicture_mapping.py
        file
        
    #Default: The main PyDatPicture directory where the sample script is kept
    """
    #my_run.MAPPING_PROGRAM = os.path.abspath("../")
    
    
    """PLOT_PATH
    Where the output of the figures created by MAP_IT will be saved
    
    #Default: OUTPUT_DIRECTORY +'/Figures/'
    """
    my_run.PLOT_PATH = os.path.join(my_run.OUTPUT_DIRECTORY,"Figures")
    
    
    

    
    
    ## INCLUDE THESE IF YOU CHANGE THE OUTPUT_DIRECTORY
    """PROCESSED_DATA
    Default: OUTPUT_DIRECTORY +'/Data/'+ POST_FILE
    """
    my_run.PROCESSED_DATA = os.path.join(my_run.OUTPUT_DIRECTORY,"Data")
    

    """RAW_METADATA_FILE
    #1. Text Data extracted from EXIFTOOL
    
    
    Default: OUTPUT_DIRECTORY +'/Data/'+ RAW_FILE
    """
    my_run.RAW_METADATA_FILE = os.path.join(my_run.PROCESSED_DATA,\
                                            my_run.RAW_FILE)

    
    """POST_PROCESSED_DATA
    #2. Text Data -> Numerical Data
    
    Default: PROCESSED_DATA +'/Data/'+ POST_FILE
    """
    my_run.POST_PROCESSED_DATA = os.path.join(my_run.PROCESSED_DATA,\
                                              my_run.POST_FILE)

                                              
    """GEOCODE_METADATA_FILE
    #3. Numerical Data With Address Associated With the Coordinates
    
    Default: OUTPUT_DIRECTORY +'/Data/'+ GEOCODE_FILE
    """
    my_run.GEOCODE_METADATA_FILE = os.path.join(my_run.PROCESSED_DATA,\
                                                my_run.GEOCODE_FILE)
    
                                            
    
    """OUTLIER_QC_METADATA_FILE 
    #4. Numerical Data after all Quality Control
    
    Default: OUTPUT_DIRECTORY +'/Data/'+ OUTLIERS_FILE
    """
    my_run.OUTLIER_QC_METADATA_FILE = os.path.join(my_run.PROCESSED_DATA,\
                                                   my_run.OUTLIERS_FILE)
    
    
    
###############################################################################
###############################################################################
    
    
    
    
    
    #DO NOT EDIT BELOW
    
    
    #FINAL VARIABLES
    myvars = my_run.status_variables()

    print_info(myvars, isSetUp, USER_ID, OS_SYSTEM)
    
    return myvars


if __name__ == '__main__':
    
    from src.pDP_Setup import setup_pyDatPicture
    
    #Checks to make sure everything is installed
    isSetUp = setup_pyDatPicture()
    
    if isSetUp == False:
        print("ERROR: THE REQUIRED SOFTWARE IS NOT INSTALLED ON YOUR MACHINE.",\
              "\nFollow PyDatPicture documentation to proceed.")
        sys.exit(0)
    else:
        #Sets the variables
        myvars = set_user_vars()
    #Runs the program
    main(myvars)