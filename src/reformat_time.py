#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 00:38:17 2019

@author: Eric Allen
Last Modified: 7 May 2019 at 11:56AM

Reformats the date and time specified below.
"""
import datetime as dt
import re

def reformatTime(date_time):
    """
    Reformats date to a YYYY-mm-dd HH:MM:SS format. Which I prefer...
    
    This could be written in 2 lines but I want to protect against potential 
    future format changes using the most traditional formats.
    
    INPUT
        date_time - (str) as formatted from the metadata
     OUPUT
        fmtTime - (str) reformatted string with date/time info
    """
    # Process Time: Not critical but I like the more traditional Format
    if date_time  != "":
        sec = 0
        try: # WORKS FOR ALL TYPICAL FORMATS
            regx = re.compile('[-/: ]')
            d_lst  = regx.split(date_time)
            if len(d_lst) == 5:
                d_lst.append(sec)
                
            dt_tuple = dt.datetime(int(d_lst[0]),int(d_lst[1]),int(d_lst[2]),\
                                   int(d_lst[3]),int(d_lst[4]),int(d_lst[5]))
            
            return dt_tuple.strftime("%Y-%m-%d %H:%M:%S")
        except:
            print("INVALID TIME")
            return "NaN"
    else:
        print("Missing Date/Time")
        return "NaN"
