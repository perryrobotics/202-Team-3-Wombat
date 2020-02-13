#!/usr/bin/python
import os, sys
import ctypes
K=ctypes.CDLL("/usr/lib/libkipr.so")
from line_following import *
from library import *
from mm_dist import *

def on_ramp():
	back_mm(800, 7)
	turn_left(800, 20)
	forward_mm(800, 3)
	turn_left(800, 40)
	back_mm(800, 45)