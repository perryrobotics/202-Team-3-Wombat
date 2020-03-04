#!/usr/bin/python
import os, sys
from wallaby import *
import math

sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
line_sensor = 2
over_sensor = 5
down_sensor = 0
RM=1
LM=0
m = math
pi = m.pi
TICKS_PER_ROT = 1920
WHEEL_CIRC_MM =  6.35*pi

def analog_average_median(port,times):
	median = []
	for x in range(times):
		line = []
		for x in range(times):
			line.append(analog(port))
    	for x in range(times-1):
			test = line[0]+line.pop(1)
			line_average = test/times
			median.append(line_average)
	median.sort()
	if times%2 == 1:
		times = times +1
	med = times/2
	again = median[med]
	print (again)
	return again

def thresh_check():
	print("start thresh")
	thresh = analog_average_median(line_sensor,5)
	print("end thresh")
	return thresh - 200

def drive_to_black(speed):
	mav(RM, speed)
	mav(LM, speed)
	while analog_average_median(line_sensor,5) < thresh:
		pass
	ao()

def back_to_black(speed):
	mav(RM, -speed)
	mav(LM, -speed)
	while analog_average_median(line_sensor,5) < thresh:
		pass
	ao()

def drive_to_white(speed):
	mav(RM, speed)
	mav(LM, speed)
	while analog_average_median(line_sensor,5) > thresh:
		pass
	ao()

def right_to_black(speed):
	mav(RM, -speed)
	mav(LM, speed)
	while analog_average_median(over_sensor,5) < thresh:
		pass
	ao() 
            
def line_follow(speed,dist):
	mav(RM, speed)
	mav(LM, speed)
	cmpc(LM) 
	total_ticks= (dist/WHEEL_CIRC_MM)*TICKS_PER_ROT
	while gmpc(LM) < total_ticks: 
		if analog_average_median(over_sensor,5) < thresh:
			mav(RM, speed-100)
			mav(LM, speed)
		else:
			mav(RM, speed)
			mav(LM, speed-200)
	ao()

def line_follow_back(speed,dist):
	mav(RM, -speed)
	mav(LM, -speed)
	cmpc(LM) 
	total_ticks= (dist/WHEEL_CIRC_MM)*TICKS_PER_ROT
	while gmpc(LM) > -total_ticks: 
		if analog_average_median(over_sensor,5) < thresh:
			mav(RM, -speed+100)
			mav(LM, -speed)
		else:
			mav(RM, -speed)
			mav(LM, -speed+100)
	ao()
                
def drive_to_over(speed):
	while analog(down_sensor) > 2400:
		mav(RM, speed)
		mav(LM, speed)
	ao()
                
                
thresh = 1300