import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import cv2
from PIL import Image


IMAGE_NAME = 'jamtest1'
IMAGE_NUM = 'jamtest1_num'
FILE = '.jpg'
DETECT_FOLDER = 'detectcircle'
IMAGE_FOLDER = 'image_test'

CWD_PATH = os.getcwd()
PREVIOS_PATH = os.path.abspath(CWD_PATH+ "/../")

PATH_TO_IMAGE_TOTAL = os.path.join(PREVIOS_PATH,IMAGE_FOLDER,IMAGE_NAME+FILE)
PATH_TO_IMAGE_HAND = os.path.join(PREVIOS_PATH,IMAGE_FOLDER,IMAGE_NUM+FILE)

img1 = cv2.imread(PATH_TO_IMAGE_TOTAL)
img2 = cv2.imread(PATH_TO_IMAGE_HAND)

img_hands = img1-img2
img_diff = cv2.absdiff(img2, img1)
img_last = cv2.bitwise_not(img_diff)

cv2.imshow('img3',img_last)
cv2.imwrite(os.path.join(PREVIOS_PATH,IMAGE_FOLDER,IMAGE_NAME+'hands.jpg'),img_last)
cv2.waitKey(0)