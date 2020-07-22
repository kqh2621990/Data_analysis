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

    # # hoang code 
    path_img = "/media/minhhoang/Data/dataPerson/MOT20/test/MOT20-04/some_img/"
    path_json = "/media/minhhoang/Data/dataPerson/data_test_person/GT/MOT20real_format/mot20-04/"
    standard_image_size = 1668600
    # #end
    
    # path_img = args['image_path']
    # path_json= args['json_file_path']
    # standard_image_size = int(args['standard_image_size'])

    ezimgs = "Datatest\\easy_img.txt"
    ezjson = "Datatest\\easy_json.txt"

    norimgs = "Datatest\\nor_imgs.txt"
    norjson = "Datatest\\nor_json.txt"

    hardimgs = "Datatest\\hard_imgs.txt"
    hardjson = "Datatest\\hard_json.txt"

    #path_img = "C:\\Users\\Admin\\Desktop\\Em_HOANG\\SCUT_HEAD_Part_B\\SCUT_HEAD_Part_B\\JPEGImages\\"
    #path_json = "C:\\Users\\Admin\\Desktop\\Em_HOANG\\scutB_head_gt\\scutB_head_gt\\"
    infomation = take_img_info_from_json(path_json, path_img, ezimgs, ezjson, norimgs, norjson, hardimgs, hardjson)
    print(infomation)
    if not os.path.exists(os.getcwd()+'/output'):
        os.mkdir(os.getcwd()+'/output')
    for info in infomation:
        info_boxes = info[0]
        img_size = info[1]
        img_path = info[2]
        # CALL FUNCTION for ANALYSIS DATA OF INFO_BOXES
        A = DataAnalysis(info_boxes, img_size, standard_image_size)
        I = A._data_analyzer()
        mean_I = np.mean(I)
        std_I = np.std(I)
        print("In ra thong tin muc do danh gia overlap")
        print(I)
        print(" In ra thong tin danh gia I trung binh va standard deviation", mean_I, std_I)

        if mean_I < 7:
            "cho vao bo Easy"
            path = os.getcwd()+'/output/Easy.txt'
            write_txt(path, img_path)
        if 7 < mean_I < 8:
            "cho vao bo Intermediate"
            path = os.getcwd() + '/output/Intermediate.txt'
            write_txt(path, img_path)
        if mean_I > 8:
            "cho vao bo Hard"
            path = os.getcwd() + '/output/Hard.txt'
            write_txt(path, img_path)




