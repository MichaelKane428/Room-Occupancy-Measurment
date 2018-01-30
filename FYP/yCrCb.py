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
			
			#reverse = cv2.bitwise_not(person)
			ROI = cv2.bitwise_and(image,image,mask=person)
			
			person,contours,_ = cv2.findContours(person,mode=cv2.RETR_EXTERNAL,method=cv2.CHAIN_APPROX_NONE)
			test = cv2.drawContours(image, contours, -1, (0,255,0), 3)
			
			cv2.imwrite('ROI.jpg', test)
			cv2.imwrite('skin.jpg', ROI)
		except:
			print("User failed to select an image.")
		# while True:
			##Showing an image on the screen (OpenCV):
			# cv2.imshow("Person", test)
			# key = cv2.waitKey(0)

			##if the 'q' key is pressed, quit:
			# if key == ord("q"):
				# break
	
	# http://opencv-users.1802565.n2.nabble.com/how-to-do-skin-detection-using-ycbcr-color-space-opencv-c-code-in-ubuntu-td7584779.html
	# http://academic.aua.am/Skhachat/Public/Papers%20on%20Face%20Detection/Survey%20on%20Skin%20Color%20Techniques.pdf
	# https://docs.opencv.org/2.4/modules/imgproc/doc/miscellaneous_transformations.html
	# https://www.learnopencv.com/color-spaces-in-opencv-cpp-python/
	def findperson(self, image):
		higher = np.array([255,185,135])
		lower = np.array([80,135,85])
		
		yCrCb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
		
		tone = cv2.inRange(yCrCb, lower, higher)
		shape = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(40,40))
		erosion = cv2.erode(tone, shape)
		dilation = cv2.dilate(erosion, shape)
		openMask = cv2.morphologyEx(dilation,cv2.MORPH_OPEN,shape)
		closedMask = cv2.morphologyEx(openMask,cv2.MORPH_CLOSE,shape)
		return closedMask

		
if __name__ == "__main__":
	person = test()
	person.getImage()
	