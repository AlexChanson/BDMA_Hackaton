from os import listdir,getcwd
import os
from os.path import isfile, join,dirname
import matplotlib.pyplot as plt
from shutil import copy
import matplotlib.image as mpimg

dirnam = getcwd()

mypath = "/Users/louis/Documents/BDMA_Hackaton/dataset/sample"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
i = 0
for photo in onlyfiles :
    print(i)
    i+=1
    if (photo!=".DS_Store"):
        img=mpimg.imread(join(mypath,photo))
        fig = plt.figure()
        plt.imshow(img)
        plt.draw()
        plt.pause(1) # <-------
        etiquette = str(input('Enter your input:'))
        print(type(etiquette))
        diretique = join(dirnam,etiquette)

        if not os.path.exists(diretique):
            os.makedirs(diretique)

        copy(join(mypath,photo), diretique)
        plt.close()
      # display it
