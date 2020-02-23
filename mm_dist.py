#!/usr/bin/python
import os, sys
import ctypes
K=ctypes.CDLL("/usr/lib/libkipr.so")
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
	K.cmpc(LM)
	K.cmpc(RM)
	total_ticks= (float(dist)/WHEEL_CIRC_MM)*TICKS_PER_ROT
	K.mrp(LM, speed, int(total_ticks))
	K.mrp(RM, speed, int(total_ticks))
	K.bmd(RM)
	K.ao()

def back_mm(speed, dist):
	K.cmpc(LM)
	K.cmpc(RM)
	total_ticks= (float(dist)/WHEEL_CIRC_MM)*TICKS_PER_ROT
	K.mrp(LM, -speed, -int(total_ticks))
	K.mrp(RM, -speed, -int(total_ticks))
	K.bmd(RM)
	K.ao()

def left_mm(speed, dist):
	K.cmpc(LM)
	K.cmpc(RM)
	total_ticks= (float(dist)/WHEEL_CIRC_MM)*TICKS_PER_ROT
	K.mrp(RM, speed, int(total_ticks))
	K.bmd(RM)
	K.ao()

def right_mm(speed, dist):
	K.cmpc(LM)
	K.cmpc(RM)
	total_ticks= (float(dist)/WHEEL_CIRC_MM)*TICKS_PER_ROT
	K.mrp(LM, speed, int(total_ticks))
	K.bmd(LM)
	K.ao()

def turn_left(speed, deg):
	mm_to_go = 0.0
	print(deg)
	K.cmpc(LM)
	K.cmpc(RM)
	mm_to_go = 1920*( (3.25/1.375)*(float(deg)/360) )
	K.mrp(RM,int(speed) ,-int(mm_to_go))
	K.mrp(LM, int(speed) ,int(mm_to_go))
	K.bmd(RM)
	K.ao()

def turn_right(speed, deg):
	K.cmpc(LM)
	K.cmpc(RM)
	mm_to_go = 1920*((3.25/1.375)*(float(deg)/360))
	K.mrp(LM, speed, -int(mm_to_go))
	K.mrp(RM, speed, int(mm_to_go))
	K.bmd(RM)
	K.ao()