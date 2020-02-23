#!/usr/bin/python
import os, sys
import ctypes
K=ctypes.CDLL("/usr/lib/libkipr.so")
from line_following import *
from library import *
from mm_dist import *
from thresh import *

def up_ramp():
	forward_mm(1000, 110)
	back_mm(1500, 5)
	turn_right(1000, 90)
	forward_mm(1500, 12)
	back_mm(1500, 10)
	turn_left(1000, 180)
	back_mm(1500, 10)
	#arm_half(10)
	#claw_open(100)
	thresh = thresh_check()
	forward_mm(1500, 25)
	line_follow(900, 30)
	elbow_back(20)

        
        
        
        
        
        
        
        