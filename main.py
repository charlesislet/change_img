import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep

img1 = cv2.imread("Image/ex1.png")
img1_1, img1_2, img1_3, img1_4 = img1[0:281, 0:210], img1[0:281, 210:421], \
                                 img1[281:562, 0:210], img1[281:562, 210:421]
img2 = cv2.imread("Image/ex2.png")
newImg2 = cv2.resize(img2, (421, 562))

cap = cv2.VideoCapture(0)
cap.set(3, 720)
cap.set(4, 480)
x, y, h = 100, 50, 100
thickness = -1
text = ["1", "2", "3", "4"]
finalText = ""

detector = HandDetector(detectionCon=0.8)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)

    if lmList:
        color = (0, 0, 0)
        cursor = lmList[8]
        if x < cursor[0] < x + h and y < cursor[1] < y + h:
            # cv2.rectangle(img, (x, y), (x + h, y + h), (200, 0, 255), thickness)
            newImg2[0:281, 0:210] = img1_1
            finalText += text[0]
            sleep(0.5)
        if x + h < cursor[0] < x + 2 * h and y < cursor[1] < y + h:
            # cv2.rectangle(img, (x + h, y), (x + 2 * h, y + h), (200, 0, 0), thickness)
            newImg2[0:281, 210:421] = img1_2
            finalText += text[1]
            sleep(0.5)
        if x < cursor[0] < x + h and y + h < cursor[1] < y + 2 * h:
            # cv2.rectangle(img, (x, y + h), (x + h, y + 2 * h), (0, 0, 200), thickness)
            newImg2[281:562, 0:210] = img1_3
            finalText += text[2]
            sleep(0.5)
        if x + h < cursor[0] < x + 2 * h and y + h < cursor[1] < y + 2 * h:
            # cv2.rectangle(img, (x + h, y + h), (x + 2 * h, y + 2 * h), (0, 100, 0), thickness)
            newImg2[281:562, 210:421] = img1_4
            finalText += text[3]
            sleep(0.5)

    cv2.rectangle(img, (x, y), (x + h, y + h), (255, 0, 255), thickness)
    cv2.rectangle(img, (x + h, y), (x + 2 * h, y + h), (255, 0, 0), thickness)
    cv2.rectangle(img, (x, y + h), (x + h, y + 2 * h), (0, 0, 255), thickness)
    cv2.rectangle(img, (x + h, y + h), (x + 2 * h, y + 2 * h), (0, 255, 0), thickness)
    cv2.putText(img, text[0], (150, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)
    cv2.putText(img, text[1], (250, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)
    cv2.putText(img, text[2], (150, 200), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)
    cv2.putText(img, text[3], (250, 200), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)
    cv2.putText(img, finalText, (100, 400), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)

    cv2.imshow("Image", img)
    cv2.imshow("pic", newImg2)
    cv2.waitKey(1)
