from os import listdir
from os.path import isfile, join
import sys
from random import sample
from shutil import copyfile

mypath = sys.argv[1]
outpath = sys.argv[2]
fraction = 0.1

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

sampling = sample(onlyfiles, int(fraction*len(onlyfiles)))

for f in sampling:
    copyfile(join(mypath, f), join(outpath, f))

