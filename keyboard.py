import cv2
import numpy as np
import time

img1 = cv2.imread("Image/test01.png")
img2 = cv2.imread("Image/test01-2.jpg")
img1_title, img1_subtitle, content1_1, content1_2, pic1_1, pic1_2 = img1[55:155, 0:850], img1[165:230, 0:835], \
                                                                    img1[230:415, 405:845], img1[420:605, 575:850], \
                                                                    img1[230:600, 10:365], img1[420:600, 370:570]
img2_title, img2_subtitle, content2_1, content2_2, pic2_1, pic2_2 = img2[55:155, 0:850], img2[165:230, 0:835], \
                                                                img2[230:415, 405:845], img2[420:605, 575:850], \
                                                                img2[230:600, 10:365], img2[420:600, 370:570]


while True:
    key = cv2.waitKey(1)
    # print(key)
    if key == ord('q'):
        for i in np.linspace(0, 1, 1000):
            alpha = i
            beta = 1 - alpha
            output = cv2.addWeighted(img2_title, alpha, img1_title, beta, 0)
            img1[55:output.shape[0]+55, 0:output.shape[1]] = output
            cv2.imshow('pic1', img1)
            time.sleep(0.01)
            cv2.waitKey(1)
            if alpha >= 0.09:
                alpha = 1
                break
            # print(alpha)

    elif key == ord('a'):
        for i in np.linspace(0, 1, 1000):
            alpha = i
            beta = 1 - alpha
            output = cv2.addWeighted(img2_subtitle, alpha, img1_subtitle, beta, 0)
            img1[165:output.shape[0] + 165, 0:output.shape[1]] = output
            cv2.imshow('pic1', img1)
            time.sleep(0.01)
            cv2.waitKey(1)
            if alpha >= 0.09:
                alpha = 1
                break
    elif key == ord('w'):
        for i in np.linspace(0, 1, 1000):
            alpha = i
            beta = 1 - alpha
            output = cv2.addWeighted(content2_1, alpha, content1_1, beta, 0)
            img1[230:output.shape[0] + 230, 405:output.shape[1]+405] = output
            cv2.imshow('pic1', img1)
            time.sleep(0.01)
            cv2.waitKey(1)
            if alpha >= 0.09:
                alpha = 1
                break
    elif key == ord('s'):
        for i in np.linspace(0, 1, 1000):
            alpha = i
            beta = 1 - alpha
            output = cv2.addWeighted(content2_2, alpha, content1_2, beta, 0)
            img1[420:output.shape[0] + 420, 575:output.shape[1]+575] = output
            cv2.imshow('pic1', img1)
            time.sleep(0.01)
            cv2.waitKey(1)
            if alpha >= 0.09:
                alpha = 1
                break
    elif key == ord('e'):
        for i in np.linspace(0, 1, 1000):
            alpha = i
            beta = 1 - alpha
            output = cv2.addWeighted(pic2_1, alpha, pic1_1, beta, 0)
            img1[230:output.shape[0] + 230, 10:output.shape[1]+10] = output
            cv2.imshow('pic1', img1)
            time.sleep(0.01)
            cv2.waitKey(1)
            if alpha >= 0.09:
                alpha = 1
                break
    elif key == ord('d'):
        for i in np.linspace(0, 1, 1000):
            alpha = i
            beta = 1 - alpha
            output = cv2.addWeighted(pic2_2, alpha, pic1_2, beta, 0)
            img1[420:output.shape[0] + 420, 370:output.shape[1]+370] = output
            cv2.imshow('pic1', img1)
            time.sleep(0.01)
            cv2.waitKey(1)
            if alpha >= 0.09:
                alpha = 1
                break

    cv2.imshow("pic1", img1)

    # cv2.waitKey(1)


