# PyDatPicture
By Eric Allen
Last Modified: 9 May 2019 at 10:00AM EDT

# 1 Overview
## Travel Much? Use your pictures to figure out where you've been.
This is a python program written to extract geolocation metadata from the media files (image, video, and audio) on your computer and process that data into a csv (comma-separated) file with time, latitude, and longitude. The output can be mapped in GIS or Python. When you are traveling this is the best way to map and track your hyper-local movements. I originally thought that social media data might provide the most insight, but the truth is that it contributes little insight compared to your photos and videos. By default, social media strips your photos of geolocation data when you post them.

This program was written with the intention of having the user "program" as little as possible. The only "code" the user should have to touch is the "main" file and the my_pyDatPicture_mapping.py (if you would like to make your own map), which are located in the **run_me** directory. In the main.py file, the user can change any of the default settings. In most cases that requires removing the #. Other cases will require you to add a file name or file path with " " on each side, to the right of the = sign. The output is very verbose so you can follow what is going on to identify where things are getting saved or where a problem might be occuring. Then the mapping template is for users who which to code their own cartopy maps. The goal is to have you download the software and just run it. That's why everything is provided, including default templates that map over most of the world and robust quality control algorithms. This documentation should be able to provide answers to any questions. If questions persist open an Issue on Github. 


# 2 Installation

