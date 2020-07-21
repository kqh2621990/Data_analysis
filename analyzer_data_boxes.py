'''
    to do : this script used to estimate image data into groups
            which have difference hard level from Easy - Average - Hard
    parameter:
            info_boxes : an array contains the information of all ground truth in an image
                        Each column of info_boxes [left-up coordinate x of the box,
                                                     left-up coordinate y of the box,
                                                     width of the box,
                                                     length of the box ]
            img_size = (number of pixels in the length) x  (number of pixels in the width)
            standard_image_size :   user choose an standard_image_size.
                                    Estimated image is compared based on the standard image
    output:
            I : estimated score for the hard level of the image
'''

import numpy as np
import overlap as ol
from overlap import do_overlap, intersec_area
import sys
#sys.path.append("C:/Users/Admin/Desktop/Em_HOANG")


class DataAnalysis:
    def __init__(self, info_boxes, img_size, standard_image_size):
        self.info_boxes = info_boxes
        self.img_size = img_size
        self.standard_image_size = standard_image_size
    def get_info_boxes(self):
        '''
            To do   : get 'info_boxes'
            return  : info_boxes
        '''
        return self.info_boxes
    def get_box_num(self):
        '''
            To do   : give number of boxes in an image
            return  : number of groung truth boxes in an image
        '''
        number_boxes = len(self.info_boxes)
        return number_boxes
    def get_coordinate_center(self):
        '''
            To do  : get the coordinate of the center point of a ground truth box
            return : the coordinate of the center point of a ground truth box
        '''
        d = self.get_box_num()
        center = np.zeros((d, 2))
        center[i,] = [ifb[i][0] + ifb[i][2] / 2, ifb[i][1] + ifb[i][3] / 2]
        return center
    def _data_analyzer(self):
        '''
        To do: Estimate the score for an image relate to:
                - visible ratio of a ground truth box,
                - relative size of ground truth box in comparison to the image size
        :return:
                I : estimated score for an image
        '''
        d = self.get_box_num()
        ifb = np.array(self.info_boxes)
        box_normed_size = np.zeros(d)
        box = np.zeros((d, 4))
        for i in range(0, d):
            box[i,] = [ifb[i][0], ifb[i][1], ifb[i][0] + ifb[i][2], ifb[i][1] + ifb[i][3]]
            box_normed_size[i] = ifb[i][2] * ifb[i][3] / self.img_size  # kich thuoc tuong doi cua box so voi image
        # he so chuan hoa size of image so voi khung chuan
        if self.img_size > self.standard_image_size:
            norm_para = 1
        else:
            norm_para = self.img_size / self.standard_image_size

        # Calculate Overlap area of two boxes
        overlap_matrix = np.zeros((d, d))   #  ma tran mo ta overlap cua cac box voi nhau : 1 la overlap ; 0 la non-overlap
        overlap_area = np.zeros((d, d))     # ma tran chua dien tich overlap cua cac box voi nhau
        for i in range(0, d - 1):
            l1 = ol.Point(box[i][0], box[i][1])
            r1 = ol.Point(box[i][2], box[i][3])
            for j in range(i + 1, d):
                l2 = ol.Point(box[j][0], box[j][1])
                r2 = ol.Point(box[j][2], box[j][3])
                if do_overlap(l1, r1, l2, r2):
                    overlap_matrix[i, j] = overlap_matrix[j, i] = 1
                    overlap_area[i, j] = overlap_area[j, i] = intersec_area(l1, r1, l2, r2)
        #  Calculate the non-overlap part of each box, using it to estimate score for the image
        I = np.ones(d, dtype=float)
        for i in range(0, d):
            for j in range(0, d):
                if overlap_matrix[i, j] == 1:
                    I[i] = 1 - overlap_area[i, j] / (ifb[i][2] * ifb[i][3])
        # I = -np.log2(norm_para * np.multiply(I, box_normed_size))
        I = -np.log2(np.multiply(I, box_normed_size))
        return I

