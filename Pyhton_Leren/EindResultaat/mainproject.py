# Auteur: Yusuf Simsek
# Functie: Gebaar herkennen

import cv2
import mediapipe as mp
import webbrowser

camera = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

draw = mp.solutions.drawing_utils

opened = False

while True:
    succes, frame = camera.read()

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb)

    if result.multi_hand_landmarks:

        for hand in result.multi_hand_landmarks:

            draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

            punten = hand.landmark

            wijsvinger = punten[8]
            middelvinger = punten[12]

            if wijsvinger.y < punten[6].y and middelvinger.y < punten[10].y:

                if opened == False:
                    webbrowser.open("https://youtube.com")
                    opened = True

    cv2.imshow("Project", frame)

    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()