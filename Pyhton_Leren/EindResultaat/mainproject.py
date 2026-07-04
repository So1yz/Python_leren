# Auteur: Yusuf Simsek
# Functie: Gebaar herkennen

import cv2
import mediapipe as mp
import webbrowser
import time

# CAP_DSHOW hulp middel voor mijn windows camera als er een probleem is.
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not camera.isOpened():
    print("FOUT: kan de camera niet openen.")
    exit()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

draw = mp.solutions.drawing_utils

# Hoeveel seconden wachten voordat hetzelfde gebaar opnieuw een actie mag
# uitvoeren. Zonder dit zou hij 30x per seconde een nieuw tabblad openen
# zolang ik me hand omhoog hou
WACHTTIJD = 5.0
laatste_actie_tijd = 0

while True:
    succes, frame = camera.read()

    if not succes or frame is None:
        continue

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb)

    gebaar_dit_frame = None

    if result.multi_hand_landmarks:

        for hand in result.multi_hand_landmarks:

            draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

            punten = hand.landmark

            wijsvinger = punten[8]
            middelvinger = punten[12]
            ringvinger = punten[16]
            pink = punten[20]

            wijs_omhoog = wijsvinger.y < punten[6].y
            middel_omhoog = middelvinger.y < punten[10].y
            ring_omhoog = ringvinger.y < punten[14].y
            pink_omhoog = pink.y < punten[18].y

            if wijs_omhoog and middel_omhoog and not ring_omhoog and not pink_omhoog:
                gebaar_dit_frame = "youtube"

            elif pink_omhoog:
                gebaar_dit_frame = "google"

    # Voer de actie uit zolang het gebaar gezien wordt, maar niet vaker
    # dan 1x per WACHTTIJD seconden.
    nu = time.time()
    if gebaar_dit_frame and (nu - laatste_actie_tijd) > WACHTTIJD:

        if gebaar_dit_frame == "youtube":
            webbrowser.open("https://youtube.com")

        elif gebaar_dit_frame == "google":
            webbrowser.open("https://google.com")

        laatste_actie_tijd = nu

    # Laat op het scherm zien wat er open gaat / Tekst
    if gebaar_dit_frame:
        cv2.putText(frame, gebaar_dit_frame, (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Project", frame)

    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()
