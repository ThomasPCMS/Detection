
import cv2
import numpy as np
import time

vid = cv2.VideoCapture(0)

def count_color(frame):
    h,w,c = frame.shape
    c=0
    for x in range(w):
        for y in range(h):
            if frame[y,x,0] != 0 and frame[y,x,1] != 0 and frame[y,x,1] != 0:
                c+=1
    return c

def detect_color(frame):
    _frame = cv2.resize(frame, (40, 30))
    hsv_frame = cv2.cvtColor(_frame, cv2.COLOR_BGR2HSV)
    clist = []

    low_red = np.array([120, 254, 200])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(_frame, _frame, mask=red_mask)
    print(f"c(red) : {count_color(red)}")
    clist.append([count_color(red),"red"])

    low_orange = np.array([5, 75, 0])
    high_orange = np.array([21, 255, 255])
    orange_mask = cv2.inRange(hsv_frame, low_orange, high_orange)
    orange = cv2.bitwise_and(_frame, _frame, mask=orange_mask)
    clist.append([count_color(orange), "orange"])

    low_yellow = np.array([22, 93, 0])
    high_yellow = np.array([35, 255, 255])
    yellow_mask = cv2.inRange(hsv_frame, low_yellow, high_yellow)
    yellow = cv2.bitwise_and(_frame, _frame, mask=yellow_mask)
    clist.append([count_color(yellow), "yellow"])
    # Green color
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(_frame, _frame, mask=green_mask)
    clist.append([count_color(green), "green"])

    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(_frame, _frame, mask=blue_mask)
    print(f"c(blue) : {count_color(blue)}")
    clist.append([count_color(blue), "blue"])

    low_purple = np.array([133, 43, 46])
    high_purple = np.array([155, 255, 255])
    purple_mask = cv2.inRange(hsv_frame, low_purple, high_purple)
    purple = cv2.bitwise_and(_frame, _frame, mask=purple_mask)

    low = np.array([0,0,0])
    high = np.array([179,100,130])
    black_mask = cv2.inRange(hsv_frame, low, high)
    black = cv2.bitwise_and(_frame, _frame, mask=black_mask)
    clist.append([count_color(black), "black"])

    lower_white = np.array([0,0,168])
    upper_white = np.array([172,111,255])
    mask = cv2.inRange(hsv_frame, lower_white, upper_white)
    white = cv2.bitwise_and(_frame, _frame, mask=mask)
    clist.append([count_color(white), "white"])

    lower_gray = np.array([0, 0, 168])
    upper_gray = np.array([172, 111, 255])
    mask = cv2.inRange(hsv_frame, lower_gray, upper_gray)
    gray = cv2.bitwise_and(_frame, _frame, mask=mask)
    clist.append([count_color(gray), "gray"])
    print(sorted(clist,reverse=True))
    return sorted(clist,reverse=True)[0][1]

#h 角度，v 濃度，s 深淺
while True:
    ret, frame = vid.read()
    #print(frame.shape)
    _frame = cv2.resize(frame, (320, 240))
    #_frame = frame.copy()
    hsv_frame = cv2.cvtColor(_frame, cv2.COLOR_BGR2HSV)

    low_purple = np.array([130, 43, 46])
    high_purple = np.array([145, 255, 255])
    purple_mask = cv2.inRange(hsv_frame, low_purple, high_purple)
    purple = cv2.bitwise_and(_frame, _frame, mask=purple_mask)


    low = np.array([0, 0, 0])
    high = np.array([179, 100, 130])
    black_mask = cv2.inRange(hsv_frame, low, high)
    black = cv2.bitwise_and(_frame, _frame, mask=black_mask)

    lower_white = np.array([0, 0, 168])
    upper_white = np.array([172, 111, 255])
    #lower = np.array([0, 0, 0])
    #upper = np.array([255, 10, 255])
    mask = cv2.inRange(hsv_frame, lower_white, upper_white)
    white = cv2.bitwise_and(_frame, _frame, mask=mask)

    low_orange = np.array([5, 25, 0])
    high_orange = np.array([21, 255, 255])
    orange_mask = cv2.inRange(hsv_frame, low_orange, high_orange)
    orange = cv2.bitwise_and(_frame, _frame, mask=orange_mask)

    low_yellow = np.array([22, 93, 0])
    high_yellow = np.array([33, 255, 255])
    yellow_mask = cv2.inRange(hsv_frame, low_yellow, high_yellow)
    yellow = cv2.bitwise_and(_frame, _frame, mask=yellow_mask)

    low_green = np.array([34, 0, 0])
    high_green = np.array([94, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(_frame, _frame, mask=green_mask)

    low_red = np.array([156, 43, 46])
    high_red = np.array([180, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(_frame, _frame, mask=red_mask)

    low_blue = np.array([94, 10, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(_frame, _frame, mask=blue_mask)

    lower_gray = np.array([0, 0, 50])
    upper_gray = np.array([255, 50, 150])
    mask = cv2.inRange(hsv_frame, lower_gray, upper_gray)
    gray = cv2.bitwise_and(_frame, _frame, mask=mask)

    cv2.imshow("Red", red)
    cv2.imshow("orange", orange)
    cv2.imshow("yellow",yellow)
    cv2.imshow("Green", green)
    cv2.imshow("Blue", blue)
    cv2.imshow("purple", purple)
    #cv2.imshow("pink", pink)
    cv2.imshow("Black", black)
    cv2.imshow("White",white)
    cv2.imshow("gray",gray)
    #cv2.imshow("_frame",_frame)
    key = cv2.waitKey(1)
    if key == 27 or key == 32:
        break
    time.sleep(0.1)


