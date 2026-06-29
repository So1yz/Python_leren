# Auteur: Yusuf Simsek
# Functie: Zwart wit camera

import cv2

camera = cv2.VideoCapture(0)

while True:
    succes, frame = camera.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Gray", gray)

    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()