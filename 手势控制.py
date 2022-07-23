import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui
cap = cv2.VideoCapture(0)
cap.set(3, 500)  # 设置高度
cap.set(4, 500)  # 设置宽度
detector = HandDetector(detectionCon=0.7,maxHands=1)  # 设置阈值
flag=0;
flag2=0;
flag5=0;
a=0
b=0
c=0
a1=0
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    img= cv2.flip(img, 1)
    cv2.imshow("gestureHand", img)
    if hands:
        if(hands[0]['type'])=='Right':
            lmList = hands[0]['lmList']
            print(lmList[12])
            a,b,c=lmList[9]
            if(a1-a>30):
               pyautogui.keyDown('right')
            if(a-a1>30):
                   pyautogui.keyDown('left')  
            fingers = detector.fingersUp(hands[0])
            if fingers[1] == 1:
                flag=1
            if(flag==1 and fingers[1] == 0):
                print ("666")
                x,y=pyautogui.position()
                pyautogui.keyDown('down')
                flag=0
            if fingers[2] == 1:
                flag2=1
            if(flag2==1 and fingers[2] == 0):
                print ("666")
                x,y=pyautogui.position()
                pyautogui.keyDown('up')
                flag2=0 
            if fingers[4] == 1:
                flag5=1
            if(flag5==1 and fingers[4] == 0):
                print ("666")
                x,y=pyautogui.position()
                pyautogui.hotkey('alt','a')
                # for i in range(1,5):
                #     pyautogui.mouseDown()
                #     pyautogui.mouseUp()
                flag5=0 
            a1,b1,c1=lmList[9]
    if 27==cv2.waitKey(1):
        break
    if ord("q")==cv2.waitKey(1):
        print("555")
        
