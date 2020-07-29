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
    #
    #
    # path_img = args['image_path']
    # path_json= args['json_file_path']
    # standard_image_size = int(args['standard_image_size'])
    
    # path cho Easy dataset
    # path_img = r"D:\Huy\datasets\easy\data_test\img_easy_dataset"
    # path_json = r"D:\Huy\datasets\easy\data_test\json_easy_dataset"
    # standard_image_size = 518400

    # path cho Norm dataset
    path_img = r"D:\Huy\datasets\ahuyboom\hard\img"
    path_json = r"D:\Huy\datasets\ahuyboom\hard\json"
    standard_image_size = 518400
    #end

    ezimgs = "Datatest\\easy_img.txt"
    ezjson = "Datatest\\easy_json.txt"

    norimgs = "Datatest\\nor_imgs.txt"
    norjson = "Datatest\\nor_json.txt"

    hardimgs = "Datatest\\hard_imgs.txt"
    hardjson = "Datatest\\hard_json.txt"

    #path_img = "C:\\Users\\Admin\\Desktop\\Em_HOANG\\SCUT_HEAD_Part_B\\SCUT_HEAD_Part_B\\JPEGImages\\"
    #path_json = "C:\\Users\\Admin\\Desktop\\Em_HOANG\\scutB_head_gt\\scutB_head_gt\\"

    for info in take_img_info_from_json(path_json, path_img):
        info_boxes = info[0]
        img_size = info[1]
        img_path = info[2]
        print('image is being runned', img_path)
        # CALL FUNCTION for ANALYSIS DATA OF INFO_BOXES
        A = DataAnalysis(info_boxes, img_size, standard_image_size)
        Estimator = A._data_analyzer
        mean_E = np.mean(Estimator[0])
        std_E = np.std(Estimator[0])
        mean_box_normed_size = Estimator[1]
        overlap_mean = Estimator[2]

        print("In ra thong tin muc do danh gia overlap")
        print(Estimator)
        print(" In ra thong tin danh gia E trung binh va standard deviation", mean_E, std_E)

        # if mean_E < 7:
        #     "cho vao bo Easy"
        #     path = os.getcwd()+'\\output\\Hard_dataset-Easy.txt'
        #     write_txt(path, img_path + "   " + str(mean_E) + "   " + str(std_E) + "   " +  str(mean_box_normed_size) + "   " + str(overlap_mean))
        # if 7 < mean_E < 8:
        #     "cho vao bo Intermediate"
        #     path = os.getcwd() + '\\output\\Hard_dataset-Intermediate.txt'
        #     write_txt(path, img_path + "   " + str(mean_E) + "   " + str(std_E) + "   " +  str(mean_box_normed_size) + "   " + str(overlap_mean))
        # if mean_E > 8:
        #     "cho vao bo Hard"
        #     path = os.getcwd() + '\\output\\Hard_dataset-Hard.txt'
        #     write_txt(path, img_path + "   " + str(mean_E) + "   " + str(std_E) + "   " +  str(mean_box_normed_size) + "   " + str(overlap_mean))



