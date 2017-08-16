#!/usr/bin/env python

import pyaudio 
import speech_recognition as sr
import rospy
import cv2
from std_msgs.msg import String
import time

r = sr.Recognizer()
r.energy_threshold  =  7500

def reconocedor():
    pub = rospy.Publisher('palabras', String, queue_size=10)
    rospy.init_node('Reconocedor', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
	    with sr.Microphone(5) as source:
	        print("Say something!")
	        audio = r.listen(source)
	        print("recorded")
	    try:
	        cadena = r.recognize_google(audio, language="es-ES")
	        print("You said: " + cadena)
	        pub.publish(cadena)
	        rate.sleep()
		time.sleep(3)
	    except sr.UnknownValueError:
	        cadena = "not recognized"
	        pub.publish(cadena)
	        rate.sleep()
	        print("Google Speech Recognition could not understand audio")
		time.sleep(3)
	    except sr.RequestError as e:
	        cadena = "no connection"
	        pub.publish(cadena)
	        rate.sleep()
	        print("Could not request results from Google Speech Recognition service; {0}".format(e))
		time.sleep(3)
if __name__=='__main__':
    try:
        reconocedor()
    except rospy.ROSInterruptException:
        pass
        
