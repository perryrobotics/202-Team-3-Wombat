#!/usr/bin/python
import os, sys
from wallaby import *

Lmotor = 3
Rmotor = 0
    
Arm = 0
Arm_back = 0
Arm_part = 400
Arm_up = 700
Arm_down = 1625
Arm_almost = 1200
Arm_mostly = 1400

    
Elbow = 1
Elbow_normal = 1500
Elbow_out = 0
Elbow_back = 2040
Elbow_part = 1000
Elbow_inside = 1425
    
Claw = 2
Claw_open = 950
Claw_half = 500
Claw_close = 0

Back = 3
Back_up = 0
Back_half = 1000
Back_down = 2040
    
def move(speed, ticks):
	cmpc(Lmotor)
	mav(Lmotor, speed);
	L.mav(Rmotor, speed);
	while L.gmpc(Lmotor) < ticks:
		pass
	ao()
            
def move_back(speed, ticks):
	cmpc(Lmotor)
	mav(Lmotor, -speed);
	mav(Rmotor, -speed);
	while gmpc(Lmotor) > -ticks:
		pass
	ao()

def move_left(speed, ticks):
	cmpc(Rmotor)
  	cmpc(Lmotor)
	mav(Rmotor, speed)
	while gmpc(Rmotor) < ticks:
		pass
	ao()

def move_right(speed, ticks):
	cmpc(Lmotor)
	mav(Lmotor, speed)
	while gmpc(Lmotor) < ticks:
		pass
	ao()

############################

def move_servo_slow(port, start_pos, end_pos, step):
	if  end_pos < start_pos:
		step=-step
  	for pos in range(start_pos, end_pos, step):
		set_servo_position(port, pos)
		msleep(50)
 	set_servo_position(port, end_pos)
            
def arm_back(step):
	move_servo_slow(Arm, get_servo_position(Arm), Arm_back, step)
	msleep(500)
        
def arm_part(step):
	move_servo_slow(Arm, get_servo_position(Arm), Arm_part, step)
	msleep(500)
    
def arm_up(step):
	move_servo_slow(Arm, get_servo_position(Arm), Arm_up, step)
	msleep(500)
        
def arm_down(step):
	move_servo_slow(Arm, get_servo_position(Arm), Arm_down, step)
	msleep(500)
        
def arm_almost(step):
	move_servo_slow(Arm, get_servo_position(Arm), Arm_almost, step)
	msleep(500)
        
def arm_mostly(step):
	move_servo_slow(Arm, get_servo_position(Arm), Arm_mostly, step)
	msleep(500)
############################
        
def elbow_back(step):
	move_servo_slow(Elbow, get_servo_position(Elbow), Elbow_back, step)
	msleep(500)
        
def elbow_out(step):
	move_servo_slow(Elbow, get_servo_position(Elbow), Elbow_out, step)
	msleep(500)
        
def elbow_90(step):
	move_servo_slow(Elbow, get_servo_position(Elbow), Elbow_normal, step)
	msleep(500)
 
def elbow_inside_mine(step):
	move_servo_slow(Elbow, get_servo_position(Elbow), Elbow_inside, step)
	msleep(500)
        
def elbow_back(step):
	move_servo_slow(Elbow, get_servo_position(Elbow), Elbow_back, step)
	msleep(300)
        
def elbow_part(step):
	move_servo_slow(Elbow, get_servo_position(Elbow), Elbow_part, step)
	msleep(300)
        
#############################

def open_claw(step):
	move_servo_slow(Claw, get_servo_position(Claw), Claw_open, step)
	msleep(500)
        
def half_claw(step):
  	move_servo_slow(Claw, get_servo_position(Claw), Claw_half, step)
	msleep(500)
        
def close_claw(step):
  	move_servo_slow(Claw, get_servo_position(Claw), Claw_close, step)
	msleep(500)

###########################
        
def up_back(step):
	move_servo_slow(Back, get_servo_position(Back), Back_up, step)
	msleep(500)
        
def half_back(step):
  	move_servo_slow(Back, get_servo_position(Back), Back_half, step)
	msleep(500)
        
def down_back(step):
  	move_servo_slow(Back, get_servo_position(Back), Back_down, step)
	msleep(500)
