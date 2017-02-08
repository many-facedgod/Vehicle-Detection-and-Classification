#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 18:09:46 2016

@author: tanmaya
"""

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


f=open("/home/tanmaya/list.txt", "r")
l=[]
for line in f:
    l.append(line.strip())

assert len(l)==1538
f_count=0
t_count=0
max_=20000
min_=0
y_=0
maxr=11111
minr=0.0
mina=1000
maxa=200000
minp=0
maxp=111111
for i in xrange(0,1538):
    mask=cv2.imread("/home/tanmaya/Masks/"+str(i)+".pgm", 0)
    #cure(mask)
    
    _,c,_=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    a=filter(lambda c: cv2.contourArea(c)>min_ and cv2.contourArea(c)<max_, c)
    
    img=cv2.imread("/home/tanmaya/Documents/Image Processing Project/Grayscale/"+l[i-1],0)
    
    for contour in a:
        x,y,w,h=cv2.boundingRect(contour)
        print x
        print y
        print w
        print h
        ratio=w/float(h)
        if y<y_:
            continue
        if ratio<minr or ratio>maxr:
            continue
        if w*h<mina or w*h>maxa:
            continue
        if cv2.arcLength(contour, True)<minp or cv2.arcLength(contour, True)>maxp:
            continue
        cv2.imwrite("/home/tanmaya/Four/"+str(f_count)+".jpg", img[y:y+h,x:x+w])
        f_count=f_count+1
