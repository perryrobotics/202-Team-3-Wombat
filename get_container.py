#!/usr/bin/python
import os, sys
import ctypes
K=ctypes.CDLL("/usr/lib/libkipr.so")
from line_following import *
from library import *
from mm_dist import *
from thresh import *

def get_container():
	#arm_block(80)
	#open_claw(80)
	#forward_mm(800, 22)
	#close_claw(70)
	#elbow_90(60)
	#back_mm(800, 30)
	#elbow_back(80)
	open_claw(80)
	turn_right(800, 25)
	back_to_black(600)
	back_mm(800, 2)
	turn_left(800, 25)
	back_mm(800,15)
	down_back(80)
	drive_to_white(600)
	turn_right(800, 40)