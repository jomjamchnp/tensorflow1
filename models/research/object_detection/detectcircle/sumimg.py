import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import cv2
from PIL import Image

IMAGE_FRAME = '1hand'
IMAGE_NUM = 'new_num'
FILE = '.jpg'
DETECT_FOLDER = 'detectcircle'
IMAGE_FOLDER = 'image_test'

CWD_PATH = os.getcwd()
PREVIOS_PATH = os.path.abspath(CWD_PATH+ "/../")

PATH_TO_IMAGE_FRAME = os.path.join(PREVIOS_PATH,IMAGE_FOLDER,IMAGE_FRAME+FILE)
PATH_TO_IMAGE_NUM = os.path.join(PREVIOS_PATH,IMAGE_FOLDER,IMAGE_NUM+FILE)

img1 = cv2.imread(PATH_TO_IMAGE_FRAME,cv2.IMREAD_COLOR)
img2 = cv2.imread(PATH_TO_IMAGE_NUM,cv2.IMREAD_COLOR)


img3 = cv2.addWeighted(img1,0.5,img2,0.5,0)
cv2.imshow('img3',img3)
# cv2.imwrite(os.path.join(PREVIOS_PATH,IMAGE_FOLDER,IMAGE_NAME+'hands.jpg'),img_last)
cv2.waitKey(0)



# import os
# import numpy as np
# from matplotlib import pyplot as plt 
# import argparse
# import math
# from math import cos
# from math import sin
# import cv2
# import matplotlib.pyplot as plt
# import tensorflow as tf
# import sys
# import json
# from PIL import Image
# import os.path
# import posixpath
# ch_eleven = 0
# ch_two = 0


# def detect_line(roi,data):
#     print(data)
#     number = 0
#     list_point = []
#     # convert to grayscale
#     grayscale = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
#     # perform edge detection
#     edges = cv2.Canny(grayscale, 30, 100)
#     # detect lines in the image using hough lines technique
#     lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=10, maxLineGap=250)
#     #Image.fromarray(lines).show()
#     # iterate over the output lines and draw them
#     for line in lines:
#         for x1, y1, x2, y2 in line:
#             cv2.line(roi, (x1, y1), (x2, y2), (255, 0, 0), 2)
#             #cv2.line(roi, (x1, y1), (x2, y2), (255, 0, 0), 2)
#     # show images
#     Image.fromarray(roi).show()
#     return x1,y1,x2,y2

