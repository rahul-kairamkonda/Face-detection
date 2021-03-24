# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 23:33:21 2021

@author: Rahul
"""
import numpy as np
import cv2 as cv
img=cv.imread('sudoku.png')
_,th1=cv.threshold(img,127,255,cv.THRESH_BINARY)
thresh1 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, 
                                          cv.THRESH_BINARY_INV, 11, 2) 
#cv.imshow('th1',th1)
cv.imshow('th2',thresh1)
cv.imshow("Image",img)
cv.waitKey(0)
cv.destroyAllWindows()