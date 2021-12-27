import cv2
import numpy as np
import pyautogui

cap = cv2.VideoCapture(0)

lower_yellow = np.array([22, 93, 0])
upper_yellow = np.array([45, 255, 255])
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])
previuos_y = 0

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    contours, hierarchy = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
    for c in contours:
        area = cv2.contourArea(c)
        if area > 50000:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
            if y < previuos_y:
                pyautogui.press('space')
            previuos_y = y
            # print(area)
            #cv2.drawContours(frame, c, -1, (0, 255, 0), 4)
    #cv2.imshow('mask', mask)
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
