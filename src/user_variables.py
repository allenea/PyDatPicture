#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:06:18 2019

@author: ericallen

This class contains all the variables that are required by the program to take
advantage of all it's capabilities. These can be changed by the user in main.py.

Default settings are set here. Do not modify the code in here.
"""
import os
from pathlib import Path
import getpass
import sys

class USER_DEFINED_VARIABLES(object):
    
    def __init__(self,
                 INPUT_PIC_DIRECTORY="",
                 OUTPUT_DIRECTORY="",
                 RAW_FILE="ImageMetadata_raw.csv",
                 POST_FILE="ImageMetadata_final.csv",
                 GEOCODE_FILE="ImageMetadata_geocode.csv",
                 OUTLIERS_FILE="ImageMetadata_remove_outliers.csv",
                 EXTRACT_PHOTO_METADATA=True,
                 SELECT_DEVICES=False,
                 DEVICES=[],
                 REMOVE_PHOTOS_TAKEN_BY_PLANE=True,
                 DO_RECURSIVE=True,
                 DETECT_OUTLIERS=True,
                 PERCENTILE="99th",
                 REVERSE_GEOCODE=False,
                 MAPIT=True,
                 MY_MAP=False):

        USER_ID = getpass.getuser()
        OS_SYSTEM = sys.platform
        
        #WHERE ARE THE PICTURES?
        if INPUT_PIC_DIRECTORY == "":
            if OS_SYSTEM == "darwin":
                self.INPUT_PIC_DIRECTORY = str(Path("/","Users",\
                                                    USER_ID, "Pictures"))
                
            # FOR MICROSOFT - WINDOWS USERS
            elif OS_SYSTEM == "win32" or OS_SYSTEM == "cygwin":
                self.INPUT_PIC_DIRECTORY = str(Path( "C:","/", "Users",\
                                                    USER_ID,"Pictures"))
                
            # FOR LINUX USERS   
            else: 
                print("Linux User? You must provide an accurate path to the ",\
                      "INPUT_PIC_DIRECTORY.");
                sys.exit(0)
        else:
            self.INPUT_PIC_DIRECTORY=INPUT_PIC_DIRECTORY
            
        #Output path.. try to keep all the outputs together - by default
        if OUTPUT_DIRECTORY =="":
            self.OUTPUT_DIRECTORY = os.path.abspath("../Output")
        else:
            self.OUTPUT_DIRECTORY = OUTPUT_DIRECTORY  ## Run directory?
        
        #File Names
        self.RAW_FILE = RAW_FILE
        self.POST_FILE = POST_FILE
        self.GEOCODE_FILE = GEOCODE_FILE
        self.OUTLIERS_FILE = OUTLIERS_FILE
        
        #Booleans and associated QC
        self.EXTRACT_PHOTO_METADATA = EXTRACT_PHOTO_METADATA
        self.SELECT_DEVICES = SELECT_DEVICES
        self.DEVICES = DEVICES
        self.REMOVE_PHOTOS_TAKEN_BY_PLANE = REMOVE_PHOTOS_TAKEN_BY_PLANE
        self.DO_RECURSIVE = DO_RECURSIVE
        self.DETECT_OUTLIARS = DETECT_OUTLIARS
        self.PERCENTILE = PERCENTILE

        self.REVERSE_GEOCODE = REVERSE_GEOCODE
        
        self.MAPIT = MAPIT
        self.MY_MAP = MY_MAP
        self.MAP_DATA_FILE="ImageMetadata_final.csv"
        self._MAPPING_FILE="my_pyDatPicture_mapping"
        self.MAPPING_PROGRAM=os.path.abspath("../")
    
        #Partial Paths
        self.PROCESSED_DATA = os.path.join(self.OUTPUT_DIRECTORY,'Data')
        
        self.PLOT_PATH = os.path.join(self.OUTPUT_DIRECTORY,'Figures')
        
        self.MAP_DATA_PATH=self.PROCESSED_DATA

        #Full Paths
        self.RAW_METADATA_FILE = os.path.join(self.PROCESSED_DATA,\
                                              self.RAW_FILE)
        
        self.GEOCODE_METADATA_FILE = os.path.join(self.PROCESSED_DATA,\
                                                  self.GEOCODE_FILE)

        self.OUTLIAR_QC_METADATA_FILE = os.path.join(self.PROCESSED_DATA,\
                                                     self.OUTLIARS_FILE)

        self.POST_PROCESSED_DATA = os.path.join(self.PROCESSED_DATA,\
                                                self.POST_FILE)
        
        #Dictionary of Variables... Used by the other programs
        self._user_vars = {'EXTRACT_PHOTO_METADATA':self.EXTRACT_PHOTO_METADATA,\
               'INPUT_PIC_DIRECTORY':self.INPUT_PIC_DIRECTORY,\
               'POST_FILE':self.POST_FILE,\
               'POST_PROCESSED_DATA':self.POST_PROCESSED_DATA,\
               'RAW_FILE':self.RAW_FILE,\
               'RAW_METADATA_FILE':self.RAW_METADATA_FILE,\
               'REMOVE_PHOTOS_TAKEN_BY_PLANE':self.REMOVE_PHOTOS_TAKEN_BY_PLANE,\
               'SELECT_DEVICES':self.SELECT_DEVICES,'DEVICES':self.DEVICES,\
               'REVERSE_GEOCODE':self.REVERSE_GEOCODE,\
               'DO_RECURSIVE':self.DO_RECURSIVE,\
               'DETECT_OUTLIARS':self.DETECT_OUTLIARS,\
               'PERCENTILE':self.PERCENTILE,\
               'PROCESSED_DATA':self.PROCESSED_DATA,\
               'OUTPUT_DIRECTORY':self.OUTPUT_DIRECTORY,\
               'GEOCODE_FILE':self.GEOCODE_FILE,\
               'GEOCODE_METADATA_FILE':self.GEOCODE_METADATA_FILE,\
               'OUTLIERS_FILE':self.OUTLIERS_FILE,\
               'OUTLIER_QC_METADATA_FILE':self.OUTLIER_QC_METADATA_FILE,\
               'PLOT_PATH':self.PLOT_PATH,'MAPIT':self.MAPIT,\
               'MY_MAP':self.MY_MAP, 'MAP_DATA_FILE':self.MAP_DATA_FILE,\
               'MAPPING_FILE':self._MAPPING_FILE,\
               'MAPPING_PROGRAM':self.MAPPING_PROGRAM,\
               'MAP_DATA_PATH':self.MAP_DATA_PATH}

        
        USER_DEFINED_VARIABLES.get_default_data(self)
    
    def get_default_data(self):
        return self._user_vars 


    def status_variables(cls):
        """ CALL/SET BEFORE PASSING TO MAIN"""
        
        # IF DOES NOT EXIST... Make to save the outputs
        if not os.path.exists(cls.OUTPUT_DIRECTORY):
            os.makedirs(cls.OUTPUT_DIRECTORY)    
            
        if not os.path.exists(cls.PROCESSED_DATA):
            os.makedirs(cls.PROCESSED_DATA) 
            
        if not os.path.exists(cls.PLOT_PATH):
            os.makedirs(cls.PLOT_PATH)    
            
    
        cls.MAP_DATA_PATH = os.path.join(cls.MAP_DATA_PATH, cls.MAP_DATA_FILE)
        
        #Make sure the path to the data exists
        if cls.MY_MAP == True:
            if os.path.exists(cls.MAP_DATA_PATH):
                pass
            else:
                print("PLOT DATA SOURCE: ", cls.MAP_DATA_PATH)
                print("NO FILE CAN BE FOUND AT THE PATH ABOVE. SWITCHING MY_MAP TO FALSE")
                print()
                
                cls.MY_MAP = False
                        
        cls.MAPPING_FILE = "my_pyDatPicture_mapping"
        
        
        cls.user_vars = {'EXTRACT_PHOTO_METADATA':cls.EXTRACT_PHOTO_METADATA,\
               'INPUT_PIC_DIRECTORY':cls.INPUT_PIC_DIRECTORY,\
               'POST_FILE':cls.POST_FILE,\
               'POST_PROCESSED_DATA':cls.POST_PROCESSED_DATA,\
               'RAW_FILE':cls.RAW_FILE,\
               'RAW_METADATA_FILE':cls.RAW_METADATA_FILE,\
               'REMOVE_PHOTOS_TAKEN_BY_PLANE':cls.REMOVE_PHOTOS_TAKEN_BY_PLANE,\
               'SELECT_DEVICES':cls.SELECT_DEVICES,\
               'DEVICES':cls.DEVICES,\
               'REVERSE_GEOCODE':cls.REVERSE_GEOCODE,\
               'DO_RECURSIVE':cls.DO_RECURSIVE,\
               'DETECT_OUTLIERS':cls.DETECT_OUTLIERS,\
               'PERCENTILE':cls.PERCENTILE,\
               'PROCESSED_DATA':cls.PROCESSED_DATA,\
               'OUTPUT_DIRECTORY':cls.OUTPUT_DIRECTORY,\
               'GEOCODE_FILE':cls.GEOCODE_FILE,\
               'GEOCODE_METADATA_FILE':cls.GEOCODE_METADATA_FILE,\
               'OUTLIERS_FILE':cls.OUTLIERS_FILE,\
               'OUTLIER_QC_METADATA_FILE':cls.OUTLIER_QC_METADATA_FILE,\
               'PLOT_PATH':cls.PLOT_PATH,'MAPIT':cls.MAPIT,\
               'MY_MAP':cls.MY_MAP, 'MAP_DATA_FILE':cls.MAP_DATA_FILE,\
               'MAPPING_FILE':cls._MAPPING_FILE,\
               'MAPPING_PROGRAM':cls.MAPPING_PROGRAM,\
               'MAP_DATA_PATH':cls.MAP_DATA_PATH}
        
        return cls.user_vars