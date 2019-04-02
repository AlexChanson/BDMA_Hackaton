from PIL import Image
import pandas as pd
import numpy as np
import glob


def rowcount(matrix):

        pd_im = pd.DataFrame(matrix)
        rowlen = pd_im.shape[0]
        return rowlen


def columncount(matrix):
    pd_im = pd.DataFrame(matrix)
    columnlen = pd_im.shape[1]
    return columnlen


def ratiocount(matrix):
    pd_im = pd.DataFrame(matrix)
    rowlen = pd_im.shape[0]
    columnlen = pd_im.shape[1]
    ratio = rowlen / columnlen
    return ratio

