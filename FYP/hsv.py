#!python2


# import the necessary packages:
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui

class hsv():	
	def getImage(self):
		try:
			#Opening an image from a file:
			file = easygui.fileopenbox()
			image = cv2.imread(file)
			person = self.findperson(image)
			
			#reverse = cv2.bitwise_not(person)
			ROI = cv2.bitwise_and(image,image,mask=person)
			
			person,contours,_ = cv2.findContours(person,mode=cv2.RETR_EXTERNAL,method=cv2.CHAIN_APPROX_NONE)
			test = cv2.drawContours(image, contours, -1, (0,255,0), 3)
			
			print(len(contours))
			
			face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
			gray = cv2.cvtColor(ROI, cv2.COLOR_BGR2GRAY)
			faces = face_cascade.detectMultiScale(gray, 1.3, 5)
			print(len(faces))
			for (x,y,w,h) in faces:
				ROI = cv2.rectangle(ROI,(x,y),(x+w,y+h),(255,0,0),2)

			
			cv2.imwrite('ROI.jpg', test)
			cv2.imwrite('skin.jpg', ROI)
		except:
			print("User failed to select an image.")

	
	# https://www.learnopencv.com/color-spaces-in-opencv-cpp-python/
	def findperson(self, image):
		higher = np.array([255,255,255])
		lower = np.array([0,40,80])
		
		HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		
		tone = cv2.inRange(HSV, lower, higher)
		shape = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(40,40))
		erosion = cv2.erode(tone, shape)
		dilation = cv2.dilate(erosion, shape)
		openMask = cv2.morphologyEx(dilation,cv2.MORPH_OPEN,shape)
		closedMask = cv2.morphologyEx(openMask,cv2.MORPH_CLOSE,shape)
		return closedMask

		
if __name__ == "__main__":
	person = hsv()
	person.getImage()
	