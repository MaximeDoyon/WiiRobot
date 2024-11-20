from pyniryo import *
import time
import keyboard
ip_robot_address = "10.4.1.51"

robot = NiryoRobot(ip_robot_address)
robot.calibrate_auto()
robot.update_tool()

#Variables positions
au_dessus_plateforme = (-0.029,-0.178,0.428,-2.053,1.481,2.489)
# au_dessus_convoyeur = (-0.006,0.263,0.264, -1.510, 1.440, 0.394)
convoyeur_id = robot.set_conveyor()


robot.move_pose(*au_dessus_plateforme)
# time.sleep(2)
# detected_objects = robot.detect_object("workspace_plateform", ObjectShape.ANY, ObjectColor.ANY)

try:
    while True:
        #Move up and down
        if keyboard.is_pressed("up"):
            print("Touche 'w' détectée ! Montée du robot...")

            position_actuelle = robot.get_pose()
            nouvelle_position = position_actuelle
            nouvelle_position.z += 0.05
            robot.move_pose(nouvelle_position)
        elif keyboard.is_pressed("down"):
            print("Touche 's' détectée ! Descente du robot...")
            position_actuelle = robot.get_pose()
            nouvelle_position = position_actuelle
            nouvelle_position.z -= 0.05
            robot.move_pose(nouvelle_position)


        #prendre objet
        elif keyboard.is_pressed("p"):
            robot.move_pose(*au_dessus_plateforme)
            time.sleep(2)
            detected_objects = robot.detect_object("workspace_plateform", ObjectShape.ANY, ObjectColor.ANY)
            if detected_objects:
                print("Objet trouvé ! Préparation à la récupération")
                obj_found, shape_ret, color_ret = robot.vision_pick("workspace_plateform", 0.005, ObjectShape.ANY, ObjectColor.ANY)
                robot.move_pose(au_dessus_plateforme)


        #Bouge profondeur
        elif keyboard.is_pressed("a"):
            print("Touche 'a' détectée !")
            position_actuelle = robot.get_pose()
            nouvelle_position = position_actuelle
            nouvelle_position.y += 0.05
            robot.move_pose(nouvelle_position)
        elif keyboard.is_pressed("d"):
            print("Touche 'd' détectée !")
            position_actuelle = robot.get_pose()
            nouvelle_position = position_actuelle
            nouvelle_position.y -= 0.05
            robot.move_pose(nouvelle_position)

        # Bouge gauche droite
        elif keyboard.is_pressed("w"):
            print("Touche 'up' détectée !")
            position_actuelle = robot.get_pose()
            nouvelle_position = position_actuelle
            nouvelle_position.x += 0.05
            robot.move_pose(nouvelle_position)
        elif keyboard.is_pressed("s"):
            print("Touche 'down' détectée !")
            position_actuelle = robot.get_pose()
            nouvelle_position = position_actuelle
            nouvelle_position.x -= 0.05
            robot.move_pose(nouvelle_position)

        #ouvre ferme pince
        elif keyboard.is_pressed("1"):
            print("Touche '1' détectée ! Ouverture de la pince")
            robot.open_gripper()
        elif keyboard.is_pressed("0"):
            print("Touche '0' détectée ! Fermeture de la pince")
            robot.close_gripper()

        #Rotation pince
        elif keyboard.is_pressed("7"):
            print("Touche '7' détectée ! Ouverture de la pince")

            position_actuelle = robot.get_pose()
            position_actuelle.roll -= 0.2
            robot.move_pose(position_actuelle)
        elif keyboard.is_pressed("9"):
            print("Touche '9' détectée ! Ouverture de la pince")
            position_actuelle = robot.get_pose()
            position_actuelle.roll += 0.2
            robot.move_pose(position_actuelle)


        #Convoyeur
        elif keyboard.is_pressed("right"):
            print("Touche 'right' détectée ! Mouvement du convoyeur")
            robot.run_conveyor(ConveyorID.ID_1, 100, ConveyorDirection.BACKWARD)

        elif keyboard.is_pressed("left"):
            print("Touche 'left' détectée ! Mouvement du convoyeur")
            robot.run_conveyor(ConveyorID.ID_1, 100, ConveyorDirection.FORWARD)

        elif keyboard.is_pressed("x"):
            print("Touche 'x' détectée ! Mouvement du convoyeur")
            robot.stop_conveyor(convoyeur_id)




except KeyboardInterrupt:
    print("Programme terminé.")
    robot.disconnect()
    robot.unset_conveyor(convoyeur_id)




#Fin du code ( sortie et déconnexion )
robot.set_learning_mode(True)
robot.close_connection()