# def checkcrash(data_num,x1,y1,x2,y2,typehand):
#     list_crash = []
#     global ch_eleven,ch_two
#     newX1 = x1
#     newY1 = y1
#     newX2 = x2
#     newY2 = y2
#     distance1 = 0
#     distance2 = 0
#     distance3 = 0
#     distance4 = 0
#     mindist = 999999
#     m = slope(x1,y1,x2,y2)
#     i=1
#     while(math.pow((newX1-h),2) + math.pow((newY1-k),2) <= math.pow((r),2)):
#         newX1+=i         
#         newY1 = y1-(m*(x1 - newX1))
#         #cv2.line(rec,(x1,y1),(int(newX1),int(newY1)),(5, 107, 120),2)
#         #print((int(newX),int(newY)))
#         status,number=inArea((int(newX1),int(newY1)),data_num)
#         distance1 = math.sqrt(((int(newX1)-x1)**2)+((int(newY1)-y1)**2) )
#         if(status):
#             if(number==11 and (typehand=="hourhand" or typehand=="minutehand")):
#                 ch_eleven = 1
#                 print(distance1)
#                 #print(distance)
#             if(number==2 and (typehand=="hourhand" or typehand=="minutehand")):
#                 ch_two = 1
#                 print(distance1)
#             crash = (distance1,status,number,x1,y1,int(newX1),int(newY1))
#             list_crash.append(crash)
#             break
#     i=-1
#     while(math.pow((newX1-h),2) + math.pow((newY1-k),2) <= math.pow((r),2)):
#         newX1+=i         
#         newY1 = y1-(m*(x1 - newX1))
#         #cv2.line(rec,(x1,y1),(int(newX1),int(newY1)),(255,123,45),2)
#         #print((int(newX),int(newY)))
#         status,number=inArea((int(newX1),int(newY1)),data_num)
#         distancex2 = math.sqrt(((int(newX1)-x1)**2)+((int(newY1)-y1)**2) )
#         if(status):
#             if(number==11 and (typehand=="hourhand" or typehand=="minutehand")):
#                 ch_eleven = 1
#             if(number==2 and (typehand=="hourhand" or typehand=="minutehand")):
#                 ch_two = 1
#             crash = (distancex2,status,number,x1,y1,int(newX1),int(newY1))
#             list_crash.append(crash)
#             break
#     i=1
#     while(math.pow((newX2-h),2) + math.pow((newY2-k),2) <= math.pow((r),2)):
#         newX2+=i         
#         newY2 = y2-(m*(x2 - newX2))
#         #cv2.line(rec,(x1,y1),(int(newX1),int(newY1)),(5, 107, 120),2)
#         #print((int(newX),int(newY)))
#         status,number=inArea((int(newX2),int(newY2)),data_num)
#         distance3 = math.sqrt(((int(newX2)-x2)**2)+((int(newY2)-y2)**2) )
#         if(status):
#             if(number==11 and (typehand=="hourhand" or typehand=="minutehand")):
#                 ch_eleven = 1
#                 print(distance1)
#                 #print(distance)
#             if(number==2 and (typehand=="hourhand" or typehand=="minutehand")):
#                 ch_two = 1
#                 print(distance3)
#             crash = (distance3,status,number,x2,y1,int(newX2),int(newY2))
#             list_crash.append(crash)
#             break
#     i=-1
#     while(math.pow((newX2-h),2) + math.pow((newY2-k),2) <= math.pow((r),2)):
#         newX2+=i         
#         newY2 = y2-(m*(x2 - newX2))
#         #cv2.line(rec,(x1,y1),(int(newX1),int(newY1)),(255,123,45),2)
#         #print((int(newX),int(newY)))
#         status,number=inArea((int(newX2),int(newY2)),data_num)
#         distance4 = math.sqrt(((int(newX2)-x2)**2)+((int(newY2)-y2)**2) )
#         if(status):
#             if(number==11 and (typehand=="hourhand" or typehand=="minutehand")):
#                 ch_eleven = 1
#             if(number==2 and (typehand=="hourhand" or typehand=="minutehand")):
#                 ch_two = 1
#             crash = (distance4,status,number,x2,y2,int(newX2),int(newY2))
#             list_crash.append(crash)
#             break
#     print("1",distance1,"2",distance2,"3",distance3,"4",distance4)
#     print(len(list_crash))
#     for i in range(0,len(list_crash)):
#         print(list_crash[i][0])
#         if(list_crash[i][0]<mindist):
#             mindist = list_crash[i][0]
#             x,y,newX,newY=list_crash[i][3],list_crash[i][4], list_crash[i][5], list_crash[i][6]
#     cv2.line(rec,(x,y),(newX,newY),(255,123,45),3)     
#     cv2.circle(rec,(x,y),2,(74, 81, 82),10)   
#     print(status,number,typehand,mindist)
#     # newX2 = x2
#     # newY2 = y2
#     # while(math.pow((newX1-h),2) + math.pow((newY1-k),2) <= math.pow((r),2)):
#     #     newX1-=i         
#     #     newY = y2-(m*(x2 - newX1))
#     #     cv2.line(rec,(x1,y1),(int(newX1),int(newY1)),(255,123,45),2)
#     #     #print((int(newX),int(newY)))
#     #     status,number=inArea((int(newX1),int(newY1)),data_num)
#     #     if(status):
#     #         if(number==11 and typehand=="hourhand"):
#     #             ch_eleven = 1
#     #         if(number==2 and typehand=="minutehand"):
#     #             ch_two = 1
#     #         break
#     # print(status,number,typehand)

#     return ch_eleven,ch_two
    


# def checkNumberClass(text):
#     if(text == "one"):
#         return 1
#     elif(text == "two"):
#         return 2
#     elif(text == "three"):
#         return 3
#     elif(text == "four"):
#         return 4
#     elif(text == "five"):
#         return 5
#     elif(text == "six"):
#         return 6
#     elif(text == "seven"):
#         return 7
#     elif(text == "eight"):
#         return 8
#     elif(text == "nine"):
#         return 9
#     elif(text == "ten"):
#         return 10
#     elif(text == "eleven"):
#         return 11
#     elif(text == "twelve"):
#         return 12

