#!/usr/bin/python
import os, sys
from wallaby import *
from line_following import *
from library import *
from mm_dist import *
from thresh import *

def up_ramp():
	elbow_90(150)
	forward_mm(1500, 113)
	back_mm(1500, 5)
	turn_right(1000, 80)
	forward_mm(1000, 12)
	back_mm(1500, 10)
	turn_left(1000, 170)
	back_mm(1500, 10)
	#arm_half(10)
	#claw_open(100)
	thresh = thresh_check()
	line_follow(900, 60)
	elbow_back(20)

        
        
        
        
        
        
        
        