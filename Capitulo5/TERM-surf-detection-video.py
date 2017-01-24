import cv2
import numpy as np
import sys

# ESTE CODIGO LO EJECUTAREMOS DESDE TEMRINAL: python3.5 TERM-surf-detection-video.py SURF 8000
alg = sys.argv[1]

def fd(algorithm):
    if algorithm == "SIFT":
        return cv2.xfeatures2d.SIFT_create()
    if algorithm == "SURF":
        return cv2.xfeatures2d.SURF_create(float(sys.argv[2]) if len(sys.argv) == 3 else 4000)

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fd_alg = fd(alg)
    keypoints, descriptor = fd_alg.detectAndCompute(gray_frame, None)
    cv2.drawKeypoints(image=frame, outImage=frame, keypoints=keypoints, flags=4, color=(51, 163, 236))
    cv2.imshow("Keypoints", frame)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()