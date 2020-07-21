from load_json import *
from ultilis import read_text
import cv2

lines = read_text("C:\\Users\\Admin\\Desktop\\project1\\Image_data_analyzer\\Output\\Easy.txt")
'''
for line in lines:
    image = cv2.imread(line)
    cv2.imshow("test_st", image)    cv2.waitKey()

cv2.destroyAllWindows()
'''

for line in lines:
    name_img = line.split("/")[-1]
    name_json, _ = name_img.split(".jpg")
    path_json = "C:\\Users\\Admin\\Desktop\\Em_HOANG\\scutB_head_gt\\scutB_head_gt\\"
    img  = cv2.imread(line)
    gts, img_gt, info_boxes = load_json(path_json, name_json, img=img, crop=False)
    cv2.imshow("imgGT", img_gt)
    cv2.waitKey()
cv2.destroyAllWindows()
