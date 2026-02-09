# ----------------------------------------------------------------------------- #
#                                                                               #                                                                          
#    Project:        Clawbot Controller with Events                             #
#    Module:         main.py                                                    #
#    Author:         VEX                                                        #
#    Created:        Fri Aug 05 2022                                            #
#    Description:    This example will use Controller button events to          # 
#                    control the V5 Clawbot arm and claw                        #
#                                                                               #                                                                          
#    Configuration:  V5 Clawbot (Individual Motors)                             #
#                    Controller                                                 #
#                    Claw Motor in Port 3                                       #
#                    Arm Motor in Port 8                                        #
#                    Left Motor in Port 1                                       #
#                    Right Motor in Port 10                                     #
#                                                                               #                                                                          
# ----------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

# Robot configuration code
shoulder_motor = Motor(Ports.PORT20, GearSetting.RATIO_36_1, False)
elbow_motor = Motor(Ports.PORT11, GearSetting.RATIO_36_1, False)
left_wheel_motor = Motor(Ports.PORT19, GearSetting.RATIO_18_1, False)
right_wheel_motor = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
wrist_motor = Motor(Ports.PORT12, GearSetting.RATIO_18_1, False)
claw_motor = Motor(Ports.PORT13, GearSetting.RATIO_36_1, False)


# Begin project code
# Create callback functions for each controller button event

#R1 clockwise for wrist 
def controller_R1_Pressed():
    wrist_motor.spin(FORWARD)
    while controller_1.buttonR1.pressing():
        wait(5, MSEC)
    wrist_motor.stop()

#L1 counter-clockwise for wrist 
def controller_L1_Pressed():
    wrist_motor.spin(REVERSE)
    while controller_1.buttonL1.pressing():
        wait(5, MSEC)
    wrist_motor.stop()

#L2 opening claw
def controller_L2_Pressed():
    claw_motor.spin(FORWARD)
    while controller_1.buttonL2.pressing():
        wait(5, MSEC)
    claw_motor.stop()

#R2 closing claw 
def controller_R2_Pressed():
    claw_motor.spin(REVERSE)
    while controller_1.buttonR2.pressing():
        wait(5, MSEC)
    claw_motor.stop()

#Button up (arrow up) shoulder 
def controller_Button_Up():
    shoulder_motor.spin(FORWARD)
    while controller_1.buttonUp.pressing():
        wait(5, MSEC)
    shoulder_motor.stop()

#Button down (arrow down) shoulder
def controller_Button_Down():
    shoulder_motor.spin(FORWARD)
    while controller_1.buttonUp.pressing():
        wait(5, MSEC)
    shoulder_motor.stop()

#ButtonX elbow up 
def controller_ButtonX_Pressing():
    elbow_motor.spin(FORWARD)
    while controller_1.buttonX.pressing():
        wait(5, MSEC)
    elbow_motor.stop()

#ButtonB elbow down 
def controller_ButtonB_Pressed():
    elbow_motor.spin(REVERSE)
    while controller_1.buttonB.pressing():
        wait(5, MSEC)
    elbow_motor.stop()

#Left joystick is movement of the wheels 

def user_control():
    brain.screen.clear_screen()
    brain.screen.print("driver control")
    # place driver control in this while loop
    while True:
        
        maxRPM = 200
        ForwardBackwardJS = (controller.axis3.position() / 100) * maxRPM
        turningJS = (controller.axis1.position() / 100) * maxRPM
        
        rightJSspeed = ForwardBackwardJS + turningJS
        leftJSspeed = ForwardBackwardJS - turningJS

        rightGears.spin(FORWARD, rightJSspeed, RPM)
        leftGears.spin(FORWARD, leftJSspeed, RPM)
            
        wait(20, MSEC) 

def controller_L1_Pressed():
    arm_motor.spin(FORWARD)
    while controller_1.buttonL1.pressing():
        wait(5, MSEC)
    arm_motor.stop()

def controller_L2_Pressed():
    arm_motor.spin(REVERSE)
    while controller_1.buttonL2.pressing():
        wait(5, MSEC)
    arm_motor.stop()

def controller_R1_Pressed():
    claw_motor.spin(REVERSE)
    while controller_1.buttonR1.pressing():
        wait(5, MSEC)
    claw_motor.stop()

def controller_R2_Pressed():
    claw_motor.spin(FORWARD)
    while controller_1.buttonR2.pressing():
        wait(5, MSEC)
    claw_motor.stop()

def controller_Button_Up():
    up_down_claw.spin(REVERSE)
    while controller_1.buttonUp.pressing():
        wait(5, MSEC)
    up_down_claw.stop()

def controller_Button_Down():
    up_down_claw.spin(FORWARD)
    while controller_1.buttonDown.pressing():
        wait(5, MSEC)
    up_down_claw.stop()


# Create Controller callback events - 15 msec delay to ensure events get registered
controller_1.buttonL1.pressed(controller_L1_Pressed)
controller_1.buttonL2.pressed(controller_L2_Pressed)
controller_1.buttonR1.pressed(controller_R1_Pressed)
controller_1.buttonR2.pressed(controller_R2_Pressed)
controller_1.buttonUp.pressed(controller_Button_Up)
controller_1.buttonUp.pressed(controller_Button_Down)
wait(15, MSEC)

# Configure Arm and Claw motor hold settings and velocity
arm_motor.set_stopping(HOLD)
claw_motor.set_stopping(HOLD)
arm_motor.set_velocity(60, PERCENT)
claw_motor.set_velocity(30, PERCENT)
up_down_claw.set_stopping(HOLD)
up_down_claw.set_velocity(20, PERCENT)

# Main Controller loop to set motors to controller axis postiions
while True:
    left_motor.set_velocity(controller_1.axis3.position(), PERCENT)
    right_motor.set_velocity(controller_1.axis2.position(), PERCENT)
    left_motor.spin(FORWARD)
    right_motor.spin(FORWARD)
    wait(5, MSEC)

