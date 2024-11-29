
# :warning: **Mises en garde**

:no_entry_sign: Ne pas se tenir dans la zone d'opération du robot  
:no_entry_sign: Dégagez l'espace d'opération du robot de tout obstacle pour éviter des collisions qui pourraient endommager le robot ou son environnement   
:no_entry_sign: En relâchant le bouton A de la manette de Wii, tout mouvement du bras robotisé est stoppé     
:no_entry_sign: Le bras robotisé bougera en fonction du mouvement de la manette de Wii ( lorsque le bouton A est maintenu enfoncé)    
# Étapes de fonctionnement du programme
   ## 1. Installation librairies (Toujours dans votre environnement virtuel)
   - Installer les bibliothèques Bluetooth :
   ```bash
   sudo apt-get install bluetooth libbluetooth-dev
   ```
   - Installer pybluez :
   ```bash
   pip install git+https://github.com/pybluez/pybluez.git
   ```
   - Installer les dépendances
   ```bash
   pip install -r requirements.txt
   ```
   
   
   ## 2. Étapes pour se connecter au robot avec la manette de Wii
   
   1. Démarrer le programme `main.py` (Le fichier `RobotController.py` est pour le contrôler avec un clavier et le fichier `reset.py` est simplement pour remettre le robot en Learning mode a partir de code)
   2. Appuyez sur le bouton 1 et 2 sur la manette de Wii simultanément.
   3. Lorsque les lumières sur la manette de Wii clignotent, appuyez sur Enter sur le clavier (Dans la console du programme)
   4. Patientez le temps que la manette de Wii se connecte (les lumières cesseront de clignoter et seule la première lumière restera allumée)
   
   
   ## 3. Étapes pour faire fonctionner le robot (Pince et convoyeur)
   1. Lorsque vous êtes connecté au robot avec les étapes précédentes, positionnez-vous à coté du robot à distance sécuritaire.
   2. Orientez-vous à 90° vers la droite du robot, de sorte à être parallèle au robot lorsque son bras est sur la plateforme.
   3. Commencez par un test simple et appuyez sur 1 ou 2 et maintenez ces boutons pour activer le convoyeur et s'assurer que tout fonctionne.
   4. Le relâchement de 1 ou 2 stoppe le convoyeur.
   5. Un clic sur le bouton + ou - ouvre et ferme la pince.
   ## 4. Étapes pour faire fonctionner le robot (Mouvement du bras)
   1. Placez la manette de Wii pour qu'elle pointe vers le ciel le plus droit possible.
   2. ***Attention, la prochaine étape fera bouger le bras robotisé***
   3. Appuyez et maintenez enfoncé le bouton A de la manette et le bras se déplacera dans la direction vers laquelle la manette de Wii est inclinée.
   4. Pour faire monter et descendre la hauteur de la pince, un clic et maintien de la flèche du haut ou du bas fera cette action.
   5. Pour faire une rotation de la pince, il suffit d'appuyer et maintenir les flèches de gauche ou droite.
# Erreur possibles :x:
- Forcer le robot à se déplacer vers une zone "out of bound" fera stopper le programme. Vous devrez recommencer les étapes pour connecter la manette de Wii (Étape 2)
- Une collision avec un obstacle pourrait briser le robot et même stopper le programme par le fait même.

   




    
