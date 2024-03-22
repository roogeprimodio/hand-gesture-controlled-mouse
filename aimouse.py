import cv2
import numpy as np
import mediapipe as mp
import pyautogui
import time
from logging import getLogger, basicConfig, INFO

basicConfig(level=INFO)

log = getLogger("AI Mouse")
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
)


def move_mouse(x, y):
    screen_width, screen_height = pyautogui.size()
    mouse_x = int((1 - x) * screen_width)
    mouse_y = int(y * screen_height)
    pyautogui.moveTo(mouse_x, mouse_y)
    log.info(f"Cursor position: ({mouse_x}, {mouse_y})")


def main():
    cap = cv2.VideoCapture(0)
    start_time = time.time()
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (320, 240))
        frame_count += 1

        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                landmarks = hand_landmarks.landmark
                h, w, c = frame.shape
                index_tip = (int(landmarks[8].x * w), int(landmarks[8].y * h))
                middle_tip = (int(landmarks[12].x * w), int(landmarks[12].y * h))

                if np.linalg.norm(np.array(index_tip) - np.array(middle_tip)) < 30:
                    pyautogui.click(button="left")

                cv2.circle(frame, index_tip, 5, (0, 255, 0), cv2.FILLED)
                cv2.circle(frame, middle_tip, 5, (0, 255, 0), cv2.FILLED)

                move_mouse(landmarks[8].x, landmarks[8].y)

        fps = frame_count / (time.time() - start_time)
        cv2.putText(
            frame,
            f"FPS: {round(fps, 2)}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
            cv2.LINE_AA,
        )
        frame_count = 0
        start_time = time.time()

        cv2.imshow("AI Mouse", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


main()
