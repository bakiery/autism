# WILL NEED TO FIX

import numpy as np
import pandas as pd
#rom colorama import Fore, Style
import cv2
from mtcnn import MTCNN
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer, make_column_transformer
from sklearn.preprocessing import OneHotEncoder, FunctionTransformer
#from taxifare.ml_logic.encoders import transform_time_features, transform_lonlat_features, compute_geohash


def resize_58x64(input_image, output_image=None):
    '''input_image - the whole path to the initial image
    output_image - the name of an output image with the path
    returns the image'''

    #inp_im = cv2.imread(input_image)
    inp_im = input_image
    mtcnn = MTCNN()
    SCALER = 1.1
    ratio = 64 / 58

    try:
        data = mtcnn.detect_faces(inp_im)
        box = data[0]['box']
        bimg = inp_im[box[1]: box[1]+int(box[2]* SCALER * ratio), box[0]: box[0]+int(box[2]*SCALER)]
        bimg_res = cv2.resize(bimg, (58,64))
    except:
        bimg_res = cv2.resize(inp_im, (58,64))

    if not output_image == None:
        cv2.imwrite(output_image, bimg_res)

    return bimg_res

def resize(inp_im, height, width):
    '''input_image - np.array
    height and width - integers
    returns the image'''

    mtcnn = MTCNN()
    SCALER = 1.1
    ratio = height / width

    try:
        data = mtcnn.detect_faces(inp_im)
        box = data[0]['box']
        bimg = inp_im[box[1]: box[1]+int(box[2]* SCALER * ratio), box[0]: box[0]+int(box[2]*SCALER)]
        bimg_res = cv2.resize(bimg, (width,height))
    except:
        bimg_res = cv2.resize(inp_im, (width,height))

    return bimg_res

def rescale(inp_im):
    '''rescales the image from [0:255] to [0:1]'''
    return inp_im/255
