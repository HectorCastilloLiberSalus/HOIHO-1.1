#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import time
import rospy
from std_msgs.msg import Int16

global img2,img
img = cv2.imread('/home/rissa/Documentos/expresiones/Alegre.png')
img2 = cv2.imread('/home/rissa/Documentos/expresiones/Alegre2.png')

def callback(data):
    global img,img2
    #img = cv2.imread('/home/rissa/Documentos/expresiones/Alegre.png')    
    print(data.data)
    
    if (data.data == 1):
   	img = cv2.imread('/home/rissa/Documentos/expresiones/Alegre.png')
    	img2 = cv2.imread('/home/rissa/Documentos/expresiones/Alegre2.png')

    if (data.data == 2):
    	img = cv2.imread('/home/rissa/Documentos/expresiones/duda1.png')
	img2 = cv2.imread('/home/rissa/Documentos/expresiones/duda2.png')	

    if (data.data == 3):
    	img = cv2.imread('/home/rissa/Documentos/expresiones/Gesto1.png')
	img2 = cv2.imread('/home/rissa/Documentos/expresiones/Gesto2.png')

    if (data.data == 4):
    	img = cv2.imread('/home/rissa/Documentos/expresiones/Neutra.png')
	img2 = cv2.imread('/home/rissa/Documentos/expresiones/Neutra2.png')


    if (data.data == 5):
    	img = cv2.imread('/home/rissa/Documentos/expresiones/Sorpresa1.png')
	img2 = cv2.imread('/home/rissa/Documentos/expresiones/Sorpresa2.png')
	
    if (data.data == 6):
    	img = cv2.imread('/home/rissa/Documentos/expresiones/Triste.png')
	img2 = cv2.imread('/home/rissa/Documentos/expresiones/Triste2.png')

def main():
    global img, img2
    print("corriendo")
    rospy.init_node('animarrostro', anonymous=True)
    rospy.Subscriber('expresion', Int16, callback)
    rospy.sleep(1)
    img_parpadeo = cv2.imread('/home/rissa/Documentos/expresiones/Parpadeo1.png')     
    print("corriendo")
    while True:
    #cv2.namedWindow("test", cv2.WND_PROP_FULLSCREEN)
   # cv2.setWindowProperty("test", cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)
	cv2.imshow("test", img_parpadeo)
    	key = cv2.waitKey(100)
    	cv2.imshow("test", img)
    	key = cv2.waitKey(800)
	cv2.imshow("test", img2)
	key = cv2.waitKey(800)
    	cv2.imshow("test", img)
    	key = cv2.waitKey(800)

if __name__== '__main__':
	main()
