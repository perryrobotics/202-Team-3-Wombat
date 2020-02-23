#!/usr/bin/python
import os, sys
import ctypes
K=ctypes.CDLL("/usr/lib/libkipr.so")
import math

sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
line_sensor = 2
over_sensor = 5
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
			line.append(K.analog(port))
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
	return thresh

def drive_to_black(speed):
	K.mav(RM, speed)
	K.mav(LM, speed)
	while analog_average_median(line_sensor,5) < thresh:
		pass
	K.ao()

def back_to_black(speed):
	K.mav(RM, -speed)
	K.mav(LM, -speed)
	while analog_average_median(line_sensor,5) < thresh:
		pass
	K.ao()

def drive_to_white(speed):
	K.mav(RM, speed)
	K.mav(LM, speed)
	while analog_average_median(line_sensor,5) > thresh:
		pass
	K.ao()

def line_follow(speed,dist):
	K.mav(RM, speed)
	K.mav(LM, speed)
	K.cmpc(LM) 
	total_ticks= (dist/WHEEL_CIRC_MM)*TICKS_PER_ROT
	while K.gmpc(LM) < total_ticks: 
		if analog_average_median(over_sensor,5) < thresh:
			K.mav(RM, speed+100)
			K.mav(LM, speed)
		else:
			K.mav(RM, speed)
			K.mav(LM, speed+100)
	K.ao()

def line_follow_back(speed,dist):
	K.mav(RM, -speed)
	K.mav(LM, -speed)
	K.cmpc(LM) 
	total_ticks= (dist/WHEEL_CIRC_MM)*TICKS_PER_ROT
	while K.gmpc(LM) > -total_ticks: 
		if analog_average_median(over_sensor,5) < thresh:
			K.mav(RM, -speed-100)
			K.mav(LM, -speed)
		else:
			K.mav(RM, -speed)
			K.mav(LM, -speed-100)
	K.ao()
                
def drive_to_over(speed):
	while K.analog(over_sensor) < 3950:
		K.mav(RM, speed)
		K.mav(LM, speed)
	K.ao()
                
                
thresh = 1300