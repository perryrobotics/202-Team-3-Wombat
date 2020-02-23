#!/usr/bin/python
import os, sys
import ctypes
K=ctypes.CDLL("/usr/lib/libkipr.so")
from line_following import *
from library import *
from mm_dist import *
from thresh import *

def get_container_new():
	back_to_black(1500)
	back_mm(1000, 17)
	turn_left(900, 15)
	back_mm(1000, 5)
	down_back(80)
	turn_right(900,90)
	drive_to_black(1500)
	turn_left(900, 20)
	forward_mm(1000,25)
	open_claw(100)
	close_claw(80)
	turn_left(900,140)
	up_back(40)
	drive_to_black(1000)
	forward_mm(1500, 30)
	back_mm(1500, 10)
	turn_left(900, 90)
	drive_to_black(1500)
	forward_mm(1500, 25)
	back_mm(1500, 6)
	turn_left(900, 85)
	elbow_90(20)
              
              
              
              
              
              
              