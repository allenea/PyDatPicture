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
        - Pinpoint Accuracy is questionable... might break the program

"""
#%% LOAD SOFTWARE
def main():
    from src.pDP_Setup import setup_pyDatPicture
    import sys
    
    isSetUp = setup_pyDatPicture()
    
    if isSetUp == False:
        print("ERROR: THE REQUIRED SOFTWARE IS NOT INSTALLED ON YOUR MACHINE.\nFollow pyDatPicture documentation to proceed.")
        sys.exit(0)
    else:
        import getpass
        from USER_DEFINED_VARIABLES import user_variables
        from src.print_run_info import print_info
        import src.pyDatPicture as pyDat
        from src.map_it import map_data
        from src.reverse_geocode import reverse_geocode
    
    # Get Systems Info
    USER_ID = getpass.getuser()
    OS_SYSTEM = sys.platform
    
    # Get the user defined variables
    usr_vars = user_variables()
    
    # Print User Defined Variables
    print_info(usr_vars, isSetUp,USER_ID,OS_SYSTEM)
    
    # Process the data with quality control routines to give you a csv file with a list of time,longitude,latitude 
    data = pyDat.pyDatPicture(usr_vars)
    
    if usr_vars['REVERSE_GEOCODE'] == True:
        # LIMITED TO 100 GEOCODES... Use on specific and limited pictures 
        reverse_geocode(usr_vars)

    if usr_vars['MAPIT'] == True:
        # Python Mapping of Data
        map_data(data['Longitude'],data['Latitude'],usr_vars['PLOT_PATH'])
    
    print("\n\npyDatPicture Complete")
    
    
    
    
# Execute main() function
if __name__ == '__main__':
    main()