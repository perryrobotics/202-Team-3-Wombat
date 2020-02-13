#!/usr/bin/python
import os, sys
import ctypes
K=ctypes.CDLL("/usr/lib/libkipr.so")
from line_following import *
from library import *
from mm_dist import *
from thresh import *

def to_ramp():
	forward_mm(800, 5)
	up_back(80)
	forward_mm(800, 12)
	turn_left(800,140)
	forward_mm(800, 30)
	back_mm(800, 5)
	turn_left(800, 85)
	forward_mm(800, 20)
	#getting container
	arm_up(80)
	close_claw(80)
	arm_back(80)
	forward_mm(800, 12)
	turn_left(500, 70)
	#forward_mm(800, 10)
	turn_left(800, 80)
	forward_mm(800, 20)
	arm_down(80)
	forward_mm(1000, 120)