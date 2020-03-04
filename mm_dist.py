#!/usr/bin/python
import os, sys
from wallaby import *

import math as m
    
LM = 0
RM = 1
pi = m.pi
#These need to be changed for your robot!
TICKS_PER_ROT = 1920
WHEEL_CIRC_MM =  6.35*pi

base = 16.51
#base - the distance between the 2 front wheels
circ_of_base = pi * base
mm_per_deg = circ_of_base / 360

def forward_mm(speed, dist):
	cmpc(LM)
	cmpc(RM)
	total_ticks= (float(dist)/WHEEL_CIRC_MM)*TICKS_PER_ROT
	mav(LM, speed)
	mav(RM, speed)
	while gmpc(LM) < total_ticks:
		pass
	ao()

def back_mm(speed, dist):
	cmpc(LM)
	cmpc(RM)
	total_ticks= (float(dist)/WHEEL_CIRC_MM)*TICKS_PER_ROT
	mav(LM, -speed)
	mav(RM, -speed)
	while gmpc(LM) > -total_ticks:
		pass
	ao()

def left_mm(speed, dist):
	cmpc(LM)
	cmpc(RM)
	total_ticks= (float(dist)/WHEEL_CIRC_MM)*TICKS_PER_ROT
	mav(LM, -speed)
	mav(RM, speed)
	while gmpc(RM) < total_ticks:
		pass
	ao()

def right_mm(speed, dist):
	cmpc(LM)
	cmpc(RM)
	total_ticks= (float(dist)/WHEEL_CIRC_MM)*TICKS_PER_ROT
	mav(LM, speed)
	mav(RM, -speed)
	while gmpc(LM) < total_ticks:
		pass
	ao()

def turn_left(speed, deg):
	mm_to_go = 0.0
	print(deg)
	cmpc(LM)
	cmpc(RM)
	mm_to_go = 1920*( (3.25/1.375)*(float(deg)/360) )
	mav(LM, -speed)
	mav(RM, speed)
	while gmpc(RM) < mm_to_go:
		pass
	ao()

def turn_right(speed, deg):
	cmpc(LM)
	cmpc(RM)
	mm_to_go = 1920*((3.25/1.375)*(float(deg)/360))
	mav(LM, speed)
	mav(RM, -speed)
	while gmpc(LM) < mm_to_go:
		pass
	ao()