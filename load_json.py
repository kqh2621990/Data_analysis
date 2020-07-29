import cv2
import json
import os
import random
import glob
import numpy as np
from shutil import copyfile


def add_padding(img, ratio=256, add_bot=True, add_right=True):  # add padding image h and w % 256
    right, bot = 0, 0  # add to right and bot
    if (img.shape[1] % ratio) != 0:
        right = ((img.shape[1] // ratio) + 1) * ratio - img.shape[1]
    if (img.shape[0] % ratio) != 0:
        bot = ((img.shape[0] // ratio) + 1) * ratio - img.shape[0]

    if add_bot:
        imgPadding = cv2.copyMakeBorder(img, 0, bot, 0, 0, cv2.BORDER_CONSTANT)
    if add_right:
        imgPadding = cv2.copyMakeBorder(img, 0, 0, 0, right, cv2.BORDER_CONSTANT)
    return imgPadding


def crop_image_cv2(imgPadding, ratio=256, save_img=False,
                   path_save='/home/minhhoang/tu/head_detection/cropimage/'):  # crop img_original to many img 256x256 return lst_img
    x = 0
    y = 0
    vt = 0
    lst_img = []
    for i in range(int(imgPadding.shape[0] / ratio)):
        for j in range(int(imgPadding.shape[1] / ratio)):
            img_crop = imgPadding[x:x + ratio, y:y + ratio, :]
            if save_img:
                cv2.imwrite(path_save + str(i) + str(j) + ".jpg", img_crop)
            lst_img.append(img_crop)
            # cv2.imwrite("/home/minhhoang/Desktop/test1/abcd/img_crop"+str('{0:04}'.format(vt))+".jpg",img_crop)
            y += ratio
            vt += 1
        y = 0
        x += ratio
    return lst_img


def load_json(directory, nameOfImage, box_img=None, p_save_img=None, img=None, crop=True):
    """
    To do : get info of ground truth which is rectangular boxes
    para :
        directory   : directory of .json file of an image
        nameOfImage : name of the image
    return:
        gts :
        img :
        info_boxes : a list contain {[x_topleft, y_topleft, w, h],...,[...]} of all boxes listed in .json file
    """
    path_file = directory + nameOfImage + ".json"
    if os.path.exists(path_file):
        print("run load json")
        gts = []
        with open(path_file) as f:
            fh1 = json.load(f)
            '''brainwash'''
            # _ , nameOfImage = nameOfImage.split("-")
            '''end'''
            info_boxes = []                             # bao gom 4 thong so cua cac box
            for idx, line in enumerate(fh1['objects']):
                gt = []
                gt.append(nameOfImage)
                # print(line['label'])
                gt.append(line['label'])
                gt.append(1)
                x = int(line['bbox']['x_topleft'])  # x_topleft
                y = int(line['bbox']['y_topleft'])  # y_topleft
                w = int(line['bbox']['w'])
                h = int(line['bbox']['h'])
                # HUY BO SUNG ###########################
                print("x=", x, "y=", y, "w=", w, "h=", h)
                info_boxes.append([x, y, w, h])

                if crop:
                    if x > box_img[1] and y > box_img[0] and (x + w) < (box_img[1] + box_img[3]) and (y + h) < (
                            box_img[2] + box_img[0]):
                        xnew = x - box_img[1]
                        ynew = y - box_img[0]
                        wnew = w
                        hnew = h
                        tup = tuple([xnew, ynew, xnew + w, ynew + h])
                        # print(tup)
                        gt.append(tup)
                        # print(xnew, ynew, wnew, hnew)
                        cv2.rectangle(img, (xnew, ynew), (xnew + wnew, ynew + hnew), (0, 255, 0), 2)
                        gts.append(gt)
                else:
                    tup = tuple([x, y, x + w, y + h])
                    # print(tup)
                    gt.append(tup)
                    # print(xnew, ynew, wnew, hnew)
                    image = cv2.putText(img, str(idx + 1), (x - 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255),
                                        1, cv2.LINE_AA)
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

                    gts.append(gt)
            print(nameOfImage)
            # cv2.imshow("gts", img)
        # cv2.waitKey()
        # save_img = p_save_img + "/" + nameOfImage + ".png"

        # cv2.imwrite(save_img, img)
        return gts, img, info_boxes

def load_json(path_json = None, img = None):
    gts = []
    with open(path_json) as f:
        fh1 = json.load(f)
        '''brainwash'''
        # _ , nameOfImage = nameOfImage.split("-")
        '''end'''
        info_boxes = []
        nameOfImage = "hoang"                          # bao gom 4 thong so cua cac box
        for idx, line in enumerate(fh1['objects']):
            gt = []
            gt.append(nameOfImage)
            # print(line['label'])
            gt.append(line['label'])
            gt.append(1)
            x = int(line['bbox']['x_topleft'])  # x_topleft
            y = int(line['bbox']['y_topleft'])  # y_topleft
            w = int(line['bbox']['w'])
            h = int(line['bbox']['h'])
            # HUY BO SUNG ###########################
            print("x=", x, "y=", y, "w=", w, "h=", h)
            info_boxes.append([x, y, w, h])
            tup = tuple([x, y, x + w, y + h])
            # print(tup)
            gt.append(tup)
            # print(xnew, ynew, wnew, hnew)
            image = cv2.putText(img, str(idx + 1), (x - 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255),
                                1, cv2.LINE_AA)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            gts.append(gt)
    return gts, img, info_boxes

def random_crop(p_img, folder_json, p_save_img, crop=True, new_size=(320, 240)):
    orig_image = cv2.imread(p_img)
    image = cv2.cvtColor(orig_image, cv2.COLOR_BGR2RGB)

    box_img = []
    name_foder = p_img.rsplit("/", 2)[1]
    nameOfimg = p_img.rsplit("/", 1)[1]
    nameOfimg = nameOfimg.rsplit(".", 1)[0]
    name_json = name_foder + "/" + nameOfimg + "/"
    if crop:
        h, w = new_size
        w_img = image.shape[0]
        h_img = image.shape[1]

        rdx = random.randint(0, w_img - w)
        rdy = random.randint(0, h_img - h)
        box_img.append(rdx)  # xtopl
        box_img.append(rdy)  # ytopl

        box_img.append(rdx + w)  # w
        box_img.append(rdy + h)  # h
        img_crop = image[rdx:rdx + w, rdy:rdy + h, :]
        rd_img = img_crop.copy()
        # cv2.imshow("crop", img_crop)

        gts, img = load_json(folder_json, name_json, box_img, rd_img)
        # cv2.imshow("rd_img", rd_img)
        save_img = p_save_img + nameOfimg + "_" + str(rdx + w) + "x" + str(rdy + h) + ".png"

        cv2.imwrite(save_img, img)
        return img_crop, gts
    # print("shape crop", img_crop.shape)
    else:

        # load_json(folder_json, nameOfimg, box_img, p_save_img, orig_image, crop=False)
        gts, img = load_json(folder_json, nameOfimg, box_img, img=orig_image, crop=False)
        # '''brainwash'''
        # # gts, img = load_json(folder_json, name_json, box_img, orig_image, crop=False)
        # '''end'''

        # # cv2.imshow("rd_img", rd_img)
        save_img = p_save_img + nameOfimg + ".png"

        cv2.imwrite(save_img, img)
        # return image, gts
        return image, gts, img

