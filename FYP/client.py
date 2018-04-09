#!python2

# webserver curl -F "file=@/Users/michaelkane/Desktop/blackSignature.png" http://192.168.0.15:5000/upload/"
# import the necessary packages:
# references: https://gist.github.com/yoavram/4351498
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui
import requests
import base64
import datetime

class client():
	def getImage(self):
		url = "http://michaelkanefyp.dynu.net:5000/upload/"
		temp = str(datetime.datetime.now())
		date = temp.replace(":", "-")
		date = date.replace(" ", "_")
		date = date[0:19]
		image = cv2.imread('test2.jpg')
		cv2.imwrite(date +'.jpg', image)
		fin = open(date +'.jpg', "rb")
		#encoded_image = base64.b64encode(fin.read())
		files={'file': fin}

		try:
			r = requests.post(url, files=files, data={'number_of_people': '700'})
			print (r.text)
		finally:
			fin.close()

	def postImage(self):
		pass

	def findPeople(self):
		pass

	def countPeople(self):
		pass

if __name__ == "__main__":
	result = client()
	result.getImage()

#http://docs.python-requests.org/en/latest/user/quickstart/#post-a-multipart-encoded-file

# url = "http://michaelkanefyp.dynu.net"
# with open('References.txt', 'rb') as f: r = requests.post("http://78.18.97.94:5000", file={'References.txt': f})
# print r.text
	