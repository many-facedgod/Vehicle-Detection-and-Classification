#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 00:54:27 2016

@author: tanmaya
"""

import cv2
import numpy as np

f=open("/home/tanmaya/list.txt", "r")
l=[]
for line in f:
    line=line.strip()
    l.append(line)

f=open("/home/tanmaya/opp80.txt", "r")
m=[]
for line in f:
    line=line.strip().split()
    m.append((int(line[0]),int(line[2])))

n=[]
o=[]
p=[]

def comp(x,y):
    tx = tuple(x[x[:,:,1].argmin()][0])
    ty = tuple(y[y[:,:,1].argmin()][0])
    if tx[0]<ty[0]:
        return -1
    elif tx[1]<ty[1]:
        return -1
    else:
        return 1
for i in xrange(1538):    
    z=filter(lambda x: x[0]==i+1, m)
    j=[x[1] for x in z]
    n.append(j)
    o.append(cv2.imread("/home/tanmaya/Masks3/image"+str(i+1)+".pgm",0))
    p.append(cv2.imread("/home/tanmaya/Documents/Image Processing Project/Grayscale2/"+l[i],0))

for i,mask in enumerate(o):
    img=p[i]

    ll=n[i]
    
    _,c,_=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    j=sorted(c, comp)
    for pr,q in enumerate(j):
        x,y,w,h=cv2.boundingRect(q)
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(255*ll[pr],255*ll[pr],255*ll[pr]),2)
    cv2.imwrite("/home/tanmaya/final2/"+str(i)+".jpg",img)