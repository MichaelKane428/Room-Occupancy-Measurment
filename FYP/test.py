#!python2


# import the necessary packages:
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui

class test():	
	def getImage(self):
		try:
			#Opening an image from a file:
			file = easygui.fileopenbox()
			image = cv2.imread(file)
			person = self.findperson(image)
			reverse = cv2.bitwise_not(person)
			ROI = cv2.bitwise_and(image,image,mask=reverse)
			
			reverse,contours,_ = cv2.findContours(reverse,mode=cv2.RETR_EXTERNAL,method=cv2.CHAIN_APPROX_NONE)
			test = cv2.drawContours(image, contours, -1, (0,255,0), 3)
			
			cv2.imwrite('ROI.jpg', test)
		except:
			print("User failed to select an image.")
		while True:
			# Showing an image on the screen (OpenCV):
			cv2.imshow("Person", test)
			key = cv2.waitKey(0)

			# if the 'q' key is pressed, quit:
			if key == ord("q"):
				break
		
	def findperson(self, image):
		# Create a grayscale mask for the signature, then use morphology to isolate part of the signature. 
		grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		grayScaleHistogram = cv2.equalizeHist(grayScale)
		threshold = cv2.threshold(grayScaleHistogram, 200, 255, cv2.THRESH_BINARY)[1]
		threshold = cv2.bitwise_not(threshold)
		
		shape = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(10,10))
		openMask = cv2.morphologyEx(threshold,cv2.MORPH_OPEN,shape)
		closedMask = cv2.morphologyEx(openMask,cv2.MORPH_CLOSE,shape)
		return closedMask

		
if __name__ == "__main__":
	person = test()
	person.getImage()
	