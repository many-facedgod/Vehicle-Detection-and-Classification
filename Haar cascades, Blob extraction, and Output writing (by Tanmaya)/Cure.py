#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 17:32:57 2016

@author: tanmaya
"""

#Puts a threshold on the area of the connected components.

import numpy as np
import cv2

def cure(a):
    x,y=a.shape
    for i in xrange(x):
        for j in xrange(y):
            val=a[i][j]
            if  np.abs(val-255)>np.abs(val-0):
                a[i][j]=0
            else:
                a[i][j]=255

for i in xrange(0, 1538):
    p=cv2.imread("/home/tanmaya/Documents/Image Processing Project/Masks/"+str(i)+".pgm", 0)
    #cure(p)
    _,c,_=cv2.findContours(p,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)	
    p=np.zeros(p.shape, dtype=p.dtype)
    y=filter(lambda c: cv2.contourArea(c)>150, c)
    cv2.drawContours(p, y, -1, (255,255,255), -1)
    cv2.imwrite("/home/tanmaya/Masks/"+str(i)+".pgm",p)
