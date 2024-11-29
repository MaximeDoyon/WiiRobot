import threading

import cv2
from pyniryo import *
import time
import keyboard
import numpy as np
ip_robot_address = "10.4.1.51"

robot = NiryoRobot(ip_robot_address)
robot.calibrate_auto()
robot.update_tool()

au_dessus_plateforme = (-0.029,-0.178,0.428,-2.053,1.481,2.489)
convoyeur_id = robot.set_conveyor()
robot.move_pose(*au_dessus_plateforme)

mutex = threading.Lock()


def display_robot_vision():

    while True:
        try:
            with mutex:
                frame = robot.get_img_compressed()

            # Convertir les données brutes en tableau NumPy
            np_frame = np.frombuffer(frame, dtype=np.uint8)

            # Décoder les données en image
            image = cv2.imdecode(np_frame, cv2.IMREAD_COLOR)
            if image is None:  # Vérifiez si la décompression a échoué
                raise ValueError("Impossible de décoder l'image.")
            # Afficher l'image dans la fenêtre
            cv2.imshow("Vision en temps réel du robot Niryo", image)
            time.sleep(1)
            # Appuyer sur 't' pour quitter l'affichage
            if cv2.waitKey(1) & 0xFF == ord('t'):
                break

        except (NiryoRobotException, ValueError) as e:
            print(f"Erreur lors de l'affichage de la vision : {e}")
            break

    # Détruire la fenêtre après la boucle
    cv2.destroyWindow("Vision en temps réel du robot Niryo")

# Démarrage du thread pour la vision
# vision_thread = threading.Thread(target=display_robot_vision, daemon=True)
# vision_thread.start()


try:
    while True:
        #Move up and down
        if keyboard.is_pressed("up"):
            print("Touche 'w' détectée ! Montée du robot...")
            with mutex:

                position_actuelle = robot.get_pose()
                nouvelle_position = position_actuelle
                nouvelle_position.z += 0.05
                robot.move_pose(nouvelle_position)

        elif keyboard.is_pressed("down"):
            print("Touche 's' détectée ! Descente du robot...")
            with mutex:
                position_actuelle = robot.get_pose()
                nouvelle_position = position_actuelle
                nouvelle_position.z -= 0.05
                robot.move_pose(nouvelle_position)
        elif keyboard.is_pressed("n"):
            try:
                frame = robot.get_img_compressed()
                np_frame = np.frombuffer(frame, dtype=np.uint8)
                image = cv2.imdecode(np_frame, cv2.IMREAD_COLOR)
                if image is None:
                    raise ValueError("Impossible de décoder l'image.")

                # Afficher l'image dans une fenêtre
                cv2.imshow("Photo", image)

                # Attendre une touche ou un délai pour éviter un "freeze"
                key = cv2.waitKey(0)  # 0 signifie attendre une touche (ferme la fenêtre si nécessaire)
                if key == ord('q'):  # Fermer sur la touche 'q'
                    cv2.destroyWindow("Photo")
            except ValueError as e:
                print(f"Erreur : {e}")


        #prendre objet
        elif keyboard.is_pressed("p"):
            with mutex:
                robot.move_pose(*au_dessus_plateforme)
            time.sleep(1)
            with mutex:
                detected_objects = robot.detect_object("workspace_plateform", ObjectShape.ANY, ObjectColor.ANY)
            if detected_objects:
                print("Objet trouvé ! Préparation à la récupération")
                with mutex:
                    obj_found, shape_ret, color_ret = robot.vision_pick("workspace_plateform", 0.005, ObjectShape.ANY, ObjectColor.ANY)
                with mutex:
                    robot.move_pose(au_dessus_plateforme)


        #Bouge profondeur
        elif keyboard.is_pressed("a"):
            print("Touche 'a' détectée !")
            with mutex:
                position_actuelle = robot.get_pose()
                nouvelle_position = position_actuelle
                nouvelle_position.y += 0.05
                robot.move_pose(nouvelle_position)
        elif keyboard.is_pressed("d"):
            print("Touche 'd' détectée !")
            with mutex:
                position_actuelle = robot.get_pose()
                nouvelle_position = position_actuelle
                nouvelle_position.y -= 0.05
                robot.move_pose(nouvelle_position)

        # Bouge gauche droite
        elif keyboard.is_pressed("w"):
            print("Touche 'up' détectée !")
            with mutex:
                position_actuelle = robot.get_pose()
                nouvelle_position = position_actuelle
                nouvelle_position.x += 0.05
                robot.move_pose(nouvelle_position)
        elif keyboard.is_pressed("s"):
            print("Touche 'down' détectée !")
            with mutex:
                position_actuelle = robot.get_pose()
                nouvelle_position = position_actuelle
                nouvelle_position.x -= 0.05
                robot.move_pose(nouvelle_position)

        #ouvre ferme pince
        elif keyboard.is_pressed("1"):
            print("Touche '1' détectée ! Ouverture de la pince")
            with mutex:
                robot.open_gripper()
        elif keyboard.is_pressed("0"):
            print("Touche '0' détectée ! Fermeture de la pince")
            with mutex:
                robot.close_gripper()

        #Rotation pince
        elif keyboard.is_pressed("q"):
            print("Touche '7' détectée ! Rotation de la pince")
            with mutex:
                position_actuelle = robot.get_pose()
                position_actuelle.roll -= 0.3
                robot.move_pose(position_actuelle)
        elif keyboard.is_pressed("e"):
            print("Touche '9' détectée ! Rotation de la pince")
            with mutex:
                position_actuelle = robot.get_pose()
                position_actuelle.roll += 0.3
                robot.move_pose(position_actuelle)


        #Convoyeur
        elif keyboard.is_pressed("right"):
            print("Touche 'right' détectée ! Mouvement du convoyeur")
            with mutex:
                robot.run_conveyor(ConveyorID.ID_1, 100, ConveyorDirection.BACKWARD)

        elif keyboard.is_pressed("left"):
            print("Touche 'left' détectée ! Mouvement du convoyeur")
            with mutex:
                robot.run_conveyor(ConveyorID.ID_1, 100, ConveyorDirection.FORWARD)

        elif keyboard.is_pressed("x"):
            print("Touche 'x' détectée ! Mouvement du convoyeur")
            with mutex:
                robot.stop_conveyor(convoyeur_id)




except KeyboardInterrupt:
    print("Programme terminé.")
    with mutex:
        robot.close_connection()
        robot.unset_conveyor(convoyeur_id)




#Fin du code ( sortie et déconnexion )
with mutex:
    robot.set_learning_mode(True)
    robot.close_connection()