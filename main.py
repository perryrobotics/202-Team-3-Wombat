#!/usr/bin/python
import os, sys
import ctypes
K=ctypes.CDLL("/usr/lib/libkipr.so")
from line_following import *
from library import *
from mm_dist import *
from get_container import *
from move_container import *
from to_ramp import *
from thresh import *
from on_ramp import *

K.enable_servos()
arm_back(70)
elbow_back(70)
close_claw(70)
up_back(70)
K.msleep(1000)
get_container()
to_ramp()