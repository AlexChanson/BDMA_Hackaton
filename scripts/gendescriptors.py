import numpy as np
from os import listdir
from os.path import isfile, join
import cv2
import sys
from pprint import pprint
import csv
import collections

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


inpath = "../dataset/all"
descriptors = "../dataset/all.csv"

files = [f for f in listdir(inpath) if isfile(join(inpath, f))]
funcs = [rowcount, columncount, gravity_center, zones]

# cv2.imshow("demo", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

errors = 0

with open(descriptors, 'w') as csvfile:
    out = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for file in files:

        try:
            img = cv2.imread(join(inpath, file), 0)
            res = flatten([f(img) for f in funcs])
            fl = [file]
            fl.extend(res)
            #print(fl)
            out.writerow(fl)
        except Exception:
            print("Error at", file)
            errors += 1

print("Done with", errors)
