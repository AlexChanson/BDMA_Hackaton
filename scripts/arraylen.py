from PIL import Image
import pandas as pd
import numpy as np
import glob
rowdes = []
columndes =[]
ratiodes =[]

def rowcount(path,rowdes):
    for filename in glob.glob(path):
        im=Image.open(filename)
        pd_im = pd.DataFrame(np.array(im))
        rowlen = pd_im.shape[0]
        rowdes.append(rowlen)
def columncount(path,columndes):
    for filename in glob.glob(path):
        im=Image.open(filename)
        pd_im = pd.DataFrame(np.array(im))
        columnlen = pd_im.shape[1]
        columndes.append(columnlen)
def ratiocount(path,columndes):
    for filename in glob.glob(path):
        im=Image.open(filename)
        pd_im = pd.DataFrame(np.array(im))
        rowlen = pd_im.shape[0]
        columnlen = pd_im.shape[1]
        ratio = rowlen / columnlen
        ratiodes.append(ratio)

filepath = '/home/xairon/Bureau/BDMA_Hackaton/dataset/0/*.png'
rowcount(filepath,rowdes)
print(rowdes)
columncount(filepath,columndes)
print(columndes)
ratiocount(filepath,ratiodes)
print(ratiodes)