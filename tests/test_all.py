#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:46:22 2019

@author: ericallen


TESTS THE FOLLOWING FUNCTIONS

src.lib.detectOutliers
    user_response
    haversine
    get_percentile_value
    get_out_of_range_value

src.lib.reformat_time
    reformatTime

src.lib.get_lat_lon
    getLatLon
    
pytest -q -rs test_all.py
"""
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.detectOutliers import user_response, haversine, get_percentile_value,get_out_of_range_value
from src.reformat_time import reformatTime
from src.get_lat_lon import getLatLon

def test_getLatLon():
    
    # EMPTY STRINGS ARE NOT POSSIBLE
    t1lat, t1lon = getLatLon(str("44 deg 8\' 4.98\""),str("9 deg 41\' 0.09\""),"North", "East")
    truelat1 = 44.134717
    truelon1 = 9.683358
    assert abs(t1lat-truelat1) < 0.000001
    assert abs(t1lon-truelon1) < 0.000001

    t2lat, t2lon = getLatLon(str("51 deg 29\' 43.95\""),str("0 deg 7\' 29.51\""),"North", "West")
    truelat2 = 51.495542
    truelon2 = -0.124864
    assert abs(t2lat-truelat2) < 0.000001
    assert abs(t2lon-truelon2) < 0.000001
    
    t3lat, t3lon = getLatLon(str("38 deg 48\' 44.75\""),str("77 deg 15\' 54.05\"	"),"South", "West")
    truelat3 = -38.812431
    truelon3 = -77.265014
    assert abs(t3lat-truelat3) < 0.000001
    assert abs(t3lon-truelon3) < 0.000001
    
    t4lat, t4lon = getLatLon(str("0 deg 0\' 0.00\""),str("0 deg 0\' 0.00\""),"North", "East")
    assert t4lat == 0.0
    assert t4lon == 0.0
    
    t5lat, t5lon = getLatLon(str("0 0\' 0.00\""),str("0 0\' 0.00\""),"North", "East")
    assert t5lat == None
    assert t5lon == None
    
    t6lat, t6lon = getLatLon(str("hello"),str("goodbye"),"North", "East")
    assert t6lat == None
    assert t6lon == None
    
    

def test_reformatTime():

    assert reformatTime("2016:10:23 00:03:44") == "2016-10-23 00:03:44"
    assert reformatTime("2018:06:25 22:49:23") == "2018-06-25 22:49:23"
    assert reformatTime("2018:06:25 22:49:23") == "2018-06-25 22:49:23"
    assert reformatTime("2018:15:25 22:49:23") == "NaN"
    assert reformatTime("2018-06-25 22:49:23") == "2018-06-25 22:49:23"
    assert reformatTime("2018/06/25 22:49:23") == "2018-06-25 22:49:23"
    assert reformatTime("2018/06/25 22:49") == "2018-06-25 22:49:00"
    assert reformatTime("") == "NaN"
    assert reformatTime("Hello") == "NaN"

def test_get_percentile_value():
    
    assert get_percentile_value("1st") == -2.326
    assert get_percentile_value("2.5th") == -1.960
    assert get_percentile_value("5th") == -1.645
    assert get_percentile_value("10th") == -1.282
    assert get_percentile_value("25th") == -0.675
    assert get_percentile_value("50th") == 0
    assert get_percentile_value("75th") == 0.675
    assert get_percentile_value("90th") == 1.282
    assert get_percentile_value("95th") == 1.645
    assert get_percentile_value("97.5th") == 1.960
    assert get_percentile_value("99th") == 2.326


def test_user_response():
    
    assert user_response("yes") == False
    assert user_response("      yes     ") == False
    assert user_response("YES") == False
    assert user_response("Yes") == False
    assert user_response("no") == True
    assert user_response("no ") == True
    assert user_response("NO") == True
    
    
def test_haversine():
    
    assert haversine(9.683358,  44.134717,  9.683358,  44.134717) == 0.0
    assert haversine(0.0,  0.0,  0.0,  0.0) == 0.0
    assert abs(haversine( 0.0,  0.0,  -1.0,  0.0)-111.19508372) < 0.01
    assert abs(haversine(-74.0060, 40.7128, 2.3508, 48.8567)-5837.14991762) < 0.01

def test_get_out_of_range_value():
    
    assert get_out_of_range_value("95th",20,2)==23.29
    assert get_out_of_range_value("99th",100,5)==111.63
