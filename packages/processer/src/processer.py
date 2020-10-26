#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 21:08:17 2020

@author: yueshan
"""

import rosbag
import cv2
from cv_bridge import CvBridge
#from sensor_msgs.msg import CompressedImage

bag = rosbag.Bag('/data/amod20-rh3-ex-record-<YueshanLi>.bag')
info=[]

#extract image and timestamp from bag file
bridge = CvBridge()
for topic, img_ros, t in bag.read_messages(topics='/luna/camera_node/image/compressed'):
    img_cv=bridge.compressed_imgmsg_to_cv2(img_ros)
    info.append([img_cv,t])
    #print(info)
bag.close() 
   
#draw timestamp
height,weight=img_cv.shape[0:2]
y_pos=height*0.05
x_pos=weight*0.05
#print(x_pos,y_pos)
for data in info:
    cv2.putText(data[0],str(data[1]),(int(x_pos),int(y_pos)),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1)

#write to new bagfile
newbag = rosbag.Bag('/data/processed_bag.bag', 'w')
for data in info:
    img_msg=bridge.cv2_to_compressed_imgmsg(data[0])    
    newbag.write('/luna/camera_node/image/compressed',img_msg,data[1])

newbag.close()