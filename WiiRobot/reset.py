

#Code pour remettre le robot en mode entrainement, en cas d'erreur

from pyniryo import *
ip_robot_address = "10.4.1.51"
robot = NiryoRobot(ip_robot_address)
robot.calibrate_auto()
robot.set_learning_mode(True)
robot.close_connection()