'''
To do : Estimate the hard level of an image through the statistic of ground truth boxes, its size, amount of overlap of
        ground truth boxes
Parameters:
        Providing the directories
            - 'path_img' : Path of the folder which contains image file with extend part '.jpg', '.png', '.jpeg'
            - 'path_json': Path of the folder which contains .json file corresponding the image file
            - 'standard_image_size' : standard image size is customized by the user .
                                      Example : an image with the size is 960 x 540 = 518400 pixels
Output :
        - I : Score of estimated image

syntax to execute :
Example:           python main.py -i [Path folder of image files] -j [Path folder of .json files] -s 518400
'''

import json
import sys
import glob
import os
import numpy as np
import argparse
from analyzer_data_boxes import *
from take_img_json import *
from ultilis import *


if __name__ == "__main__":
    # ap = argparse.ArgumentParser()
    # ap.add_argument('-i','--image_path', required=True, help='provide directory of image')
    # ap.add_argument('-j', '--json_file_path', required=True, help='provide directory of .json file')
    # ap.add_argument('-s', '--standard_image_size', required=True, help='provide the standard image size')
    # args = vars(ap.parse_args())

    path_img = "/media/minhhoang/Data/dataPerson/Datatest/easy_img.txt"
    path_json= "/media/minhhoang/Data/dataPerson/Datatest/easy_json.txt"
    dir_data = "/media/minhhoang/Data/dataPerson/"
    standard_image_size = 518400

    ezimgs = "Datatest/easy_img.txt"
    ezjson = "Datatest/easy_json.txt"

    norimgs = "Datatest/nor_imgs.txt"
    norjson = "Datatest/nor_json.txt"

    hardimgs = "Datatest/hard_imgs.txt"
    hardjson = "Datatest/hard_json.txt"

    #path_img = "C:/Users/Admin/Desktop/Em_HOANG/SCUT_HEAD_Part_B/SCUT_HEAD_Part_B/JPEGImages/"
    #path_json = "C:/Users/Admin/Desktop/Em_HOANG/scutB_head_gt/scutB_head_gt/"

    # for info in take_img_info_from_json(path_json, path_img):
    values = []
    means = []
    stds = []
    idx = 0
    for info in take_img_info_from_txt(path_json, path_img, dir_data):
        idx += 1
        # if idx <= 100:
        info_boxes = info[0]
        img_size = info[1]
        img_path = info[2]
        # CALL FUNCTION for ANALYSIS DATA OF INFO_BOXES
        A = DataAnalysis(info_boxes, img_size, standard_image_size)
        E = A._data_analyzer
        mean_E = np.mean(E)
        std_E = np.std(E)
        values.append(E)
        means.append(mean_E)
        stds.append(std_E)
        print('processing of %d' % (idx + 1))
        if mean_E < 7:
            "cho vao bo Easy"
            path = os.getcwd() + '/outputez/Easy_crow.txt'
            write_txt(path, img_path)
        if 7 < mean_E < 8:
            "cho vao bo Intermediate"
            path = os.getcwd() + '/outputez/Intermediate_crow.txt'
            write_txt(path, img_path)
        if mean_E > 8:
            "cho vao bo Hard"
            path = os.getcwd() + '/outputez/Hard_crow.txt'
            write_txt(path, img_path)
        # else:
        #     break

    import matplotlib.pyplot as plt
    plt.figure(dpi=150)
    plt.plot(np.sort(np.array(means)), 'ro')
    plt.show()

