# pyDatPicture
By Eric Allen
Last Modified: 4 May 2019 at 3:30PM EDT

##Travel Much? Use your pictures to figure out where you've been.
This is a python program written to extract metadata from images on your computer and process that data into a csv file with time, latitude, and longitude. The output can be mapped in GIS or Python.

## The User only needs to modify the USER_DEFINED_VARIABLES.py file. More often than not the default settings will not need to be changed.
- Compatible with Windows and OS X systems. Unknown for Linux. 
    - For windows users it is assumed that you are on the C: drive.
    - For OS X users it is assumed that you are on the /Users/ directory.
- Default settings are for a recursive search of the default Pictures folder location.
- Depending on the number of photos you have the initial gathering of photo data could take a few minutes to a few hours.


##FILE STRUCTURE:

<B>pyDatPicture</B>

    - <B>main.py</B> This is the program that you run after you have made the necessary changes in USER_DEFINED_VARIABLES.py. The other files should not need to be touched (outside of USER_DEFINED_VARIABLES).
    
    - <B>USER_DEFINED_VARIABLES.py</B> Contains the 10 variables that may need to be changed according to your computer and how you want to search and get the data. Contains instructions and examples.


    <B>src
        - <B>wget.py</B> is a unlicensed program that supports in the downloading of the EXIFTOOL software in the event you haven't downloaded/installed it. This does not actually install the program. Instead it puts it on your desktop.
    
        - <B>pDP_Setup.py</B> will check to make sure you have the necessary software installed. If you are using Anaconda and are missing software, then pDP_Setup will assist in the installation process. Otherwise, you'll need to follow the instructions in the documentation.
    
        - <B>print_run_info.py</B> will print the results of the USER_DEFINED_VARIABLES and some systems information.
    
        - <B>get_image_data.py</B> will retrieve the data from your media located under the path that is set. Default location is the pictures folder for your computer user account. The output file by default is ImageMetadata_raw.csv but this can be changed in this file. The default option is "-r" or recursive to search the entire folder and it's subfolders. To not search the subfolders set recursive=False in the function call in pyDatPicture.py. Add additional variables at your own risk following Phil Harvey's documentation. The -common option could be added after -ee, and uncommenting the commented variables in pyDatPicture.py. 
    
        - <B>pyDatPicture.py</B> uses the extracted geolocation data from photos and cleans the data, returning a second csv with Time, Longitude, and Latitude for all photos that have geographic information.
    
        - <B>get_lat_lon.py</B> will parse the latitude and longitude strings which are in DMS format and return a float (in decimal degrees) adjusted by reference value.
    
        - <B>reformat_time.py</B> will reformat the date and time string to become YYYY-mm-dd HH:MM:SS
    
        - <B>reverse_geocode.py</B> will work in a limited capacity up to 100 photos/data points. This takes latitude and longitude and gives you an address for that location. Saves in an output file. This may or may not crash the program depending on the API - Nominatim. I recommend not using it unless absolutely necessary, if you do use it try to limit it to a handful of pictures.
    
        - <B>map_it.py</B> is starter code for mapping your data in python. See the Cartopy online documentation.
        

    <B>Sample_Figures
    
        - <B>testplot_pictures.JPG</B> is the sample cartopy world view figure
        
        - <B>Europe_Sample.JPG</B> is the European view ArcGIS Pro created figure
        
        - <B>sample1.JPG</B> is a quick 6-pannel city view ArcGIS Pro created figure
        
        - <B>sample2.JPG</B> is a quick 6-pannel city view ArcGIS Pro created figure
        
        - <B>sample3.JPG</B> is a quick 6-pannel city view ArcGIS Pro created figure
        
        
    <B>Documentation
    
        - <B>meta.yaml</B> I started trying to figure out how to host this code on Anaconda to do a conda install pyDatPicture (not working yet).
        
        - <B>WGET_README.md</B> is the README file for the wget program that was used.
        
        - <B>PyDatPicture.ipynb</B> is the original documentation for the code