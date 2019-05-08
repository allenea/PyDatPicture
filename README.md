# pyDatPicture
By Eric Allen
Last Modified: 8 May 2019 at 2:00AM EDT

# 1. Overview
## Travel Much? Use your pictures to figure out where you've been.
This is a python program written to extract geolocation metadata from the media files (images, videos, and audio) on your computer and process that data into a csv file with time, latitude, and longitude. The output can be mapped in GIS or Python. When you are traveling this is the best way to map and track your hyper-local movements. Your social media data provides little insight compared to your photos and videos.

This program was written with the intention of having the user program as little as possible. The only "code" the user should have to touch is the "main" file. There the user can change any of the default settings. In most cases that requires removing the #. Other cases will require you to add a file name or file path with " " on each side, to the right of the = sign. The output is very verbose so you can follow what is going on to identify where things are getting saved or where a problem might be occuring. The goal is to have you download the software and just run it.


# 2. Installation

## 2.1 Required Software
- EXIFTOOLS (REQUIRED: Phil Harvey: <https://sno.phy.queensu.ca/~phil/exiftool/>)
- Python 3 (REQUIRED: I HIGHLY RECOMMEND: Anaconda https://www.anaconda.com/distribution/#download-section)

	**WITH THE FOLLOWING PYTHON MODULES:**
	
	**Windows Users:** Use the Windows Anaconda Prompt and enter the code below to install the modules on Anaconda.
	
	**Apple Users:** Use Terminal and enter the code below to install the modules on Anaconda.
	
	- **numpy** (REQUIRED - Comes preinstalled on Anaconda <https://scipy.org/install.html>)
	- **pandas** (REQUIRED - Comes preinstalled on Anaconda <https://pandas.pydata.org/pandas-docs/stable/install.html>)
	- **matplotlib** (REQUIRED - Comes preinstalled on Anaconda: For map making: <https://scipy.org/install.html>)
	- **geopy** (REQUIRED: For geocoding: <https://geopy.readthedocs.io/en/stable/>)
	> conda install -c conda-forge geopy
	- **cartopy** (REQUIRED: For map making: <https://scitools.org.uk/cartopy/docs/latest/installing.html#installing>)
	> conda install -c conda-forge cartopy
	- **The pre-installed modules for everyone should include: dateutil, os, sys, getpass, pathlib, shutil, re**
	
	
If you are using anaconda, then there is a chance (fingers crossed) that any required missing software will be automatically installed. This has not been tested.


## 2.2 Compatiability & File Paths
- Compatible with Windows and OS X systems. Unknown for Linux. 
    - For windows users it is assumed that you are on the C: drive.
    - For OS X users it is assumed that you are on the /Users/ directory.
- Default settings are for a recursive search of the default Pictures folder location.
- Depending on the number of photos you have the initial gathering of photo data could take a few minutes to a few hours.
- You can always set the path to start looking recursively from your computers root/home directory. Not done by default.


## 2.3 Setting up your main.py file

**The user only needs to modify the main.py file, as needed. More often than not the default settings will not need to be changed. If the user wishes to include their own cartopy mapping routine, they can do so in the my_PyDatPicture_mapping.py template using the provided function definition.**

  
#### EXTRACT_PHOTO_METADATA
	Default: True -> Get Data
	Alternative: False -> Use an existing data file created by PyDatPicture
> my_run.EXTRACT_PHOTO_METADATA = True


#### INPUT_PIC_DIRECTORY
	Default: Pictures directory/folder for Windows and Mac users
             
	     (/Users/username/Pictures/)
	     
             getpass.getuser() -> your computer account login username
             
             You can also just put the root directory for your machine and
             it will just search everything, but that takes more time.
             
> my_run.INPUT_PIC_DIRECTORY = "/Users/"+getpass.getuser()+"/Desktop/"  # FOR MAC OS USER


#### OUTPUT_DIRECTORY
	Where the output data (figures and data) will be saved

	Default: os.path.abspath("../Output")  -> ./PyDatPicture/Output/

> my_run.OUTPUT_DIRECTORY = os.path.abspath("../Output")


#### RAW_FILE (see above)
	1. Text Data extracted from EXIFTOOL

	Default: "ImageMetadata_raw.csv"

> my_run.RAW_FILE = "test_ImageMetadataRaw.csv"


#### POST_FILE (see above)
	2. Text Data -> Numerical Data

	Default: "ImageMetadata_final.csv"

>my_run.POST_FILE = "test_ImageMetadata_final.csv"


#### GEOCODE_FILE (see above)
	3. Numerical data with the address associated with the coordinates.

	Default: "ImageMetadata_geocode.csv"

>my_run.GEOCODE_FILE = "test_ImageMetadata_geocode.csv"


#### OUTLIARS_FILE (see above)
	4. Numerical data after all the quality control steps

	Default: "ImageMetadata_remove_outliers.csv"

>my_run.OUTLIARS_FILE = "test_ImageMetadata_remove_outliers.csv"


#### DETECT_OUTLIARS
	Will also use PERCENTILE to determine what is an outliar.

	Default: True  -> Use spatial analysis to predict places you haven't been 
			    (if any) from the data and allow you to decide what to use

	Alternative: False -> Use whatever data is there

>my_run.DETECT_OUTLIARS = False


#### PERCENTILE
	Default: "99th" (as type string) -> Detect outside of the 99th percentile

	Preset Options = 1st, 2.5th, 5th, 10th, 25th, 50th, 75th, 90th, 95th, 
			97.5th, 99th

>my_run.PERCENTILE = "95th"


#### REMOVE_PHOTOS_TAKEN_BY_PLANE
	Default: True -> remove photos taken above 8000m or 
			  going faster than 75kmh and at above 1000m

	Alternative: False -> Include all pictures regardless of altitude or speed

>my_run.REMOVE_PHOTOS_TAKEN_BY_PLANE = False


#### SELECT_DEVICES
	Default: False -> Use all devices
	Alternative: True -> Use selcted devices defined by DEVICES below

>my_run.SELECT_DEVICES = True


#### DEVICES
	Default: [] -> Empty List
	Alternative: -> List of strings with acceptable models 

>my_run.DEVICES = ["iPhone X"]


#### DO_RECURSIVE
	Default: True  -> Search All Folders and Subfolders
	Alternative: False -> Search ONLY the immediate directory 

>my_run.DO_RECURSIVE = False


#### REVERSE_GEOCODE 
	This is limited to the first 100 coordinates. Suggested you select certain
	pictures < 100 and then pass that raw data to PyDatPicture with this turned
	to True

	Default: False -> Do not reverse geocode
	Alternative: True -> Reverse geocode the data (not to exceed 100)

>my_run.REVERSE_GEOCODE = True


#### MAPIT
	Default: True -> Map the data
	Alternative: False -> Do not map any of the data

>my_run.MAPIT = False


#### MY_MAP
	Default: False -> Use the default maps

	Alternative: True -> Provide your own mapping code in the
			my_PyDatPicture_mapping.py program provided with your
			either the current data or with prior data created by 
			PyDatPicture

>my_run.MY_MAP = True


#### MAP_DATA_FILE
	You can specify with output PyDatPicture data file you want mapped.

		Here you should give the file name

	Default: ImageMetadata_final.csv

>my_run.MAP_DATA_FILE = "ImageMetadata_final.csv"


#### MAP_DATA_PATH
	If MY_MAP is True then you have an opportunity to provide a separate source
	    of data created by PyDatPicture. 
    
        Here you should give the path the the data file
        
	Default: OUTPUT_DIRECTORY/Data/ Path

>my_run.MAP_DATA_PATH = "/Users/"+getpass.getuser()+"/Documents/GitHub/PyDatPicture/output/Data/"


#### MAPPING_PROGRAM
    If MY_MAP is True then you have an opportunity to provide your own 
    mapping/plotting code for PyDatPicture provided within the template
    my_pyDatPicture_mapping.
    
    Provide the path to the directory that holds my_pyDatPicture_mapping.py
    file
    
    Default: The main PyDatPicture directory where the sample script is kept

>my_run.MAPPING_PROGRAM = os.path.abspath("../")


#### PLOT_PATH
	Where the output of the figures created by MAP_IT will be saved

	Default: OUTPUT_DIRECTORY +'/Figures/'

>my_run.PLOT_PATH = os.path.join(my_run.OUTPUT_DIRECTORY,"Figures")




**INCLUDE THESE IF YOU CHANGED THE OUTPUT_DIRECTORY**


#### PROCESSED_DATA
	Default: OUTPUT_DIRECTORY +'/Data/'+ POST_FILE

> my_run.PROCESSED_DATA = os.path.join(my_run.OUTPUT_DIRECTORY,"Data")


#### RAW_METADATA_FILE
	1. Text Data extracted from EXIFTOOL

	Default: OUTPUT_DIRECTORY +'/Data/'+ RAW_FILE

> my_run.RAW_METADATA_FILE = os.path.join(my_run.PROCESSED_DATA, my_run.RAW_FILE)


#### POST_PROCESSED_DATA
	2. Text Data -> Numerical Data

	Default: PROCESSED_DATA +'/Data/'+ POST_FILE

> my_run.POST_PROCESSED_DATA = os.path.join(my_run.PROCESSED_DATA, my_run.POST_FILE)

                                          
#### GEOCODE_METADATA_FILE
	3. Numerical Data With Address Associated With the Coordinates

	Default: OUTPUT_DIRECTORY +'/Data/'+ GEOCODE_FILE

> my_run.GEOCODE_METADATA_FILE = os.path.join(my_run.PROCESSED_DATA, my_run.GEOCODE_FILE)

                                        

#### OUTLIAR_QC_METADATA_FILE 
	4. Numerical Data after all Quality Control

	Default: OUTPUT_DIRECTORY +'/Data/'+ OUTLIARS_FILE

> my_run.OUTLIAR_QC_METADATA_FILE = os.path.join(my_run.PROCESSED_DATA, my_run.OUTLIARS_FILE)





# 3. FILE STRUCTURE:

## 3.1 PyDatPicture Code

- **main.py** This is the program that you run after you have made the necessary changes in USER_DEFINED_VARIABLES.py. The other files should not need to be touched (outside of USER_DEFINED_VARIABLES).
- **USER_DEFINED_VARIABLES.py** Contains the 10 variables that may need to be changed according to your computer and how you want to search and get the data. Contains instructions and examples.

- **pyDatPicture/src**

	- **wget.py** is a unlicensed program that supports in the downloading of the EXIFTOOL software in the event you haven't downloaded/installed it. This does not actually install the program. Instead it puts it on your desktop.
	
	- **pDP_Setup.py** will check to make sure you have the necessary software installed. If you are using Anaconda and are missing software, then pDP_Setup will assist in the installation process. Otherwise, you'll need to follow the instructions in the documentation.
	
	- **print_run_info.py** will print the results of the USER_DEFINED_VARIABLES and some systems information.
	
	- **get_image_data.py** will retrieve the data from your media located under the path that is set. Default location is the pictures folder for your computer user account. The output file by default is ImageMetadata_raw.csv but this can be changed in this file. The default option is "-r" or recursive to search the entire folder and it's subfolders. To not search the subfolders set recursive=False in the function call in pyDatPicture.py. Add additional variables at your own risk following Phil Harvey's documentation. The -common option could be added after -ee, and uncommenting the commented variables in pyDatPicture.py. 
	
	- **pyDatPicture.py** uses the extracted geolocation data from photos and cleans the data, returning a second csv with Time, Longitude, and Latitude for all photos that have geographic information.
	
	- **get_lat_lon.py** will parse the latitude and longitude strings which are in DMS format and return a float (in decimal degrees) adjusted by reference value.
	
	- **reformat_time.py** will reformat the date and time string to become YYYY-mm-dd HH:MM:SS
	
	- **reverse_geocode.py** will work in a limited capacity up to 100 photos/data points. This takes latitude and longitude and gives you an address for that location. Saves in an output file. This may or may not crash the program depending on the API - Nominatim. I recommend not using it unless absolutely necessary, if you do use it try to limit it to a handful of pictures.
	
	- **map_it.py** is starter code for mapping your data in python. See the Cartopy online documentation.

- **pyDatPicture/Sample_Figures**
	- **testplot_pictures.JPG** is the sample cartopy world view figure
	
	- **Europe_Sample.JPG** is the European view ArcGIS Pro created figure
	
	- **sample1.JPG** is a quick 6-pannel city view ArcGIS Pro created figure
	
	- **sample2.JPG** is a quick 6-pannel city view ArcGIS Pro created figure
	
	- **sample3.JPG** is a quick 6-pannel city view ArcGIS Pro created figure

- **pyDatPicture/Documentation**
	- **meta.yaml** I started trying to figure out how to host this code on Anaconda to do a conda install pyDatPicture (not working yet).
	
	- **WGET_README.md** is the README file for the wget program that was used.
	
	- **PyDatPicture.ipynb** is the original documentation for the code
	
	
	
## 3.2 Output Files:

**FORMAT**
    - Date_Time - (str) YYYY-mm-dd HH:MM:SS (Depends on device time at photo)
    - Latitude - (float) Decimal Degrees (Negative values are South)
    - Longitude - (float) Decimal Degrees (Negative values are West)
    * Address -   OPTIONAL IN A LIMITED CAPACITY (str) 
                    Reverse geocoded address (OR WITH PAID API)
                    
                    
1. RAW_METADATA_FILE 
    - What is extracted from your photos by EXIFTOOLS. Text Data.

2. POST_PROCESSED_DATA 
    - What is returned from pyDatPicture.py, It only
        accounts for REMOVE_PHOTOS_TAKEN_BY_PLANE (Altitude above 8000m, 
        or speed greater than 75 km/hr and altitude above 1000m) or by
        the DEVICE that was used to take the picture, if SELECT_DEVICES is
        turned on. The Date, Time, Latitude, and Longitude is
        corrected for the reference (N/S, E/W) and saved as
        a numeric numbers. Date/Time is reformatted. Numerical Data.
        
3. GEOCODE_METADATA_FILE 
    - Data (not to exceed 100 coordinates without modifying the
         code, should only be done if you have a paid API...) that
         is saved in POST_PROCESSED_DATA file (numerical latitude 
         and longitude) is used to get a physical address of the
         locations the picture was taken. It is recommended that you
         create a folder with select photos not to exceed 100
         and run this program on that set of data. The API will
         kick you off with too many calls. I can't control that.
         Numerical Data.

4. OUTLIAR_QC_METADATA_FILE
    - This is a really neat feature that uses spatial
        analysis and statistics to figure out and predict
        pictures that were taken at places you may not
        have visisted before. Maybe you downloaded a picture
        off the internet or a friend sent you a picture from
        their trip to someplace you have not been. If this
        happens, the address is shown and then the CONSOLE
        ALLOWS YOU TO DECIDE IF THE PICTURE'S LOCATION
        SHOULD BE INCLUDED IN THE FINAL OUTPUT. This can be
        done by typing yes (remove) or no (keep) into the
        command line/console when prompted. This is the last
        step in the program, once it's about ~99% finished. 
        What happens here does not impact any of the other 
        results.

** These 4 files are returned as CSV files with a header row including the
    following headers  **

5. Output/Figures/
    - This folder includes figures created with either the template mapping
        program or if you modify the the mapping program, your maps.
        You have the opportunity to change where the program is
        looking for the data to be mapped and where the have your
        mapping routines(code) saved. These are not set by default
        and must be done in the main.py by changing the class variable
        value, from where you are running the code.
