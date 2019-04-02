import numpy as np
from os import listdir
from os.path import isfile, join
import cv2
import sys
from pprint import pprint
import csv
import collections

inpath = "../dataset/profs"
outpath = "../dataset/profs_resize"

files = [f for f in listdir(inpath) if isfile(join(inpath, f))]

for file in files:
    oriimg = cv2.imread(join(inpath, file), 0)
    img = cv2.resize(oriimg, (64, 64))
    cv2.imwrite(join(outpath, file), img)
