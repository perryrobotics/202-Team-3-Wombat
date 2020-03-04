#!/usr/bin/python
import os, sys
from wallaby import *
from line_following import *
from library import *
from mm_dist import *
from thresh import *

def get_container_new():
	back_to_black(1500)
	back_mm(1500, 15)
	turn_left(900, 15)
	back_mm(1500, 3)
	down_back(150)
	turn_right(800,90)
	drive_to_black(1500)
	turn_left(900, 20)
	forward_mm(1500,27)
	open_claw(150)
	close_claw(150)
	turn_left(900,130)
	up_back(150)
	drive_to_black(1500)
	forward_mm(1500, 30)
	back_mm(1500, 10)
	turn_left(900, 80)
	forward_mm(1500, 10)
	drive_to_black(1500)
	forward_mm(1500, 25)
	back_mm(1500, 6)
	turn_left(900, 73)

              
              
              
              
              
              
              