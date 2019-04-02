from os import listdir
from os.path import isfile, join, isdir
import csv

path = "../etiquetage"
res = []
with open('../dataset/sample_labels.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    for directory in listdir(path):
        if isdir(join(path, directory)):
            for sub_file in listdir(join(path, directory)):
                print([sub_file, directory])
                writer.writerow([sub_file, directory])