import time
import cv2
import numpy as np
from picamera2 import Picamera2

def main():
    print("Initialisation de la caméra sur Raspberry Pi 5...")
    
    # Création de l'instance Picamera2
    picam2 = Picamera2()

    # Configuration de la caméra
    # Nous demandons un format brut ou YUV qui sera converti pour l'affichage
    config = picam2.create_configuration(main={"size": (640, 480), "format": "RGB888"})
    picam2.configure(config)

    print("Démarrage de la prévisualisation...")
    picam2.start()

    # Boucle pour afficher le flux vidéo
    try:
        while True:
            # Capture une image sous forme de tableau (array) compatible OpenCV
            # wait=True attend que la prochaine image soit prête
            frame = picam2.capture_array()

            # Si votre caméra est nativement monochrome, l'image sera déjà en N&B.
            # Toutefois, libcamera peut parfois fournir un format RGB même pour une caméra Mono.
            # L'affichage ci-dessous montrera ce que la caméra voit réellement.
            
            cv2.imshow("Test Camera Noir & Blanc (Appuyez sur 'q' pour quitter)", frame)

            # Vérifie si l'utilisateur appuie sur 'q' pour quitter
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except Exception as e:
        print(f"Une erreur est survenue : {e}")

    finally:
        # Nettoyage propre des ressources
        picam2.stop()
        cv2.destroyAllWindows()
        print("Caméra arrêtée.")

if __name__ == "__main__":
    main()