#!python2

# webserver curl -F "file=@/Users/michaelkane/Desktop/blackSignature.png" http://192.168.0.15:5000/"
# import the necessary packages:
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui

class roomOccupancy():
	
	def getImage(self):
		try:
			image = cv2.imread(file)
			
		except:
			print("User failed to select an image.")
		while True:
			# Showing an image on the screen (OpenCV):
			cv2.imshow("Image", image)
			key = cv2.waitKey(0)

			# if the 'q' key is pressed, quit:
			if key == ord("q"):
				break

if __name__ == "__main__":
	result = roomOccupancy()
	result.getImage()
	