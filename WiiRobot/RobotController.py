from pyniryo import *
import time
ip_robot_address = "10.4.1.51"

robot = NiryoRobot(ip_robot_address)
robot.calibrate_auto()
#default home
x= 0.54
y=0.15
z=-0.5
roll=0.0
pitch=0.0
yaw=0.0
robot.move_joints(0.54,0.15,-0.5,0.0,0.0,0.0)
while True:
    time.sleep(0.2)
    while True:
        action_keyboad =input("Do a move:")
        if input("up")=="up":
            x += 0.1
    robot.move_joints(x, y, z, roll, pitch, yaw)

robot.set_learning_mode(True)



robot.close_connection()