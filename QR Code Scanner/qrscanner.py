import cv2
from pyzbar.pyzbar import decode
import time

# create a variable, amd ask the opencv module to make a video capture function work for us
cam = cv2.VideoCapture(0)
cam.set(5, 640)
cam.set(6, 480)

camera = True
while camera == True:
    success, frame = cam.read()
    
    for i in decode(frame):
        print(i.type)
        print(i.data.decode('utf-8'))
        time.sleep(6)
        
        cv2.imshow("QR_Scanner", frame)
        cv2.waitKey(3)  # Capture the frame after 3sec
        
        