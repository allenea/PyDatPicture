#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:06:18 2019

@author: ericallen
"""
import os
from pathlib import Path
import getpass
import sys

class USER_DEFINED_VARIABLES(object):
    
    def __init__(self, INPUT_PIC_DIRECTORY="",OUTPUT_DIRECTORY="",\
                 RAW_FILE="ImageMetadata_raw.csv", POST_FILE="ImageMetadata_final.csv" ,\
                 EXTRACT_PHOTO_METADATA=True,SELECT_DEVICES=False,DEVICES=[],\
                 REMOVE_PHOTOS_TAKEN_BY_PLANE=True,DO_RECURSIVE=True,DETECT_OUTLIARS=True,\
                 PERCENTILE="99th",MAPIT=True,REVERSE_GEOCODE=False):
        
        USER_ID = getpass.getuser()
        OS_SYSTEM = sys.platform
        if INPUT_PIC_DIRECTORY == "":
            if OS_SYSTEM == "darwin":   self.INPUT_PIC_DIRECTORY = str(Path("/","Users", USER_ID, "Pictures"))
            # FOR MICROSOFT - WINDOWS USERS
            elif OS_SYSTEM == "win32":  self.INPUT_PIC_DIRECTORY = str(Path( "C:", "Users", USER_ID,"Pictures"))
            # FOR LINUX USERS   
            else: print("Linux Users? You must provide an accurate path to the INPUT_PIC_DIRECTORY."); sys.exit(0)
        else:
            self.INPUT_PIC_DIRECTORY=INPUT_PIC_DIRECTORY
            
        
        if OUTPUT_DIRECTORY =="":
            self.OUTPUT_DIRECTORY = os.path.join(os.getcwd(),'Output')
        else:
            self.OUTPUT_DIRECTORY = OUTPUT_DIRECTORY  ## Run directory?
        
        
        self.RAW_FILE = RAW_FILE
        self.POST_FILE = POST_FILE
        
        self.EXTRACT_PHOTO_METADATA = EXTRACT_PHOTO_METADATA
        self.SELECT_DEVICES = SELECT_DEVICES
        self.DEVICES = DEVICES
        self.REMOVE_PHOTOS_TAKEN_BY_PLANE = REMOVE_PHOTOS_TAKEN_BY_PLANE
        self.DO_RECURSIVE = DO_RECURSIVE
        self.DETECT_OUTLIARS = DETECT_OUTLIARS
        self.PERCENTILE = PERCENTILE
        self.MAPIT = MAPIT
        self.REVERSE_GEOCODE = REVERSE_GEOCODE
    

        self.PROCESSED_DATA =  os.path.join(self.OUTPUT_DIRECTORY,'Data')
        
        if not os.path.exists(self.PROCESSED_DATA): os.makedirs(self.PROCESSED_DATA)    
        
        self.PLOT_PATH = os.path.join(self.OUTPUT_DIRECTORY,'Figures')
                
        self.RAW_METADATA_FILE = os.path.join(self.PROCESSED_DATA, self.RAW_FILE)
        
        self.POST_PROCESSED_DATA = os.path.join(self.PROCESSED_DATA, self.POST_FILE)
        
        
        self._user_vars = {'EXTRACT_PHOTO_METADATA':self.EXTRACT_PHOTO_METADATA,\
               'INPUT_PIC_DIRECTORY':self.INPUT_PIC_DIRECTORY, 'POST_FILE':self.POST_FILE,\
               'POST_PROCESSED_DATA':self.POST_PROCESSED_DATA, 'RAW_FILE':self.RAW_FILE,\
               'RAW_METADATA_FILE':self.RAW_METADATA_FILE,\
               'REMOVE_PHOTOS_TAKEN_BY_PLANE':self.REMOVE_PHOTOS_TAKEN_BY_PLANE,\
               'SELECT_DEVICES':self.SELECT_DEVICES,'DEVICES':self.DEVICES,\
               'PLOT_PATH':self.PLOT_PATH,'MAPIT':self.MAPIT,'REVERSE_GEOCODE':self.REVERSE_GEOCODE,\
               'DO_RECURSIVE':self.DO_RECURSIVE,'DETECT_OUTLIARS':self.DETECT_OUTLIARS,\
               'PERCENTILE':self.PERCENTILE,'PROCESSED_DATA':self.PROCESSED_DATA,\
               'OUTPUT_DIRECTORY':self.OUTPUT_DIRECTORY} 
     
        
        USER_DEFINED_VARIABLES.get_default_data(self)
    
    def get_default_data(self):
        return self._user_vars 
    """    
    @classmethod
    def set_EXTRACT_PHOTO_METADATA(cls, EXTRACT_PHOTO_METADATA:bool):
        cls.EXTRACT_PHOTO_METADATA=EXTRACT_PHOTO_METADATA
        
    @classmethod
    def set_INPUT_PIC_DIRECTORY(cls,INPUT_PIC_DIRECTORY:str):
        cls.INPUT_PIC_DIRECTORY=INPUT_PIC_DIRECTORY
    
    @classmethod   
    def set_OUTPUT_DIRECTORY(cls, OUTPUT_DIRECTORY:str):
        cls.OUTPUT_DIRECTORY=OUTPUT_DIRECTORY
    
    @classmethod
    def set_POST_FILE(cls, POST_FILE:str):
        cls.POST_FILE=POST_FILE
    
    @classmethod
    def set_RAW_FILE(cls, RAW_FILE:str):
        cls.RAW_FILE=RAW_FILE
    
    @classmethod
    def set_SELECT_DEVICES(cls, SELECT_DEVICES:bool):
        cls.SELECT_DEVICES=SELECT_DEVICES
    
    @classmethod
    def set_DEVICES(cls, DEVICES:list):
        cls.DEVICES=DEVICES
     
    @classmethod
    def set_REMOVE_PHOTOS_TAKEN_BY_PLANE(cls, REMOVE_PHOTOS_TAKEN_BY_PLANE:bool):
        cls.REMOVE_PHOTOS_TAKEN_BY_PLANE=REMOVE_PHOTOS_TAKEN_BY_PLANE
     
    @classmethod
    def set_DO_RECURSIVE(cls, DO_RECURSIVE:bool):
        cls.DO_RECURSIVE=DO_RECURSIVE
    
    @classmethod
    def set_DETECT_OUTLIARS(cls, DETECT_OUTLIARS:bool):
        cls.DETECT_OUTLIARS=DETECT_OUTLIARS
    
    @classmethod    
    def set_PERCENTILE(cls, PERCENTILE:str):
        cls.PERCENTILE=PERCENTILE        
      
    @classmethod
    def set_MAPIT(cls,  MAPIT:bool):
        cls.MAPIT=MAPIT
        
    @classmethod   
    def set_REVERSE_GEOCODE(cls, REVERSE_GEOCODE:bool):
        cls.REVERSE_GEOCODE=REVERSE_GEOCODE
        
    """    
    def status_variables(cls):
        """ SET BEFORE PASSING TO MAIN"""
        
        # IF NOT EXIST... Make to save the outputs
        if not os.path.exists(cls.OUTPUT_DIRECTORY): os.makedirs(cls.OUTPUT_DIRECTORY)    
        if not os.path.exists(cls.PROCESSED_DATA): os.makedirs(cls.PROCESSED_DATA)    
        if not os.path.exists(cls.PLOT_PATH): os.makedirs(cls.PLOT_PATH)    

        cls.user_vars = {'EXTRACT_PHOTO_METADATA':cls.EXTRACT_PHOTO_METADATA,\
               'INPUT_PIC_DIRECTORY':cls.INPUT_PIC_DIRECTORY, 'POST_FILE':cls.POST_FILE,\
               'POST_PROCESSED_DATA':cls.POST_PROCESSED_DATA, 'RAW_FILE':cls.RAW_FILE,\
               'RAW_METADATA_FILE':cls.RAW_METADATA_FILE,\
               'REMOVE_PHOTOS_TAKEN_BY_PLANE':cls.REMOVE_PHOTOS_TAKEN_BY_PLANE,\
               'SELECT_DEVICES':cls.SELECT_DEVICES,'DEVICES':cls.DEVICES,\
               'PLOT_PATH':cls.PLOT_PATH,'MAPIT':cls.MAPIT,'REVERSE_GEOCODE':cls.REVERSE_GEOCODE,\
               'DO_RECURSIVE':cls.DO_RECURSIVE,'DETECT_OUTLIARS':cls.DETECT_OUTLIARS,\
               'PERCENTILE':cls.PERCENTILE,'PROCESSED_DATA':cls.PROCESSED_DATA,\
               'OUTPUT_DIRECTORY':cls.OUTPUT_DIRECTORY} 
        return cls.user_vars