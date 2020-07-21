# ---------------------------------------------
# Python program to check if rectangles overlap
class Point:
    def __init__(self, x, y):
        '''
            Point : the coordinate (x, y) of a point in 2D
        '''
        self.x = x
        self.y = y

def do_overlap(l1, r1, l2, r2):
    '''
    To do:
        Calculate intersection of two boxes
    params:
        l1 : the coordinate of left-top edge of the 1st box
        r1 : the coordinate of right-bottom edge of the 1st box
        l2 : the coordinate of left-top edge of the 2nd box
        r2 : the coordinate of right-bottom edge of the 2nd box
    return:
        True    : if 2 boxes is overlap each others
        False   : if 2 boxes is non-overlap each others
    '''

    # If one rectangle is on left side of other
    if (l1.x >= r2.x or l2.x >= r1.x):
        return False

    # If one rectangle is above other
    if (l1.y >= r2.y or l2.y >= r1.y):
        return False
    return True

def intersec_area(l1, r1, l2, r2):
    '''
        To do:
            Calculate intersection area of two boxes
        params:
            l1 : the coordinate of left-top edge of the 1st box
            r1 : the coordinate of right-bottom edge of the 1st box
            l2 : the coordinate of left-top edge of the 2nd box
            r2 : the coordinate of right-bottom edge of the 2nd box
        return:
            intersection_area : overlapping area between 2 boxes
        '''
    x_left = max(l1.x, l2.x)
    y_top = max(l1.y, l2.y)
    x_right = min(r1.x, r2.x)
    y_bottom = min(r1.y, r2.y)

    intersection_area = (x_right - x_left) * (y_bottom - y_top)
    return intersection_area