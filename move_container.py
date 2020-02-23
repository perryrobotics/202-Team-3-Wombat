#!/usr/bin/python
import os, sys
import ctypes
K=ctypes.CDLL("/usr/lib/libkipr.so")
from line_following import *
from library import *
from mm_dist import *
from thresh import *

def move_container():
	forward_mm(800,5)
	close_claw(80)
	arm_up(80)
	turn_left(800,200)
	line_follow_back(800, 20)
	elbow_out(40)
	arm_under(80)
	turn_left(800,20)