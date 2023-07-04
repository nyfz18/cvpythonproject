from util import *
import pytesseract

#with original file, color so you can pick the highlighted, then contour it
#then use the binding box, then crop it to images and give to pytesseract
path = 'dummytext.jpg'
hsv = [0, 65, 59, 255, 0, 255]
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

imgHigh = cv2.imread(path)
imgResult = detectColor(imgHigh, hsv)
imgContours, contours = getContours(imgResult, imgHigh, showCanny=False,
                                    minArea= 1000, filter=4, cThr=[100,150],
                                    draw=True)
#print(len(contours))

roiList = getRoi(imgHigh, contours)
#roiDisplay(roiList)

highlightedTxt =[]
for x, roi in enumerate(roiList):
    highlightedTxt.append(pytesseract.image_to_string(roi))
saveText(highlightedTxt)