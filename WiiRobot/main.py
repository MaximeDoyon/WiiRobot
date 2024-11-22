#!/usr/bin/env python3

import wiimote
import time
import sys
from pyniryo import *
import time
ip_robot_address = "10.4.1.51"

robot = NiryoRobot(ip_robot_address)
robot.calibrate_auto()
robot.update_tool()
robot.set_conveyor()


"""
A simple demo script for the wiimote.py module.
Start as `python3 wiimote_demo.py [bluetooth address of Wiimote]` and follow
instructions.
"""

input("Press the 'sync' button on the back of your Wiimote Plus " +
      "or buttons (1) and (2) on your classic Wiimote.\n" +
      "Press <return> once the Wiimote's LEDs start blinking.")

if len(sys.argv) == 1:
    addr, name = wiimote.find()[0]
elif len(sys.argv) == 2:
    addr = sys.argv[1]
    name = None

elif len(sys.argv) == 3:
    addr, name = sys.argv[1:3]
print(("Connecting to %s (%s)" % (name, addr)))
wm = wiimote.connect(addr, name)

# Demo Time!
patterns = [[1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [1, 0, 0, 0]]
for i in range(5):
    for p in patterns:
        wm.leds = p
        time.sleep(0.05)


def print_ir(ir_data):
    if len(ir_data) == 0:
        return
    for ir_obj in ir_data:
        # print("%4d %4d %2d     " % (ir_obj["x"],ir_obj["y"],ir_obj["size"]), end=' ')
        print("%4d %4d %2d     " % (ir_obj["x"], ir_obj["y"], ir_obj["size"]))
    print()

#wm.ir.register_callback(print_ir)
home = (-0.029,-0.178,0.428,-2.053,1.481,2.489)
robot.move_pose(home)
current_position =robot.get_pose()
jog_pose =[0,0,0,0,0,0]
vitesse_X = 0
vitesse_Y = 0
acceleration_X =0.001
deceleration_X =-0.001
acceleration_Y =0.001
deceleration_Y =-0.001


while True:
    if wm.buttons["A"]:
        wm.leds[1] = True
        #wm.rumble(0.1)
        #print((wm.accelerometer))
        #print(vitesse_X)
        if(wm.accelerometer[0]<0):#gauche
            if(vitesse_X<0):
                vitesse_X=0
            vitesse_X +=acceleration_X

        elif (wm.accelerometer[0] > 0):#droite
            if (vitesse_X > 0):
                vitesse_X = 0
            vitesse_X +=deceleration_X

        if (wm.accelerometer[2] < 0):#devant
            if (vitesse_Y < 0):
                vitesse_Y = 0
            vitesse_Y += acceleration_Y

        elif (wm.accelerometer[2] > 0):#derriere
            if (vitesse_Y > 0):
                vitesse_Y = 0
            vitesse_Y += deceleration_Y

        jog_pose[0]=vitesse_X
        jog_pose[1]=vitesse_Y
        print(wm.accelerometer[0])
        print(wm.accelerometer[1])
        print(wm.accelerometer[2])
        print(jog_pose)
        robot.jog_pose(jog_pose)
        #print("X: ",vitesse_X)
        #print("Y: ", vitesse_Y)
    elif wm.buttons["Home"]:
        vitesse_Y = 0
        vitesse_X = 0
        robot.move_pose(home)
        wm.speaker.beep()
        #print("beep")
    elif wm.buttons["Up"]:
        robot.jog_pose([0,0,0.005,0,0,0])
    elif wm.buttons["Down"]:
        robot.jog_pose([0,0,-0.005,0,0,0])
    elif wm.buttons["Minus"]:
        robot.close_gripper()
    elif wm.buttons["Plus"]:
        robot.open_gripper()
    elif wm.buttons["One"]:
        robot.run_conveyor(ConveyorID.ID_1, 100, ConveyorDirection.BACKWARD)
    elif wm.buttons["Two"]:
        robot.run_conveyor(ConveyorID.ID_1, 100, ConveyorDirection.FORWARD)
    elif wm.buttons["Left"]:
        robot.jog_pose([0,0,0,0,0,0.1])
    elif wm.buttons["Right"]:
        robot.jog_pose([0,0,0,0,0,-0.1])
    else:
        robot.stop_conveyor(ConveyorID.ID_1)
        wm.leds[1] = False
        pass

    time.sleep(0.1)