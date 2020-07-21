--------------------------------------------------------------------------------------------------------------
Version 0.1, July 2020
This package contains source code to estimate the hard-level of an image 
which will be used to test for trained deep learning model 
---------------------------------------------------------------------------------------------------------------
ALGORITHM
Information of ground truth boxes - 'bbox' is loaded from .json file correspoding to a image file.
With respect to each 'bbox', a number of intersection with others is determined.
Part of non-overlap area of each 'bbox' is estimated.
This visible area of a box in percentage is multiplied by normed area of the box
( [normed area of a box] = [area of a box in pixel ] / [area of the whole image in pixel].
This quantity represents amount of relatively usefull information in a box in an image which has a specific size.
After that, relatively usefull information is normalized based on a standard image size ( customized by user).
Estimated score for an image is estimated by the quantity I = -log2[sum of usefull information]   
---------------------------------------------------------------------------------------------------------------
ESTIMATED LEVEL
  I < 6		: Easy level
  6 < I < 8 : Intermediate level
  8 < I < 9 : Difficult level
  I > 9 	: Very Difficult level     
---------------------------------------------------------------------------------------------------------------
SOURCE CODE includes files:
main.py 	              - main code 			
analyzer_data_boxes.py 	- Contain function to estimate the score for an image
load_json.py            - Take information of all ground truth boxes in an image
take_img_json.py		    - Load name of .json file corresponding name of image file
overlap.py 				      - Calculate overlap area of two boxes



