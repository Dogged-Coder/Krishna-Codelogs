import cv2
import mediapipe as mp
import pyautogui
import time
import math

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()

prev_x, prev_y = 0, 0
smoothening = 3  # Higher = smoother
dragging = False

def euclidean(p1, p2):
    return math.hypot(p2[0]-p1[0], p2[1]-p1[1])

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    h, w, c = img.shape

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((cx, cy))

            # Draw the hand
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            if lm_list:
                index_finger = lm_list[8]
                thumb_tip = lm_list[4]
                middle_tip = lm_list[12]
                ring_tip = lm_list[16]

                # Cursor movement
                x, y = index_finger
                screen_x = int((x / w) * screen_w)
                screen_y = int((y / h) * screen_h)

                # Smooth movement
                cur_x = prev_x + (screen_x - prev_x) // smoothening
                cur_y = prev_y + (screen_y - prev_y) // smoothening
                pyautogui.moveTo(cur_x, cur_y)
                prev_x, prev_y = cur_x, cur_y

                # Gesture Detection
                pinch_distance = euclidean(index_finger, thumb_tip)
                peace_distance = euclidean(thumb_tip, ring_tip)
                ring_distance = euclidean(index_finger, ring_tip)

                # Left Click (Pinch)
                if pinch_distance < 40:
                    cv2.putText(img, 'Left Click 👌', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)
                    pyautogui.click()
                    time.sleep(1)

                # Right Click (Peace Pinch)
                elif peace_distance < 40:
                    cv2.putText(img, 'Right Click ✌️', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)
                    pyautogui.click(button='right')
                    time.sleep(1)

                # Fist (Start Drag)
                elif all([ euclidean(index_finger, middle_tip) < 30,
                    euclidean(index_finger, ring_tip) < 30,
                    euclidean(index_finger, thumb_tip) > 50 ]):
                    if not dragging:
                        pyautogui.mouseDown()
                        dragging = True
                        cv2.putText(img, 'Dragging ✊', (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255), 2)

                # Open Hand (Release Drag)
                elif dragging:
                    if pinch_distance > 80 and peace_distance > 80 and ring_distance > 80:
                        pyautogui.mouseUp()
                        dragging = False
                        cv2.putText(img, 'Released ✋', (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    cv2.imshow("🖥️ Krishna's JARVIS Mouse", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break