#  #  check line in number's area n=0 : arrownohead , n=1 : arrow
# def inArea(p,data) : #,n,x1,y1,x2,y2
#     status = False
#     number = 0
#     for i in data:
#         top_left = (int(i[2]), int(i[0]))
#         bottom_right = (int(i[3]), int(i[1]))
#         cv2.rectangle(rec, top_left, bottom_right,(53, 77, 206 ), 2) 
#         text = str(i[5][0]).split(':')
#         check = checkInArea(top_left,bottom_right,p)
#         if(check == True):
#             status = True
#             num_text = str(i[5][0]).split(':')
#             #print("true",num_text[0])
#             number = checkNumberClass(num_text[0])

#     return status,number
    
# def checkInArea(top_left,bottom_right,p):
#     if (p[0] >= top_left[0] and p[0] <= bottom_right[0] and p[1] >= top_left[1] and p[1] <= bottom_right[1]) :
#         return True
#     else :
#         return False   

# def detect_circle(image):
#     output = image.copy()
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# # detect circles in the image
#     circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
# # ensure at least some circles were found
#     if circles is not None:
# 	# convert the (x, y) coordinates and radius of the circles to integers
#         circles = np.round(circles[0, :]).astype("int")
#         # loop over the (x, y) coordinates and radius of the circles
#         for (x, y, r) in circles:
#             cv2.circle(output,(x, y),r, (255,0,0), 3)
#     Image.fromarray(output).show()
#     return x,y,r

# def slope(x1, y1, x2, y2):
#     m = (y2-y1)/(x2-x1)
#     return m

# def checkline(h,k,xhead,yhead,xtail,ytail,rec,data_num,r,typehand):
#     global ch_eleven,ch_two
#     newX = xhead
#     newY = yhead
#     i= -1
#     if(xhead>xtail):
#         i=1
#     m = slope(xhead,yhead,xtail,ytail)
#     while(math.pow((newX-h),2) + math.pow((newY-k),2) <= math.pow((r),2)):
#         c = xhead-((m)*yhead)
#         newX+=i         
#         newY = ytail-(m*(xtail - newX))
#         cv2.line(rec,(xtail,ytail),(int(newX),int(newY)),(223, 222, 39 ),2)
#         #print((int(newX),int(newY)))
#         status,number=inArea((int(newX),int(newY)),data_num)
#         if(status):
#             if(number==11 and typehand=="hourhand"):
#                 ch_eleven = 1
#             if(number==2 and typehand=="minutehand"):
#                 ch_two = 1
#             break
#     # print(status,number,typehand)
#     return ch_eleven,ch_two


# def checkarrowinbox(h,k,xhead,yhead,xtail,ytail,rec,data_num,r,typehand):
#     global ch_eleven,ch_two
#     newX = xhead
#     newY = yhead
#     i= -1
#     if(xhead>xtail):
#         i=1
#     m = slope(xhead,yhead,xtail,ytail)
#     while(math.pow((newX-h),2) + math.pow((newY-k),2) <= math.pow((r),2)):
#         c = xhead-((m)*yhead)
#         newX+=i         
#         newY = ytail-(m*(xtail - newX))
#         cv2.line(rec,(xtail,ytail),(int(newX),int(newY)),(223, 222, 39 ),2)
#         status,number=inArea((int(newX),int(newY)),data_num)
#         if(status):
#             if(number==11 and typehand=="hourhand"):
#                 ch_eleven = 1
#             if(number==2 and typehand=="minutehand"):
#                 ch_two = 1
#             break
#     print(status,number,typehand)
#     return ch_eleven,ch_two


# def get_values(iterables, key_to_find):
#   return list(filter(lambda x:key_to_find in x, iterables)) 

# def detect_arrow(img,name):
#     #Image.fromarray(img).show()
#     k = 1
#     list_center = []
#     list_dist = []
#     list_namemean = []
#     # convert image to gray scale image 
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

#     # detect corners with the goodFeaturesToTrack function. 
#     corners = cv2.goodFeaturesToTrack(gray, 8, 0.005,10) 
#     corners = np.int0(corners) 
    
