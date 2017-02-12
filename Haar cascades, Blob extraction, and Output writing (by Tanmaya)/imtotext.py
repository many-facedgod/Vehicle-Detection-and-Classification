#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 22:14:43 2016

@author: tanmaya
"""

import cv2
import numpy as np
f=open("blah.txt", "w")

for i in xrange(1,1539):
    mask=cv2.imread("/home/tanmaya/Masks3/image"+str(i)+".pgm", 0)
    for j in xrange(mask.shape[0]):
        for k in xrange(mask.shape[1]):
            if mask[j,k]==0:
                f.write("0 ")
            else:
                f.write("1 ")
    f.write("\n")
    print i
f.close()