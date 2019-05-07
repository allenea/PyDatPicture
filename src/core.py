#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 13:02:02 2019

@author: Eric Allen
Last Modified: 7 May 2019 at 12:30PM

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

4.OUTLIAR_QC_METADATA_FILE (This is a really neat feature that uses spatial
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
