#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 11:48:59 2019

@author: ben
"""

import numpy as np
from os import listdir
from os.path import isfile, join
import cv2
import sys
from pprint import pprint
import csv
import collections
import pandas as pd

def flatten(l):
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el


def rowcount(matrix):
    return len(matrix)


def columncount(matrix):
    return len(matrix[0])

def white_ratio(matrix):
    y = np.array(matrix)
    ratiopixel = (y == 255).sum()
    ratiopixel = ratiopixel/y.size
    return ratiopixel


def gravity_center(mat):
    sy, sx = mat.shape

    px = 0.0
    py = 0.0

    i = 0
    for x in range(sx):
        for y in range(sy):
            if mat[y, x] > 0:
                px += x
                py += y
                i += 1

    i = float(i)

    return [(px / i)/sx, (py / i)/sy]

def zones(matrix):
    res = np.array([[0]*3]*3)
    x = len(matrix)
    y = len(matrix[0])
    for i in range(x):
        for j in range(y):
            #print(int((i / x) *3), int((j / y) * 3), matrix[i][j])
            res[int((i / x) *3)][int((j / y) * 3)] += matrix[i][j]/255
    res = res/(x*y)
    return res.flatten()

def hist(mat):
    sy,sx = mat.shape
    
    hist_x = [0.0 for x in range(sx)]
    hist_y = [0.0 for x in range(sy)]
    
    for x in range(sx):
        for y in range(sy):
            if mat[y,x] == 1:
                hist_x[x] += 1.0
                hist_y[y] += 1.0
    
    hist_x = [x / sx for x in hist_x]
    hist_y = [y / sy for y in hist_y]
    
    return hist_x+hist_y
    
    

def dist(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

def touching(s1, s2):
    for t1 in s1:
        for t2 in s2:
            if dist(*t1,*t2) <= 1:
                return True
    return False

def separated_shapes(mat):
    sy, sx = mat.shape
    
    shapes = set()
    previous = set()
    
    i = 0
    
    while i < mat.size:
        y, x = (int(i / sx), i % sx)
        val = mat[y,x]
        
        if val <= 0:
            shapes.add(frozenset([(x,y)]))
        
        i += 1
    
    while len(shapes) != len(previous):
        
        previous = set(shapes)
        
        
        sh = list(shapes)
        
        shouldBreak = False
        
        for i in range(len(sh)):
            
            if shouldBreak:
                break
            
            for j in range(i+1,len(sh)):
                s1 = sh[i]
                s2 = sh[j]
                
                if touching(s1,s2):
                    shapes.remove(s1)
                    shapes.remove(s2)
                    shapes.add(s1.union(s2))
                    
                    shouldBreak = True
                    break
    
    return len(shapes)
    



inpath = "../dataset/profs"
descriptors_path = "../dataset/profs.csv"

files = [f for f in listdir(inpath) if isfile(join(inpath, f))]
descriptors = {
        "rowcount":rowcount,
        "columncount":columncount,
        "gravity_center":gravity_center,
        "zones":zones
        }

"""
resized_descriptors = {
        "histogram":hist,
        "separated_shapes": separated_shapes
        }
"""


resized_descriptors = {
        "histogram":hist,
        }




# cv2.imshow("demo", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

errors = 0

df = pd.DataFrame()

j = 0

for file in files:
    j += 1
    
    if j % 3 == 0:
        print("Image {}".format(j))
    
    img = cv2.imread(join(inpath, file), 0)
    
    resized_img = cv2.resize(img, (64, 64))
        
    for c,f in descriptors.items():
        res = list(flatten([f(img)]))
        
        
        if len(res) > 0:
            for i in range(len(res)):
                df.loc[file, c+"_{}".format(i)] = res[i]
        else:
            df.loc[file, c] = res
           
    res = None
        
    for c,f in resized_descriptors.items():
        res_resized = list(flatten([f(resized_img)]))
                
        if len(res_resized) > 0:
            for i in range(len(res_resized)):
                df.loc[file, c+"_{}".format(i)] = res_resized[i]
        else:
            df.loc[file, c] = res_resized
        
df.to_csv(descriptors_path, sep=",")
