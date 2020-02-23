#!/usr/bin/python
import os, sys
import ctypes
K=ctypes.CDLL("/usr/lib/libkipr.so")
from line_following import *
from library import *
from mm_dist import *
from thresh import *

def getting_palms():
	#grab 1
	drive_to_over(900)
	back_mm(800, 3)
	arm_part(15)
	elbow_90(15)
	half_claw(100)
	arm_almost(15)
	open_claw(50)
	arm_down(15)
	close_claw(100)
	arm_part(11)
	elbow_back(15)
	arm_back(20)
	back_mm(800, 14)
	elbow_out(15)
	half_claw(40)
	close_claw(50)
	elbow_back(15)
	#grab 2
	drive_to_over(900)
	back_mm(800, 3)
	arm_part(15)
	elbow_90(15)
	half_claw(100)
	arm_mostly(15)
	forward_mm(800, 1)
	open_claw(50)
	close_claw(100)
	back_mm(800, 1)
	arm_part(15)
	elbow_back(15)
	arm_back(20)
	back_mm(800, 14)
	elbow_out(15)
	half_claw(40)
	close_claw(50)
	elbow_back(15)
	
	
        
        
        
        