import os
import numpy as np
from matplotlib import pyplot as plt 
import argparse
import math
from math import cos
from math import sin
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
import sys
import json
from PIL import Image
import os.path
import posixpath

def checkNumberClass(text):
    if(text == "one"):
        return 1
    elif(text == "two"):
        return 2
    elif(text == "three"):
        return 3
    elif(text == "four"):
        return 4
    elif(text == "five"):
        return 5
    elif(text == "six"):
        return 6
    elif(text == "seven"):
        return 7
    elif(text == "eight"):
        return 8
    elif(text == "nine"):
        return 9
    elif(text == "ten"):
        return 10
    elif(text == "eleven"):
        return 11
    elif(text == "twelve"):
        return 12

 #  check line in number's area
def inArea(p,data) :
    number = 0
    status = False
    for i in data:
        top_left = (int(i[2]), int(i[0]))
        bottom_right = (int(i[3]), int(i[1]))
        cv2.rectangle(rec, top_left, bottom_right,109, 2) 
        text = str(i[5][0]).split(':')
        # print(top_left,bottom_right,p,text[0])
        check = checkInArea(top_left,bottom_right,p)
        if(check == True):
            status = True
            num_text = str(i[5][0]).split(':')
            # print("true",num_text[0])
            number = checkNumberClass(num_text[0])
    return status,number
    
def checkInArea(top_left,bottom_right,p):
    if (p[0] >= top_left[0] and p[0] <= bottom_right[0] and p[1] >= top_left[1] and p[1] <= bottom_right[1]) :
        return True
    else :
        return False   

def detect_circle(image):
    output = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# detect circles in the image
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
# ensure at least some circles were found
    if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            cv2.circle(output,(x, y),r, (255,0,0), 3)
    Image.fromarray(output).show()
    return x,y,r

def slope(x1, y1, x2, y2):
    m = (y2-y1)/(x2-x1)
    return m

def checkarrowinbox(h,k,xhead,yhead,xtail,ytail,rec,data_num,r,typehand):
    newX = xhead
    newY = yhead
    i= -1
    if(xhead>xtail):
        i=1
    m = slope(xhead,yhead,xtail,ytail)
    while(math.pow((newX-h),2) + math.pow((newY-k),2) <= math.pow((r),2)):
        c = xhead-((m)*yhead)
        newX+=i         
        newY = ytail-(m*(xtail - newX))
        cv2.line(rec,(xhead,yhead),(int(newX),int(newY)),(255,123,45),2)
        status,number=inArea((int(newX),int(newY)),data_num)
        if(status):
            break
    print(status,number,typehand)



def get_values(iterables, key_to_find):
  return list(filter(lambda x:key_to_find in x, iterables)) 

def detect_arrow(img,name):
    #Image.fromarray(img).show()
    k = 1
    list_center = []
    list_dist = []
    list_namemean = []
    # convert image to gray scale image 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

    # detect corners with the goodFeaturesToTrack function. 
    corners = cv2.goodFeaturesToTrack(gray, 8, 0.005,10) 
    corners = np.int0(corners) 
    
    # making a circle at each point that we think is a corner. 
    for i in corners: 
        x, y = i.ravel() 
        center = x,y
        list_center.append(center)
        cv2.circle(img, (x, y), 3, 255, 2)
        cv2.putText(img,str(k),(x, y), font, 0.1, (0,122,22), 1, cv2.LINE_AA)
        k = k + 1

    list_diff = []    
    # cv2.rectangle(img, (x, y), (x+20, y+20), (255,0,0), 10)
    xmean, ymean = (np.mean(corners, axis = 0)).ravel()
    center = (int(xmean),int(ymean))
    #cv2.circle(img,center, 3, 100, 10)
    Image.fromarray(img).show()
    for i in list_center:
        x,y = i
        distance = math.sqrt(((xmean-x)**2)+((ymean-y)**2) )
        dist = x,y,int(distance)
        list_dist.append(dist)
        #print(list_dist)
        maxval=0
        for i in range(0, len(list_dist)):
            #print(list_dist[i][2])
            if (list_dist[i][2]>=maxval):
                maxval = list_dist[i][2]
                p1,p2 = list_dist[i][0],list_dist[i][1]
    #print(maxval)
    #print(p1,p2)
    #cv2.circle(img,(int(xmean), int(ymean)), 3, 100, 10)
    namemean = img,center,p1,p2,name
    list_namemean.append(namemean)
    return img,center,p1,p2,name
