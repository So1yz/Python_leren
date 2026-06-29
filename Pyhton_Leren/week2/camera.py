# Auteur: Yusuf Simsek
# Functie: Webcam openen

import cv2

camera = cv2.VideoCapture(0)

while True:
    succes, frame = camera.read()

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()