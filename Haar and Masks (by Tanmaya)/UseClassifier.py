#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 06:21:56 2016

@author: tanmaya
"""

def fu():
	cas=cv2.CascadeClassifier("/home/tanmaya/opencv-haar-classifier-training/classifier/cascade.xml")
	for img in l:
		x2=cv2.imread("/home/tanmaya/Documents/Image Processing Project/Grayscale2/"+img,0)
		z = cas.detectMultiScale(x2)
		for (x,y,w,h) in z:
			  cv2.rectangle(x2,(x,y),(x+w,y+h),(255,255,255),2)
		cv2.imwrite("/home/tanmaya/Final2/"+img, x2)

fu()