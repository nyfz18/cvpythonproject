import cv2
import pytesseract

#setting tesseract path
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
imgC = cv2.imread('canterville.jpg')
imgC = cv2.cvtColor(imgC, cv2.COLOR_BGR2RGB)
#print(pytesseract.image_to_string(img))

#Detecting Characters
hImg,wImg,_ = imgC.shape
boxes = pytesseract.image_to_boxes(imgC)
for b in boxes.splitlines():
    b = b.split()
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(imgC,(x,hImg-y),(w,hImg-h),(0,0,255),1)
    cv2.putText(imgC,b[0],(x,hImg-y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),1)

cv2.imshow('Result',imgC)
cv2.waitKey(0)