#!python2

# webserver curl -F "file=@/Users/michaelkane/Desktop/blackSignature.png" http://192.168.0.15:5000/"
# import the necessary packages:
# references: https://gist.github.com/yoavram/4351498
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui
import requests
import base64
class roomOccupancy():
	
	
	
	def getImage(self):
		url = "http://78.18.97.94:5000/"
		image = cv2.imread('test2.jpg')
		cv2.imwrite('test.jpg', image)
		
		fin = open('test.jpg', "rb")
		encoded_image = base64.b64encode(fin.read())
		files={'file': fin}
		
		try:
			r = requests.post(url, files=files)
			print r.text
		finally:
			fin.close()

if __name__ == "__main__":
	result = roomOccupancy()
	result.getImage()

#http://docs.python-requests.org/en/latest/user/quickstart/#post-a-multipart-encoded-file

# url = "http://michaelkanefyp.dynu.net"
# with open('References.txt', 'rb') as f: r = requests.post("http://78.18.97.94:5000", file={'References.txt': f})
# print r.text
	