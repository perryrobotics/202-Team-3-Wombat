#!/usr/bin/python
import os, sys
from wallaby import *

from line_following import *
from library import *
from mm_dist import *
from thresh import *
from get_container_new import *
from up_ramp import *
from getting_palms import *
from wait_for_start import *

enable_servos()
arm_back(50)
elbow_back(50)
close_claw(50)
up_back(70)
wait_for_start(4)
shut_down_in(120)
get_container_new()
up_ramp()
getting_palms()