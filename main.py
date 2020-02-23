#!/usr/bin/python
import os, sys
import ctypes
K=ctypes.CDLL("/usr/lib/libkipr.so")
from line_following import *
from library import *
from mm_dist import *
from thresh import *
from get_container_new import *
from up_ramp import *
from getting_palms import *

K.enable_servos()
arm_back(10)
elbow_back(10)
close_claw(10)
up_back(70)
    
get_container_new()
up_ramp()
getting_palms()