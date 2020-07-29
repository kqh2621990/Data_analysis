import sys
import glob
import os
import cv2

'''
def write_txt(path_txt, array_path):
    with open(path_txt, "a") as txt_file:
        for line in array_path:
            txt_file.write("".join(line) + "\\n")
'''


def write_txt(path_txt, path_image):
    with open(path_txt, "a") as txt_file:
        txt_file.write(f'{path_image}\n')

def write_txt(path_txt, content):
    with open(path_txt, "a") as txt_file:
        txt_file.write('{}  \n'.format(content))

def read_text(directory_path):
    with open(directory_path) as file:
        path_image = file.readlines()
    data = [line.replace("\\\\", '/').strip() for line in path_image]
    return data
        # while path_image:
        #     img = cv2.imread(path_image)
        #     cv2.imshow('show_image', img)
        #     cv2.waitKey()
        #     path_image = file.readlines()

# path = r"C:\Users\Admin\Desktop\project1\Image_data_analyzer\Output\test.txt"
# write_txt(path, "teen anh" + "   " + str(10))



