#!/usr/bin/python
import os, sys
import ctypes
K=ctypes.CDLL("/usr/lib/libkipr.so")

Lmotor = 3
Rmotor = 0
    
Arm = 0
Arm_back = 0
Arm_block = 200
Arm_up = 700
Arm_down = 2040
Arm_under = 1400
Arm_transport = 900
    
Elbow = 1
Elbow_normal = 1400
Elbow_out = 0
Elbow_back = 2040
    
Claw = 2
Claw_open = 1050
Claw_half = 500
Claw_close = 0

Back = 3
Back_up = 0
Back_half = 1000
Back_down = 2040
    
def move(speed, ticks):
	K.cmpc(Lmotor)
	K.mav(Lmotor, speed);
	L.mav(Rmotor, speed);
	while L.gmpc(Lmotor) < ticks:
		pass
	K.ao()
            
def move_back(speed, ticks):
	K.cmpc(Lmotor)
	K.mav(Lmotor, -speed);
	K.mav(Rmotor, -speed);
	while K.gmpc(Lmotor) > -ticks:
		pass
	K.ao()

def move_left(speed, ticks):
	K.cmpc(Rmotor)
  	K.cmpc(Lmotor)
	K.mav(Rmotor, speed)
	while K.gmpc(Rmotor) < ticks:
		pass
	K.ao()

def move_right(speed, ticks):
	K.cmpc(Lmotor)
	K.mav(Lmotor, speed)
	while K.gmpc(Lmotor) < ticks:
		pass
	K.ao()

############################

def move_servo_slow(port, start_pos, end_pos, step):
	if  end_pos < start_pos:
		step=-step
  	for pos in range(start_pos, end_pos, step):
		K.set_servo_position(port, pos)
		K.msleep(50)
 	K.set_servo_position(port, end_pos)
            
def arm_back(step):
	move_servo_slow(Arm, K.get_servo_position(Arm), Arm_back, step)
	K.msleep(500)
        
def arm_block(step):
	move_servo_slow(Arm, K.get_servo_position(Arm), Arm_block, step)
	K.msleep(500)
    
def arm_up(step):
	move_servo_slow(Arm, K.get_servo_position(Arm), Arm_up, step)
	K.msleep(500)
        
def arm_down(step):
	move_servo_slow(Arm, K.get_servo_position(Arm), Arm_down, step)
	K.msleep(500)
        
def arm_transport(step):
	move_servo_slow(Arm, K.get_servo_position(Arm), Arm_transport, step)
	K.msleep(500)
        
def arm_under(step):
	move_servo_slow(Arm, K.get_servo_position(Arm), Arm_under, step)
	K.msleep(500)
############################
        
def elbow_back(step):
	move_servo_slow(Elbow, K.get_servo_position(Elbow), Elbow_back, step)
	K.msleep(500)
        
def elbow_out(step):
	move_servo_slow(Elbow, K.get_servo_position(Elbow), Elbow_out, step)
	K.msleep(500)
        
def elbow_90(step):
	move_servo_slow(Elbow, K.get_servo_position(Elbow), Elbow_normal, step)
	K.msleep(500)
        
def elbow_back(step):
	move_servo_slow(Elbow, K.get_servo_position(Elbow), Elbow_back, step)
	K.msleep(300)
        
#############################

def open_claw(step):
	move_servo_slow(Claw, K.get_servo_position(Claw), Claw_open, step)
	K.msleep(500)
        
def half_claw(step):
  	move_servo_slow(Claw, K.get_servo_position(Claw), Claw_half, step)
	K.msleep(500)
        
def close_claw(step):
  	move_servo_slow(Claw, K.get_servo_position(Claw), Claw_close, step)
	K.msleep(500)

###########################
        
def up_back(step):
	move_servo_slow(Back, K.get_servo_position(Back), Back_up, step)
	K.msleep(500)
        
def half_back(step):
  	move_servo_slow(Back, K.get_servo_position(Back), Back_half, step)
	K.msleep(500)
        
def down_back(step):
  	move_servo_slow(Back, K.get_servo_position(Back), Back_down, step)
	K.msleep(500)
