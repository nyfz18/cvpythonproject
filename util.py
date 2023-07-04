import cv2
import numpy as np

def detectColor(img, hsv):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([hsv[0], hsv[2], hsv[4]]) #lower range, color threshold
    upper = np.array([hsv[1], hsv[3], hsv[5]]) #upper range
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)
    return imgResult

def getContours(img, imgDraw, cThr=[100,100], showCanny=False, minArea=1000, filter=0, draw=False):
    imgDraw = imgDraw.copy()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5,5), 1) #preserve edges, avoid noise
    imgCanny = cv2.Canny(imgBlur, cThr[0], cThr[1])
    kernel = np.array((10,10))
    imgDial = cv2.dilate(imgCanny, kernel, iterations=1) #increse thickness
    imgClose = cv2.morphologyEx(imgDial, cv2.MORPH_CLOSE, kernel) #close gaps

    if showCanny:
        cv2.imshow('Canny',imgClose) #retr_external: external contours for bbox; contours approx
    contours, hierarchy = cv2.findContours(imgClose, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    finalContours = []
    for i in contours:
        area = cv2.contourArea(i)
        if area > minArea: #avoid noise
            perimeter = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02*perimeter, True)
            bbox = cv2.boundingRect(approx)
            #if filter > 0:
                #if len(approx) == filter: #only want our filters
                    #finalContours.append([len(approx), area, approx, bbox, i])
            #else: #just add everything
            finalContours.append([len(approx), area, approx, bbox, i])

    if draw:
        for cons in finalContours:
            x,y,w,h = cons[3] #bounding box
            cv2.rectangle(imgDraw, (x,y), (x+w, y+h), (255, 0, 255), 2)

    return imgDraw, finalContours

def getRoi(img, contours): #region of interest
    roiList = []
    for con in contours:
        x,y,w,h = con[3] #bbox
        roiList.append(img[y:y+h, x:x+w])
    return roiList

def roiDisplay(roiList):
    for x, roi in enumerate(roiList):
        roi = cv2.resize(roi, (0,0), None, 2,2)
        cv2.imshow(str(x), roi)

def saveText(highlightedTxt):
    with open('HighlightedTxt.csv', 'w') as f:
        for text in highlightedTxt:
            f.writelines(f'\n{text}')
