# Auteur: Yusuf Simsek
# Functie: Gebaar herkennen

import cv2
import mediapipe as mp
import webbrowser

# CAP_DSHOW helpt vaak tegen camera-problemen op Windows.
# Werkt dit niet, probeer dan gewoon cv2.VideoCapture(0)
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not camera.isOpened():
    print("FOUT: kan de camera niet openen. Check of een andere app de camera gebruikt,")
    print("of probeer cv2.VideoCapture(0) zonder CAP_DSHOW.")
    exit()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

draw = mp.solutions.drawing_utils

opened = False

while True:
    succes, frame = camera.read()

    # Belangrijk: als het lezen mislukt, sla dit frame gewoon over
    # in plaats van te crashen op een lege frame.
    if not succes or frame is None:
        print("Geen frame ontvangen van de camera, probeer opnieuw...")
        continue

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