#     # making a circle at each point that we think is a corner. 
#     for i in corners: 
#         x, y = i.ravel() 
#         center = x,y
#         list_center.append(center)
#         cv2.circle(img, (x, y), 3, 255, 2)
#         cv2.putText(img,str(k),(x, y), font, 0.1, (0,122,22), 1, cv2.LINE_AA)
#         k = k + 1

#     list_diff = []    
#     # cv2.rectangle(img, (x, y), (x+20, y+20), (255,0,0), 10)
#     xmean, ymean = (np.mean(corners, axis = 0)).ravel()
#     center = (int(xmean),int(ymean))
#     Image.fromarray(img).show()
#     for i in list_center:
#         x,y = i
#         distance = math.sqrt(((xmean-x)**2)+((ymean-y)**2) )
#         dist = x,y,int(distance)
#         list_dist.append(dist)
#         #print(list_dist)
#         maxval=0
#         for i in range(0, len(list_dist)):
#             #print(list_dist[i][2])
#             if (list_dist[i][2]>=maxval):
#                 maxval = list_dist[i][2]
#                 print(maxval)
#                 p1,p2 = list_dist[i][0],list_dist[i][1]
#     namemean = img,center,p1,p2,name
#     list_namemean.append(namemean)
#     return img,center,p1,p2,name
# # Name of the directory containing the object detection module we're using
# MODEL_NAME = 'inference_graph'
# IMAGE_NAME = 'hand2'
# FILE = '.jpg'
# IMAGE_FOLDER = 'image_test'

# # Grab path to current working directory
# CWD_PATH = os.getcwd()
# PREVIOS_PATH = os.path.abspath(CWD_PATH+ "/../")
# # Path to image
# PATH_TO_IMAGE = os.path.join(PREVIOS_PATH,IMAGE_FOLDER,IMAGE_NAME+FILE)
# #Read image 
# image = cv2.imread(PATH_TO_IMAGE)

# #read hand
# with open("json/script"+IMAGE_NAME+".json") as f:
#   data = json.load(f)
  
# data_corr = []
# data_circle = []
# # read num from json
# with open("json/scriptnew_num.json") as f:
#   data2 = json.load(f)
#   for p in data2['coordinate']:
# 	  data_corr.append(p)
#   for p in data2['circle']:
# 	  data_circle.append(p)

# #load coordinates from json file
# name=[]
# list=[] #list of hands
# list_point=[] #list of coordinate no head [(x1,y2),(x2,y2)]
# list_centroid =[]
# list_crashnum = []
# list_distance = [] 
# output = image.copy()
# rec = image.copy()
# font=cv2.FONT_ITALIC
# #data[0][0] = ymin , data[0][1]=ymax, data[0][2]=xmin, data[0][3]=xmax
# curr_area = 0 
# curr_dist = 99999999
# #find radius
# h,k,r = data_circle
# #cv2.circle(rec,(h,k),1,152,5)

# #score
# score_4 = 0
# score_5 = 0


# for i in range(0, len(data)):
#     #print(len(data))
#     ymin  = data[i][0]
#     ymax = data[i][1]
#     xmin = data[i][2]
#     xmax = data[i][3]
#     name = data[i][5][0].split(":")
#     lenx = xmax-xmin
#     leny = ymax-ymin
#     area = lenx * leny
#     start_point = (data[i][2],data[i][0])
#     end_point = (data[i][3],data[i][1])
#     #print(name[0])
#     if(name[0]=="arrownohead"):
#         roi = output[ymin:ymin+leny,xmin:xmin+lenx]
#         Image.fromarray(roi).show()
#         x1,y1,x2,y2 = detect_line(roi,data_corr)
#         distance = math.sqrt( ((x1-x2)**2)+((y1-y2)**2))
#         #print(distance)
#         if (distance<curr_dist):
#             arrow = "hourhand"
#             curr_dist = distance
#             # status,number=inArea((x1,y1),data_corr)
#             ch_eleven,ch_two=checkcrash(data_corr,x1+xmin,y1+ymin,x2+xmin,y2+ymin,"hourhand")
#             #cv2.circle(rec, (x1+xmin,y1+ymin), 3, 255, 2)
#             #cv2.circle(rec, (x2+xmin,y2+ymin), 3, 255, 2)