## 2.1 Required Software
- Download the PyDatPicture code from Github (<https://github.com/allenea/PyDatPicture>)
- EXIFTOOLS By Phil Harvey (REQUIRED: <https://sno.phy.queensu.ca/~phil/exiftool/>)
- Python 3 (REQUIRED: I highly recommend Anaconda https://www.anaconda.com/distribution/#download-section)

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
- **You will likely be required to grant Anaconda/Python Full Disk Access in settings to allow it to access your Photos in iPhotos** 
	- This is required in the EXIFTOOL portion of the code to extract metadata
	- Terminal by default has Full Disk Access (Apple users)
	- You will recieve a message in the console if it cannot access that directory. You will want this directory to be accessible.
	* <https://macpaw.com/how-to/full-disk-access-mojave>   
	
If you are using anaconda, then there is a chance, fingers crossed, that any required (missing) software will be automatically installed. This has not been tested. If not just follow these steps.


## 2.2 Compatiability & File Paths
- Compatible with Windows and OS X systems. Unknown for Linux (let me know?). 
    - For Windows users it is assumed that you are on your C: drive.
    - For OS X users it is assumed that you are on the /Users/ directory for your username.
- Default settings are for a recursive search of the default Pictures folder location.
- Depending on the number of photos you have the initial gathering of photo data could take a few minutes to a few hours.
- You can always set the path to start looking recursively from your computers root/home directory. Not done by default.

## 2.3 Setting up your main.py file

**The user only needs to modify the main.py file, as needed. More often than not the default settings will not need to be changed. If the user wishes to include their own cartopy mapping routine, they can do so in the my_PyDatPicture_mapping.py template using the provided function definition. All namelist options are in Section 3.**

 # 3 Namelist Options
 
#### 3.1 EXTRACT_PHOTO_METADATA
	Default: True -> Get Data
	
	Alternative: False -> Use an existing data file created by PyDatPicture. 
	
    	Set the filename in RAW_FILE and RAW_METADATA_FILE.
    	
> my_run.EXTRACT_PHOTO_METADATA = True


#### 3.2 INPUT_PIC_DIRECTORY
	Default: Pictures directory/folder for Windows and Mac users
           
		(/Users/username/Pictures/)
	     
             getpass.getuser() -> your computer account login username
             
    Alternative: Set to any location on your machine
    
             You can also just put the root directory for your machine and
             it will just search everything, but that takes more time.
             
> my_run.INPUT_PIC_DIRECTORY = "/Users/"+getpass.getuser()+"/Desktop/"  # FOR MAC OS USER


#### 3.3 OUTPUT_DIRECTORY
	Default: os.path.abspath("../Output")  -> ./PyDatPicture/Output/
	
    Alternative: Set to any location on your machine

	Where the output data (figures and data) will be saved

> my_run.OUTPUT_DIRECTORY = os.path.abspath("../Output")


#### 3.4 RAW_FILE (see above)
	Default: "ImageMetadata_raw.csv"
	
	Alternative: Any name in quotes (no spaces) ending with .csv
	
	1. Text Data extracted from EXIFTOOL

> my_run.RAW_FILE = "test_ImageMetadataRaw.csv"


#### 3.5 POST_FILE (see above)
	Default: "ImageMetadata_final.csv"
	
	Alternative: Any name in quotes (no spaces) ending with .csv

	2. Text Data -> Numerical Data

>my_run.POST_FILE = "test_ImageMetadata_final.csv"


#### 3.6 GEOCODE_FILE (see above)
	Default: "ImageMetadata_geocode.csv"
	
	Alternative: Any name in quotes (no spaces) ending with .csv

	3. Numerical data with the address associated with the coordinates.

>my_run.GEOCODE_FILE = "test_ImageMetadata_geocode.csv"


#### 3.7 OUTLIERS_FILE (see above)
	Default: "ImageMetadata_remove_outliers.csv"
	
	Alternative: Any name in quotes (no spaces) ending with .csv

	4. Numerical data after all the quality control steps

>my_run.OUTLIERS_FILE = "test_ImageMetadata_remove_outliers.csv"


#### 3.8 DETECT_OUTLIERS
	Default: True  -> Use spatial analysis to predict places you haven't been 
			    (if any) from the data and allow you to decide what to use

	Alternative: False -> Use whatever data is there
	
	Will also use PERCENTILE to determine what is an outlier.

>my_run.DETECT_OUTLIERS = False


#### 3.9 PERCENTILE
	Default: "99th" (as type string) -> Detect outside of the 99th percentile
	
    Alternative: Select any of the other preset percentile options enclosed in " "
    
	Preset Options = 1st, 2.5th, 5th, 10th, 25th, 50th, 75th, 90th, 95th, 
			97.5th, 99th

>my_run.PERCENTILE = "95th"


#### 3.10 REMOVE_PHOTOS_TAKEN_BY_PLANE
	Default: True -> remove photos taken above 8000m or 
			  going faster than 75kmh and at above 1000m

	Alternative: False -> Include all pictures regardless of altitude or speed

>my_run.REMOVE_PHOTOS_TAKEN_BY_PLANE = False


#### 3.11 SELECT_DEVICES
	Default: False -> Use all devices
	
	Alternative: True -> Use selcted devices defined by DEVICES below

>my_run.SELECT_DEVICES = True


#### 3.12 DEVICES
	Default: [] -> Empty List
	
	Alternative: -> List of strings with acceptable models 

>my_run.DEVICES = ["iPhone X"]


#### 3.13 DO_RECURSIVE
	Default: True  -> Search All Folders and Subfolders
	
	Alternative: False -> Search ONLY the immediate directory 

>my_run.DO_RECURSIVE = False


#### 3.14 REVERSE_GEOCODE 
	Default: False -> Do not reverse geocode
	
	Alternative: True -> Reverse geocode the data (not to exceed 100)

	This is limited to the first 100 coordinates. Suggested you select certain
	pictures < 100 and then pass that raw data to PyDatPicture with this turned
	to True

>my_run.REVERSE_GEOCODE = True


#### 3.15 MAPIT
	Default: True -> Map the data
	
	Alternative: False -> Do not map any of the data

>my_run.MAPIT = False


#### 3.16 MY_MAP
	Default: False -> Use the default maps

	Alternative: True -> Provide your own mapping code in the
			my_PyDatPicture_mapping.py program provided with your
			either the current data or with prior data created by 
			PyDatPicture

>my_run.MY_MAP = True


#### 3.17 MAP_DATA_FILE
	Default: ImageMetadata_final.csv

    Alternative: You can specify an output PyDatPicture data file you want mapped.

		Here you should give the file name

>my_run.MAP_DATA_FILE = "ImageMetadata_final.csv"


#### 3.18 MAP_DATA_PATH
	Default: OUTPUT_DIRECTORY/Data/ <- PATH

	If MY_MAP is True then you have an opportunity to provide a separate source
	    of data created by PyDatPicture. 
    
        Here you should give the path the the data file
        
>my_run.MAP_DATA_PATH = "/Users/"+getpass.getuser()+"/Documents/GitHub/PyDatPicture/output/Data/"


#### 3.19 MAPPING_PROGRAM
    Default: The run_me PyDatPicture directory where the sample script is kept

    If MY_MAP is True then you have an opportunity to provide your own 
    mapping/plotting code for PyDatPicture provided within the template
    my_pyDatPicture_mapping.
    
    Provide the path to the directory that holds my_pyDatPicture_mapping.py
    file

>my_run.MAPPING_PROGRAM = os.path.abspath("../run_me")


#### 3.20 PLOT_PATH
	Where the output of the figures created by MAP_IT will be saved

	Default: OUTPUT_DIRECTORY +'/Figures/'

>my_run.PLOT_PATH = os.path.join(my_run.OUTPUT_DIRECTORY,"Figures")


**INCLUDE THESE IF YOU CHANGED THE OUTPUT_DIRECTORY**


#### 3.21 PROCESSED_DATA
	Default: OUTPUT_DIRECTORY +'/Data/'+ POST_FILE

> my_run.PROCESSED_DATA = os.path.join(my_run.OUTPUT_DIRECTORY,"Data")


#### 3.22 RAW_METADATA_FILE
	Default: OUTPUT_DIRECTORY +'/Data/'+ RAW_FILE

	1. Text Data extracted from EXIFTOOL

> my_run.RAW_METADATA_FILE = os.path.join(my_run.PROCESSED_DATA, my_run.RAW_FILE)


#### 3.23 POST_PROCESSED_DATA
	Default: PROCESSED_DATA +'/Data/'+ POST_FILE

	2. Text Data -> Numerical Data

> my_run.POST_PROCESSED_DATA = os.path.join(my_run.PROCESSED_DATA, my_run.POST_FILE)

                                          
#### 3.24 GEOCODE_METADATA_FILE
	Default: OUTPUT_DIRECTORY +'/Data/'+ GEOCODE_FILE

	3. Numerical Data With Address Associated With the Coordinates

> my_run.GEOCODE_METADATA_FILE = os.path.join(my_run.PROCESSED_DATA, my_run.GEOCODE_FILE)

                                        

#### 3.25 OUTLIER_QC_METADATA_FILE 
	Default: OUTPUT_DIRECTORY +'/Data/'+ OUTLIERS_FILE

	4. Numerical Data after all Quality Control

> my_run.OUTLIER_QC_METADATA_FILE = os.path.join(my_run.PROCESSED_DATA, my_run.OUTLIERS_FILE)



# 4 FILE STRUCTURE:

## 4.1 PyDatPicture Code


- **pyDatPicture/run_me/**

    - **main.py** Is the main program that is actually executed. This file contains the user variables (namelist options) which the user can change if they do not want to use the default values. See section 3 for details.
    
    - **my_pyDatPicture_mapping.py** User modifiable custom-mapping routine.


- **pyDatPicture/src/**

    - **core.py** Is the core of the PyDatPicture algorithm that "turns the crank" on PyDatPicture. It helps facilitate everything.
    
    - **detectOutlier.py** Is a statistical analysis feature that identifies potential outliers and requests feedback from the user as to whether or not to include the data in the final output.
    
    - **get_image_data.py** Runs the exiftools command to extract the metadata and save it to a csv file which can then be processed by PyDatPicture.
    
    - **get_lat_lon.py** Parses the text string for latitude and longitude to calculate the decimal degree value from DMS then applies references for N/S and E/W.
        
    - **map_it.py**  Is the default mapping routine that is packaged with PyDatPicture
    
    - **pDP_Setup.py**  Checks to see if you have all the necessary software installed. If not it will hopefully help to install whatever isn’t there or point you towards what needs installed.
    
    - **print_run_info.py** Prints all the information about user variables and the run to the console/command line so you are able to traceback any potential issues. 
    
    - **pyDatPicture.py** Is the main processing algorithm that turns the text strings into numerical data that can then be analyzed and mapped.
    
    - **reformat_time.py** Reformats the date and time string into a more readable format.
    
    - **reverse_geocode.py** Takes geographic coordinates and reverse geocodes to obtain an physical address for that location.
    
    - **user_variables.py** is a class that contains all the user defined variables that can then be changed before being passed to the core program as a dictionary.
    
    - **wget.py** is a unlicensed program that supports in the downloading of the EXIFTOOL software in the event you haven't downloaded/installed it. This does not actually install the program. Instead it puts it on your desktop.
    
    - **__init__.py** is required to make Python treat directories containing the file as packages

- **pyDatPicture/Documentation/**

	- **WGET_README.md** is the README file for the wget program that was used.

	- **/Sample_Figures/**
	
		- **testplot_pictures.JPG** is the sample cartopy world view figure
		
		- **Europe_Sample.JPG** is the European view ArcGIS Pro created figure
	
		- **sample1.JPG** is a quick 6-pannel city view ArcGIS Pro created figure
	
		- **sample2.JPG** is a quick 6-pannel city view ArcGIS Pro created figure
	
		- **sample3.JPG** is a quick 6-pannel city view ArcGIS Pro created figure

		- **Africa.jpeg** is a continent view, sample template, of cartopys mapping capabilities.
	
		- **Asia.jpeg** is a continent view, sample template, of cartopys mapping capabilities.
	
		- **Australia.jpeg** is a continent view, sample template, of cartopys mapping capabilities.

		- **Europe.jpeg** is a continent view, sample template, of cartopys mapping capabilities.
	
		- **SouthAmerica.jpeg** is a continent view, sample template, of cartopys mapping capabilities.
	
		- **USA.jpeg** is a USA view, sample template, of cartopys mapping capabilities.

		- **World.jpeg** is a world view, sample template, of cartopys mapping capabilities.


- **pyDatPicture/conda_build/**
	- **meta.yaml** is NOT working, but a script to eventually build as an conda package. You don't need to do anything with this.

- **pyDatPicture/Output/**
	- **/Data/**  Comes empty but will hold the output data by default
	- **/Figures/**  Comes empty but will hold the output figures by default

- **pyDatPicture/tests/**
	- **test_all.py** Contains tests to make sure that the program is working as it should

- **README.md** Contains documentation and instructions for PyDatPicture

- **LICENSE** GNU GPLv3 License
	
	


## 4.2 Output Files & Figures:


#### 4.2.1 VARIABLES

- Date_Time - (str) YYYY-mm-dd HH:MM:SS (Depends on device time at photo. Time zone not recorded.)

- Latitude - (float) Decimal Degrees (Negative values are South)

- Longitude - (float) Decimal Degrees (Negative values are West)

* Address -   OPTIONAL IN A LIMITED CAPACITY (str)

	- Reverse geocoding the addresses with a PAID API will require a few modifications.
            
	    
	    
#### 4.2.2 FILES
                    
1. RAW_METADATA_FILE 
    - What is extracted from your photos by EXIFTOOLS. Text Data.

2. POST_PROCESSED_DATA 
    - What is returned from pyDatPicture.py, It only
        accounts for REMOVE_PHOTOS_TAKEN_BY_PLANE (Altitude above 8000m, 
        or speed greater than 75 km/hr and altitude above 1000m) or by
        the DEVICE that was used to take the picture, if SELECT_DEVICES is
        turned on. These can be set in the run_me file. 
        The Date-Time, Latitude, and Longitude is
        corrected for the reference (N/S, E/W) and saved as
        a numerical values. Date/Time is reformatted. Numerical Data.
        
3. GEOCODE_METADATA_FILE 
    - Data that is saved in POST_PROCESSED_DATA file (numerical latitude 
         and longitude) is used to get a physical address of the
         locations the picture was taken. It is recommended that you
         create a folder with select photos not to exceed 100
         and run this program on that set of data. The API will
         kick you off with too many calls. I can't control that.
         Numerical Data.
        * Not to exceed 100 coordinates without modifying the code, should only be done if you have a paid API...

4. OUTLIER_QC_METADATA_FILE
    - This is a really neat feature that uses spatial
        analysis and statistics to figure out and predict
        pictures that were taken at places you may not
        have visisted before. Maybe you downloaded a picture
        off the internet or a friend sent you a picture from
        their trip to some place you have never been. If this
        happens, the address is shown and then the CONSOLE
        ALLOWS YOU TO DECIDE IF THE PICTURE'S LOCATION
        SHOULD BE INCLUDED IN THE FINAL OUTPUT. This can be
        done by typing yes (remove) or no (keep) into the
        command line/console when prompted. This is the last
        step in the program, once it's about ~99% finished. 
        What happens here does not impact any of the other 
        results.

**These 4 files are returned as CSV files with a header row including the
    following headers**
    
#### 4.2.3 FIGURES

5. Output/Figures/
    - This folder includes figures created with either the template mapping
        program or if you modify the the mapping program, your maps.
        You have the opportunity to change where the program is
        looking for the data to be mapped and where the have your
        mapping routines(code) saved. These are not set by default
        and must be done in the main.py by changing the class variable
        value, from where you are running the code.


# 5 MAPPING

## 5.1 MAPPING IN GIS

First open your GIS software, create a project, and start a new map. My instructions will be through the POV of a ArcGIS Pro user. Go to Catalog -> Portal -> Living Atlas and select a background (i.e. World Imagery) or use the default topographic background. Then click the Map tab and select Add Data (under the layer section) -> XY Point Data. Select your file. The input table will be the csv file (quality controled or "final") depending on if you QC'd your data. The x field should be Longitude and the y field should be Latitude. Use the proper coordinate system, I selected GCS_WGS_1984. Then click run. Your data should appear. If your data appears only in one spot when there should be many points, then you are likely using the wrong projection. From there symbolize your data as you would like and create some nice maps in layout. This requires you to have output file that you want to map accessible by the ArcGIS software. More information for ArcGIS Pro or other GIS softare can be found online.


## 5.2 MAPPING IN PYTHON

To map your data in python turn MAP_IT on (True).

Mapping in python is a good alternative if you do not have access to GIS software like ArcGIS Pro. Cartopy is an amazing library that can make it happen. Cartopy allows you to add features like boarders, states, coastlines (at high or low resolution), and map data on top of the map.Cartopy supports many projections to map your data how you want. Just apply that projection while plotting your data (using transform = projection). See map_it.py for a template of how to map and zoom with set_extent. You can change the dot size, color, and shape for the geographic locations that photos are taken. Search for Cartopy documentation for more details of how to map with cartopy. 

Use the PLOT_PATH to direct PyDatPicture where it should save your figure files. By default it's in the ./Output/Figure/ PATH.

#### 5.2.1 MAPIT.py
	> map_data(longitude,latitude,usr_vars)
This is the default mapping program that I wrote in like two minutes covering what I believe are the major travel areas of the world. Obviously I am missing many regions. You can add them to this file or adjust these as you wish. This file takes in longitude, latitude, and the dictionary usr_vars as parameters.

By default, it will use the last data file to the extent your performed quality control on your data. This can be changed using the MAP_DATA_FILE and MAP_DATA_PATH variables as described above.

#### 5.2.2 my_pyDatPicture_mapping.py
	> map_data(usr_vars)
This is a file where you can create your own map with ANY PyDatPicture output file that contains latitude and longitude. This template was written so that you don't have to touch any of the src code. You need to switch MY_MAP to True and then you have the freedom to use the default data and just contribute your own mapping algorithm, and you can pass any PyDatPicture data output (new or old) just set the file name with MAP_DATA_FILE and then set the path to that file with MAP_DATA_PATH. DO NOT change the name of the my_pyDatPicture_mapping.py file or the function call. 

There should only be two files you need to touch. 

# 6 PRIVACY

I don't trust those online websites that say they'll what PyDatPicture does for you. First they just aren't simple to use and second I don't want to give some random website my pictures. Other tools to extract metadata from pictures aren't this simple to use or make it this easy to map the data. **But with PyDatPicture you control your data, who has access to it, and it's an easy tool to use.**

# 7 ACKNOWLEDGEMENTS

Please acknowledge Eric Allen and PyDatPicture in any work that is not for personal use. Not bad for a meteorologist who coded this in about a week and a half, eh? Spread the word about this program. Use #PyDatPicture in any social media posts where you are sharing maps of your travels.


**“Travel makes one modest. You see what a tiny place you occupy in the world.” -Gustav Flaubert**

**#LiveLoveLaughTravel - Kyri (tour guide w/ #EF)**
