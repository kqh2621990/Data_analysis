import cv2
import glob
import os
import sys
from load_json import *
from analyzer_data_boxes import *
import imghdr
def check_imgs(path_img):
    type_img = ('*.jpg', '*.png', "*.jpeg", "*.json")
    lst_img = []
    for files in type_img:
        # print(files)
        lst_img.extend(glob.glob(path_img + files))
    return lst_img

def take_img_json(path_json, path_img, ezimgs, ezjson, norimgs, norjson, hardimgs, hardjson):
    lst_json = check_imgs(path_json)
    lst_json = sorted(lst_json)
    num_img = len(lst_json)
    path_ez_imgs = []
    path_ez_jsons = []

    path_nor_imgs = []
    path_nor_jsons = []

    path_hard_imgs = []
    path_hard_jsons = []

    count = 0

    for image_path in lst_json:
        name_img = image_path.split("\\")[-1]
        name_img = name_img.replace('json', 'jpg')
        image_path = os.path.join(path_img, name_img)
        print(image_path)
        img = cv2.imread(image_path)
        name_json, _ = name_img.split(".jpg")
        gts, img_gt, info_boxes = load_json(path_json, name_json, img=img, crop=False)
        json_path = path_json + name_img + ".json"
        img_size = img.shape[0] * img.shape[1]
        print('ten anh va kich thuoc anh', name_img, img_size)
        cv2.imshow("imgGT", img_gt)
        char = cv2.waitKey()
        print(char)

def take_img_info_from_json(path_json, path_img):
    '''
    Get the ground truth from annotation of .json
    Json structure:
                    "img_width"     : ['the width of an image']
                    "img_height"    : ['the height of an image']
                    "objects": [
                        {
                        "instanceId"    : ['id_of_instance' ]
                        "label"         : ['name_of_label ']
                        "bbox": {
                            "x_topleft" : ['x coordinate of the top left edge of the bbox']
                            "y_topleft" : ['y coordinate of the top left edge of the bbox']
                            "w"         : ['the width of bbox']
                            "h"         : ['the height of bbox']
                        }
                        ...
    Params:
        path_json : path of .json file of the image
        name_json : name of .json file of the image
    Return:
        info_boxes : a list contain {[x_topleft, y_topleft, w, h],...,[...]} of all boxes listed in .json file
        img_size   : size of image in pixel.
    '''
    lst_json = os.listdir(path_json)
    lst_img = os.listdir(path_img)
    lst_json = sorted(lst_json)
    num_img = len(lst_json)

    count = 0
    for p_img, p_json in zip(lst_img, lst_json):

    # for image_path in lst_json:
    #     name_img = image_path.split("\\")[-1]
    #     name_img = name_img.replace('json', 'jpg')
    #     image_path = os.path.join(path_img, name_img)
    #     print(image_path)
        img_name = os.path.join(path_img, p_img)
        img = cv2.imread(img_name)
        path_json_of_image = os.path.join(path_json, p_json)
        print(path_json)
        gts, img_gt, info_boxes = load_json(path_json=path_json_of_image, img = img)
        # json_path = path_json + name_img + ".json"
        img_size = img.shape[0] * img.shape[1]

        yield info_boxes, img_size, img_name

        #print('Name of image {} Image size {} '.format(name_img, img_size))
        cv2.imshow("imgGT", img_gt)
        char = cv2.waitKey()
        print(char)













