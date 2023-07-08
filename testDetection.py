import cv2
import pytesseract
from tkinter import Tk
from tkinter.filedialog import askopenfilename

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

Tk().withdraw()

image_path = askopenfilename(title="Select Image File",
                             filetypes=[("Image Files", ("*.png", "*.jpg", "*.jpeg", "*.bmp"))])

if image_path:
    img = cv2.imread(image_path)
    #img = cv2.imread('test.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#print(pytesseract.image_to_string(img))

#Detecting Characters
#hImg,wImg,_ = img.shape
#boxes = pytesseract.image_to_boxes(img)
#for b in boxes.splitlines():
    #b = b.split(' ')
    #x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    #cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),1)
    #cv2.putText(img,b[0],(x,hImg-y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),1)

#Detecting Words
hImg,wImg,_ = img.shape
boxes = pytesseract.image_to_data(img)
for x,b in enumerate(boxes.splitlines()):
    if x!=0:
        b = b.split() #separate by whitespace

        if len(b)==12:
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),1)
            cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),1)


cv2.imshow('Result',img)
cv2.waitKey(0)

