#!/usr/bin/python
import os, sys
from wallaby import *
from line_following import *
from library import *
from mm_dist import *
from thresh import *

def getting_palms():
	for x in range(5):
		#grab 1
		drive_to_over(900)
		back_mm(1500, 5)
		turn_right(500, 1.7)
		arm_part(80)
		elbow_90(80)
		half_claw(100)
		arm_almost(80)
		open_claw(80)
		arm_down(80)
		close_claw(100)
		turn_left(800,1.7)
		arm_part(80)
		elbow_back(80)
		arm_back(80)
		back_mm(1500, 14)
		elbow_out(80)
		half_claw(50)
		close_claw(80)
		elbow_back(80)
		#turn_left(800, 5)
		#right_to_black(800)
		#turn_left(800, 0.5)
		#grab 2
		drive_to_over(900)
		back_mm(1500, 5)
		turn_right(500, 1.5)
		arm_part(80)
		elbow_90(80)
		half_claw(100)
		arm_almost(80)
		elbow_inside_mine(70)
		open_claw(100)
		forward_mm(800, 2)
		arm_down(100)
		close_claw(100)
		back_mm(800, 2)
		turn_left(800,1.5)
		arm_part(80)
		elbow_back(80)
		arm_back(80)
		back_mm(1500, 14)
		elbow_out(80)
		half_claw(50)
		close_claw(80)
		elbow_back(80)
		turn_left(800, 3)

	
	
        
        
        
        