from load_json import *
from ultilis import read_text
import cv2
import os


# target = r'C:\Users\Admin\Desktop\project1\Image_data_analyzer\Output\Normal_dataset-Intermediate.txt'
# container = open(target, 'r')
# for line in container.readlines():
#     path_to_image = line.split(' ')[0]
#     image = cv2.imread(path_to_image)
#     cv2.imshow('test', image)
#     cv2.waitKey()
#     cv2.destroyAllWindows()

'''
for line in lines:
    image = cv2.imread(line)
    cv2.imshow("test_st", image)    cv2.waitKey()

cv2.destroyAllWindows()
'''


count = 0
target = r'C:\Users\Admin\Desktop\project1\Image_data_analyzer\Output\Hard_dataset-Hard.txt'
container = open(target, 'r')
for line in container.readlines():
    print(line)
    path_to_image = line.split(' ')[0]
    name_split = path_to_image.split(" ")[0]
    name_img = path_to_image.split("\\")[-1]
    #name_img = line.split(" ")[-1]
    #name, _ = name_img.split(".jpg")
    name, extend = os.path.splitext(name_img)

    name_json = name + ".json"
    path_json = r"D:\Huy\datasets\ahuyboom\hard\json"
    path_json =os.path.join(path_json,name_json)
    print('path_json',path_json)


    img  = cv2.imread(name_split)
    gts, img_gt, info_boxes = load_json(path_json, img)
    cv2.imshow("imgGT", img_gt)
    # nbcv2.imshow("iamge",img)
    cv2.waitKey()
    count = count +1
    print('dem so anh ',count)
    cv2.destroyAllWindows()