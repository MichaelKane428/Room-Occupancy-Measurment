#!python2

import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui

class test():
	def getImage(self):
		file = easygui.fileopenbox()
		image = cv2.imread(file)
		
		#grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		#grayScale = cv2.bitwise_not(grayScale)
		grayScaleMask = cv2.threshold(image, 50, 150, cv2.THRESH_BINARY)[1]
		#threshold = cv2.bitwise_not(threshold)
		# grayScaleMask = cv2.adaptiveThreshold(grayScale, maxValue = 255,
		# adaptiveMethod = cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
		# thresholdType = cv2.THRESH_BINARY,
		# blockSize = 11,C = 30)
		cv2.imwrite('threshold.jpg', grayScaleMask)
		
		while True:
			cv2.imshow("Signature", grayScaleMask)
			key = cv2.waitKey(0)
			# if the 'q' key is pressed, quit:
			if key == ord("q"):
				break
		
			

if __name__ == "__main__":
	result = test()
	result.getImage()