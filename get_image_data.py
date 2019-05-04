#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 00:38:19 2019

@author: ericallen
"""
import os

def getImageData(input_dir,recursive=True):
    """
    This function retrieves the metadata and stores it in a csv file.
    
    INPUT:
        input_dir - (str) path to the input directory
    OUTPUT:
        output_file - (str) output filename ... This can be changed by the user but is set internally.
        
        ! A csv file containing the metadata for the photos - INTERNAL PROCESS
    """
    
    #This file stores the raw data from your picture (including location)
    output_file = 'ImageMetadata_raw' # SAVED IN RUN DIRECTORY... UNLESS YOU SPECIFY A PATH

    # Check to see if the user wants to search all files and sub-folders
    if recursive == True: r = "-r"
    else: r = ""
    
    if ".csv" in output_file:  print('Your Output File Is: ' + output_file)
    else:
        if "." in output_file: output_file = output_file.split(".")[0] + ".csv"
        else:   output_file = output_file + ".csv"
        print('Your New Output File Is: ' + output_file)
   
    print("\nSTORING THE FOLLOWING DATA: Source File, Model DateTimeOriginal, GPSDateStamp, GPSTimeStamp, "+
          "GPSLatitude, GPSLatitudeRef, GPSLongitude, GPSLongitudeRef, GPSAltitude, GPSAltitudeRef, "+
          "GPSSpeed, GPSSpeedRef, GPSTrack, GPSTrackRef, GPSImgDirection, GPSImgDirectionRef")
    
    print("\nSome Warnings/Errors are Okay\n")
    
    command = ["exiftool -csv "+r+ " -ee -SourceFile -Model "+\
              "-DateTimeOriginal -gps:GPSDateStamp -gps:GPSTimeStamp -gps:GPSLatitude "+\
              "-gps:GPSLatitudeRef -gps:GPSLongitude -gps:GPSLongitudeRef -gps:GPSAltitude "+\
              "-gps:GPSAltitudeRef -gps:GPSSpeed -gps:GPSSpeedRef -gps:GPSTrack -gps:GPSTrackRef "+\
              "-gps:GPSImgDirection -gps:GPSImgDirectionRef "+ input_dir+" > "+output_file]
    
    print(command[0],"\n")
    os.system(command[0])
    
    return output_file

