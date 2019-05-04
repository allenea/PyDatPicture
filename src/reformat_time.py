#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 00:38:17 2019

@author: ericallen

Reformats the date and time

"""
import datetime as dt

def reformatTime(date_time):
    """
    Reformats date to a YYYY-mm-dd HH:MM:SS format. Which I prefer
    
    INPUT
       date_time - (str) as formatted from the metadata
     OUPUT
         fmtTime - (str) reformatted string with date/time info
    """
    # Process Time: Not critical but I like the more traditional Format
    if date_time  != "":
        try:
            dt_tuple = dt.datetime.strptime(date_time,"%Y:%m:%d %H:%M:%S")
            fmtTime = dt_tuple.strftime("%Y-%m-%d %H:%M:%S")
        except:
            print("INVALID TIME")
            fmtTime = "NaN"
    else:
        print("Missing Date/Time")
        fmtTime = "NaN"
    return fmtTime