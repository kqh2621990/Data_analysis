from load_json import *
from ultilis import read_text
import cv2
import imghdr
lines = read_text("/home/minhhoang/Desktop/Data_analysis/outputez/Hard_crow.txt")
'''
for line in lines:
    image = cv2.imread(line)
    cv2.imshow("test_st", image)    cv2.waitKey()

cv2.destroyAllWindows()
'''
path_images = open("/home/minhhoang/Desktop/Data_analysis/outputez/Hard_crow.txt").read().splitlines()

path_json = open("/media/minhhoang/Data/dataPerson/Datatest/easy_json.txt").read().splitlines()

dir_data = "/media/minhhoang/Data/dataPerson/"
for p_img in path_images:
    for p_json in path_json:
        name_img = p_img.split("/")[-1]
        type_img = imghdr.what(p_img)
        if type_img == "jpeg" or type_img == None:
            type_img = "jpg"
        
        name_json, _ = name_img.split("." + type_img)
        
        if name_json in p_json:
            p_json = dir_data + p_json
            img  = cv2.imread(p_img)
            gts, img_gt, info_boxes = load_json(path_json=p_json, img=img)
            cv2.imshow("imgGT", img_gt)
            cv2.waitKey()
    cv2.destroyAllWindows()