#             # status,number=inArea((x2,y2),data_corr)
#         if(distance>curr_dist):
#              arrow = "minutehand"
#              ch_eleven,ch_two=checkcrash(data_corr,x1+xmin,y1+ymin,x2+xmin,y2+ymin,"hourhand")
#              #cv2.circle(rec, (x1+xmin,y1+ymin), 3, 255, 2)
#              #cv2.circle(rec, (x2+xmin,y2+ymin), 3, 255, 2)
#         cv2.putText(rec,str(arrow),(x1+xmin,y1+ymin), font, 0.7, (200,12,0), 1, cv2.LINE_AA)
#         list.append(str(arrow))
#         # ch_eleven,ch_two = checkarrowinbox(h,k,x1,y1,x2,y2,rec,data_corr,r,arrow)
#         # cv2.circle(rec,(x1+xmin,y1+ymin), 3,200,10)
#         # cv2.circle(rec,(x2+xmin,y2+ymin), 3,200,2)

#     #find hour and minute hand #ROI = image[y1:y2, x1:x2] (xmin:ymin , xmax:ymax)
#     else:
#         if(area > curr_area):
#             arrow = "minutehand"
#             curr_area = area
#             roi_minute = output[ymin:ymin+leny,xmin:xmin+lenx]
#             img,head,p1,p2,name = detect_arrow(roi_minute,arrow)
#             x,y = head
#             #cv2.circle(rec,(x+xmin,y+ymin), 3,100,10)
#             xhead = x+xmin
#             yhead = y+ymin
#             xtail = p1+xmin
#             ytail = p2+ymin 
#             cv2.circle(rec,(xtail,ytail),1,(231, 184, 184),2)
#             #cv2.circle(rec,(xhead,yhead), 3,500,10)
#             ch_eleven,ch_two = checkarrowinbox(h,k,xhead,yhead,xtail,ytail,rec,data_corr,r,"minutehand")
#         # list_crashnum.append([status,number,typehand])
#             cv2.putText(rec,str(arrow),(start_point), font, 0.7, (0,122,22), 1, cv2.LINE_AA)
#         if(area < curr_area):
#             arrow = "hourhand"
#             roi_hour = output[ymin:ymin+leny,xmin:xmin+lenx]
#             img,head,p1,p2,name = detect_arrow(roi_hour,arrow)
#             x,y = head
#             #cv2.circle(rec,(x+xmin,y+ymin), 3,100,10)
#             xhead = x+xmin
#             yhead = y+ymin
#             xtail = p1+xmin
#             ytail = p2+ymin 
#             cv2.circle(rec,(xtail,ytail),1,(231, 184, 184),2)
#             #cv2.circle(rec,(xhead,yhead), 3,500,10)
#             ch_eleven,ch_two = checkarrowinbox(h,k,xhead,yhead,xtail,ytail,rec,data_corr,r,"hourhand")
#             #x+min,y+ymin = จุดเริ่มตรงกลาง , p1+xmin,p2+ymin = จุดไกลพุ่งไปเลข
#             cv2.putText(rec,str(arrow),(xmin-60,ymax+20), font, 0.7, (200,12,0), 1, cv2.LINE_AA)
#         list.append(str(arrow))
# #rule4    
# print(list)
# print(ch_eleven,ch_two)
# ch_min = 0
# ch_hr = 0
# if 'minutehand' in list :
#     ch_min = 1
#     score_4 = score_4 + ch_min
# if 'hourhand' in list :
#     ch_hr = 1
#     score_4 = score_4 + ch_hr
# else:
#     ch_hr = 0
#     ch_min= 0

# #rule5
# if(ch_eleven==1):
#     score_5 = score_5 + 1
# if(ch_two==1):
#     score_5 = score_5 + 1


# print("4.have 2 hands: ",score_4)
# print("5.hands on correct digit: ",score_5)
# Image.fromarray(rec).show()
# cv2.imwrite(os.path.join(PREVIOS_PATH,IMAGE_FOLDER,IMAGE_NAME+'frame.jpg'),rec)
# # result = Image.fromarray((rec * 255).astype(np.uint8))
# # result.save(IMAGE_NAME+'.jpg')
# # #Image.fromarray(output).show()