# Name of the directory containing the object detection module we're using
MODEL_NAME = 'inference_graph'
IMAGE_NAME = 'handd'
FILE = '.jpg'
DETECT_FOLDER = 'detectcircle'

# Grab path to current working directory
CWD_PATH = os.getcwd()
IMG_PATH = os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))
# Path to image
PATH_TO_IMAGE = os.path.join(IMG_PATH,IMAGE_NAME+FILE)
#Read image 
image = cv2.imread(PATH_TO_IMAGE)


#read hand
with open("json/script"+IMAGE_NAME+".json") as f:
  data = json.load(f)

# read num from json
file_path = "json/scriptonlynuml.json"
f = open (file_path, "r") 
# Reading from file 
data_num = json.loads(f.read()) 
# Closing file 
f.close() 

#load coordinates from json file
name=[]
list=[] #list of hands
list_centroid =[]
output = image.copy()
rec = image.copy()
font=cv2.FONT_ITALIC
#data[0][0] = ymin , data[0][1]=ymax, data[0][2]=xmin, data[0][3]=xmax
curr_area = 0 
#find radius
h,k,r = detect_circle(image)
cv2.circle(rec,(h,k),1,152,5)

for i in range(0, len(data)):
    #(len(data))
    ymin  = data[i][0]
    ymax = data[i][1]
    xmin = data[i][2]
    xmax = data[i][3]
    name = data[i][5][0].split(":")
    lenx = xmax-xmin
    leny = ymax-ymin
    area = lenx * leny
    start_point = (data[i][2],data[i][0])
    end_point = (data[i][3],data[i][1])
    #find hour and minute hand #ROI = image[y1:y2, x1:x2] (xmin:ymin , xmax:ymax)
    if(area > curr_area):
        arrow = "minutehand"
        curr_area = area
        roi_minute = output[ymin:ymin+leny,xmin:xmin+lenx]
        img,head,p1,p2,name = detect_arrow(roi_minute,arrow)
        x,y = head
        #cv2.circle(rec,(x+xmin,y+ymin), 3,100,10)
        xhead = x+xmin
        yhead = y+ymin
        xtail = p1+xmin
        ytail = p2+ymin 
        cv2.circle(rec,(xhead,yhead), 3,500,10)
        checkarrowinbox(h,k,xhead,yhead,xtail,ytail,rec,data_num,r,"minutehand")
        # cv2.line(rec,(x+xmin,y+ymin),(p1+xmin,p2+ymin),(255,123,0),5)
        cv2.putText(rec,str(arrow),(start_point), font, 0.7, (0,122,22), 1, cv2.LINE_AA)
    else:
        arrow = "hourhand"
        roi_hour = output[ymin:ymin+leny,xmin:xmin+lenx]
        # Image.fromarray(roi_hour).show()
        #cv2.circle(output,(xmin,ymax), 3, (200,12,0), 3)
        img,head,p1,p2,name = detect_arrow(roi_hour,arrow)
        x,y = head
        #cv2.circle(rec,(x+xmin,y+ymin), 3,100,10)
        xhead = x+xmin
        yhead = y+ymin
        xtail = p1+xmin
        ytail = p2+ymin 
        cv2.circle(rec,(xhead,yhead), 3,500,10)
        checkarrowinbox(h,k,xhead,yhead,xtail,ytail,rec,data_num,r,"hourhand")
        #x+min,y+ymin = จุดเริ่มตรงกลาง , p1+xmin,p2+ymin = จุดไกลพุ่งไปเลข
        cv2.putText(rec,str(arrow),(xmin-60,ymax+20), font, 0.7, (200,12,0), 1, cv2.LINE_AA)
    list.append(str(arrow))
    
# print(list)
Image.fromarray(rec).show()
#Image.fromarray(output).show()