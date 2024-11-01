from pyniryo import *
import time
ip_robot_address = "10.4.1.51"

robot = NiryoRobot(ip_robot_address)
robot.calibrate_auto()
robot.update_tool()

#Variables positions
au_dessus_plateforme = (0.140,0.066,0.445,-0.473,1.477,-0.151)
au_dessus_convoyeur = (-0.006,0.263,0.264, -1.510, 1.440, 0.394)


robot.move_pose(*au_dessus_plateforme)
time.sleep(2)
detected_objects = robot.detect_object("workspace_plateform", ObjectShape.ANY, ObjectColor.ANY)
print(detected_objects)
if detected_objects:
    print("Objet trouvé ! Préparation à la récupération")



    obj_found, shape_ret, color_ret = robot.vision_pick("workspace_plateform", 0.05, ObjectShape.ANY, ObjectColor.ANY)
    print(obj_found)
    time.sleep(2)
    robot.move_pose(*au_dessus_convoyeur)
else:
    print("aucun objet detecté")
    robot.move_pose(*au_dessus_convoyeur)







#Fin du code ( sortie et déconnexion )
robot.set_learning_mode(True)
robot.close_connection()