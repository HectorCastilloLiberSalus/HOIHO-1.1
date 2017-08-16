#!/usr/bin/env python

from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient
import rospy
from std_msgs.msg import Float32
import numpy
import time
from beginner_tutorials.msg import Num
from geometry_msgs.msg import Twist
import sys, curses
from std_msgs.msg import String
from std_msgs.msg import Empty
from face_recognition.msg import FaceRecognitionActionFeedback

global voz, mover,vel_msg, soundhandle, X, Y, Z, THETA,G, R1, R2, pub,  nombre, nombre_identificado, it, nombre_encontrado
vel_msg = Twist()
it = 0
X = 90
Y = 180
Z = 150
THETA = 90
G = 0
R1 = 90
R2 = 50
voz = 0
vel_msg.linear.y = 0
vel_msg.linear.z = 0
vel_msg.angular.x = 0
vel_msg.angular.y = 0
nombre = ' '
nombre_identificado = 0
nombre_encontrado= ''
def callback_create(data):
    global voz, vel_msg, soundhandle
    rospy.loginfo(rospy.get_caller_id() + 'Parar %s', data)
    vel_msg.linear.x = abs(0)
    vel_msg.angular.z = abs(0)
    mover.publish(vel_msg)

def nombre(data):
    global it, nombre_identificado, nombre, nombre_encontrado
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.feedback.names)
    if (nombre_identificado == 0 or it == 10):
    	nombre = data.feedback.names
	nombre_identificado = nombre_identificado + 1
        it  = 0
    if (nombre_identificado>0):
	if (nombre == data.feedback.names):
		nombre_identificado = nombre_identificado + 1 
        if (nombre_identificado == 5):
		a = str(nombre)
    		b = a.replace("[","")
   		c = b.replace("]","")
   		nombre_encontrado = c.replace("'","")
		nombre_identificado = 0
    it = it + 1
def callback(data):
    recognized = 0
    global voz, vel_msg, soundhandle, X, Y, Z, THETA, G, R1, R2,pub, nombre_encontrado
    rospy.loginfo(rospy.get_caller_id() + 'Dijiste:  %s', data.data)
    if ('who are you' in data.data):
	    s = "Hello, i am hoiho"
	    voice = 'voice_kal_diphone'
	    volume = 0.05
	    soundhandle.say(s, voice, volume)
    	    rospy.sleep(1)
	    recognized = 1
    if ('hoiho' in data.data):
	    voice = 'voice_kal_diphone'
            volume = 0.05
            if ('front' in data.data):
		vel_msg.linear.x = abs(0.05)
		vel_msg.angular.z = abs(0)
	    	ss = "ok going front,  ,   ,   ,   ,  ,  ,  ,"
		s = ss + nombre_encontrado    		
		soundhandle.say(s, voice, volume)
		print(s)
		for ww in range (0, 30):
			mover.publish(vel_msg)
			time.sleep(0.1)
		recognized = 1

	    if ('back' in data.data):
		vel_msg.linear.x = -abs(0.05)
		vel_msg.angular.z = abs(0)
		print("atras")
	    	ss = "ok going back  ,   ,   ,   ,  ,  ,  ,"
		s = ss + nombre_encontrado 
	    	soundhandle.say(s, voice, volume)
		for ww in range (0, 30):
			mover.publish(vel_msg)
			time.sleep(0.1)
		recognized = 1

	    if ('rigth' in data.data):
		vel_msg.angular.z = -abs(0.55)
		vel_msg.linear.x = abs(0)
		mover.publish(vel_msg)
		print("Derecha")	
	    	s = "ok turning right"
	    	soundhandle.say(s, voice, volume)
		recognized = 1

	    if ('left' in data.data):
		vel_msg.angular.z = abs(0.5)
		vel_msg.linear.x = abs(0)
		mover.publish(vel_msg)
		print("ok")
	    	s = "ok, turning left"
	    	soundhandle.say(s, voice, volume) 
	 	recognized = 1



	    if ('how' in data.data and 'are' in data.data):
	    	ss = "I am fine, , , , and you?, , , , , , , "
		s = ss + nombre_encontrado 
	    	soundhandle.say(s, voice, volume)
	    	rospy.sleep(1)
		recognized = 1

	    if ('nice' in data.data and 'meet' in data.data):
	    	s = "nice to meet you too"
	    	soundhandle.say(s, voice, volume)
	    	rospy.sleep(1)
		recognized = 1

	    if ('go home' in data.data):
	    	ss = "Ok, going home, , , , , , , , "
		s = ss + nombre_encontrado 
	    	soundhandle.say(s, voice, volume)
	    	rospy.sleep(1)
		recognized = 1

	    if ('fine' in data.data):
	    	s = "great"
		print("great")
	    	soundhandle.say(s, voice, volume)
	    	rospy.sleep(1)
		print()
		recognized = 1

	    if ('stop' in data.data):
	    	s = "ok, , , stopping"
		print("great")
	    	soundhandle.say(s, voice, volume)
	    	rospy.sleep(1)
		print()
		recognized = 1

	    if ('follow me' in data.data):
	    	ss = "ok, , , following you, , , , , , "
	        s = ss + nombre_encontrado 
	    	soundhandle.say(s, voice, volume)
	    	rospy.sleep(1)
		print()
		recognized = 1

	    if ('take' in data.data):
	    	s = "ok, , , following you"
	    	soundhandle.say(s, voice, volume)
	    	rospy.sleep(1)
		print()
		recognized = 1
		G = 1
		a = numpy.array([X,Y,Z,THETA,G],dtype=numpy.float32)
		pub.publish(a)
	    if ('please' in data.data and 'me' in data.data ):
	    	s = "ok, , , no problem"
		print("great")
	    	soundhandle.say(s, voice, volume)
	    	rospy.sleep(1)
		print()
		recognized = 1


	    if(recognized == 0):
	    	ss = "Sorry, , , , , ,  i dont understand, , ,  "
		s = ss + nombre_encontrado 
		volume = 0.05
	    	soundhandle.say(s, voice, volume)
	    	rospy.sleep(1)
		
	
def talker():
    global voz, mover, vel_msg, soundhandle, X, Y, Z, THETA, G, R1, R2, pub
    pub = rospy.Publisher('izquierdo', Num, queue_size=10)
    pubD = rospy.Publisher('derecho', Num, queue_size=10)
    pubC1 = rospy.Publisher('cabezarot', Num, queue_size=10)
    pubC2 = rospy.Publisher('cabezarot2', Num, queue_size=10)
    mover = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.init_node('mandobrazos', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    stdscr = curses.initscr()
    curses.cbreak()
    stdscr.keypad(1)
    stdscr.addstr(0,0,"Teclea los comandos")
    stdscr.refresh()
    tecla = '' 
    
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0


    #'''
    X = 90
    Y = 0
    Z = 20
    THETA = 0
    G = 0
    R1 = 90
    R2 = 50
    rospy.Subscriber('/recognizer/output', String, callback)
    rospy.Subscriber('wheeldrop', Empty, callback_create)
    soundhandle = SoundClient()
    rospy.sleep(1)
    rospy.Subscriber('/face_recognition/feedback', FaceRecognitionActionFeedback, nombre)
    voice = 'voice_el_diphone'
    volume = 0.05
    s = "Hola"

    while not rospy.is_shutdown():
	tecla = stdscr.getch()
        #stdscr.refresh()
	if(tecla == ord('8')):
		vel_msg.linear.x = abs(0.05)
		vel_msg.angular.z = abs(0)
		for ww in range (0, 30):
			mover.publish(vel_msg)
			time.sleep(0.1)
		print("adelante")
	if(tecla == ord('5')):
		vel_msg.linear.x = -abs(0.05)
		vel_msg.angular.z = abs(0)
		for ww in range (0, 30):
			mover.publish(vel_msg)
			time.sleep(0.1)
		print("atras")
	if(tecla == ord('4')):
		vel_msg.angular.z = abs(0.5)
		vel_msg.linear.x = abs(0)
		mover.publish(vel_msg)
		print("izquierda")
	if(tecla == ord('6')):
		vel_msg.angular.z = -abs(0.5)
		vel_msg.linear.x = abs(0)
		mover.publish(vel_msg)
		print("Derecha")
	if(tecla == ord('q')):
		X = X+20
		a = numpy.array([X,Y,Z,THETA,G],dtype=numpy.float32)
		pubD.publish(a) 
		rospy.loginfo(a)
	if(tecla == ord('a')):
		X = X-20
		a = numpy.array([X,Y,Z,THETA,G],dtype=numpy.float32)
		pubD.publish(a)
		rospy.loginfo(a)
	if(tecla == ord('w')):
		Y = Y+20
		a = numpy.array([X,Y,Z,THETA,G],dtype=numpy.float32)
		pubD.publish(a)
		rospy.loginfo(a)
	if(tecla == ord('s')):
		Y = Y-20
		a = numpy.array([X,Y,Z,THETA,G],dtype=numpy.float32)
		pubD.publish(a)
		rospy.loginfo(a)
	if(tecla == ord('e')):
		Z = Z+20
		a = numpy.array([X,Y,Z,THETA,G],dtype=numpy.float32)
		pubD.publish(a)
		rospy.loginfo(a)
	if(tecla == ord('d')):
		Z = Z-20
		a = numpy.array([X,Y,Z,THETA,G],dtype=numpy.float32)
		pubD.publish(a)
		rospy.loginfo(a)
	if(tecla == curses.KEY_LEFT):
		THETA = THETA+40
		a = numpy.array([X,Y,Z,THETA,G],dtype=numpy.float32)
		pubD.publish(a)
		rospy.loginfo(a)
	if(tecla == curses.KEY_RIGHT):
		THETA = THETA-40
		a = numpy.array([X,Y,Z,THETA,G],dtype=numpy.float32)
		pubD.publish(a)
		rospy.loginfo(a)
	if(tecla == ord('c')):
		G = 1
		a = numpy.array([X,Y,Z,THETA,G],dtype=numpy.float32)
		pubD.publish(a)
		rospy.loginfo(a)
	if(tecla == ord('o')):
		G = 0
		a = numpy.array([X,Y,Z,THETA,G],dtype=numpy.float32)
		pubD.publish(a)
		rospy.loginfo(a)
	if(tecla == ord('r')):
		R1 = R1 + 10
		B = numpy.array([R1],dtype=numpy.float32)
		pubC1.publish(B)
	if(tecla == ord('f')):
		R1 = R1 - 10
		B = numpy.array([R1],dtype=numpy.float32)
		pubC1.publish(B)
	if(tecla == ord('t')):
		R2 = R2 + 10
		C = numpy.array([R2],dtype=numpy.float32)
        	pubC2.publish(C)
	if(tecla == ord('g')):
		R2 = R2 - 10
		C = numpy.array([R2],dtype=numpy.float32)
        	pubC2.publish(C)

	#rospy.loginfo(a)
		
	
	#pubD.publish(a)


	#vel_msg.linear.x = 0
	#mover.publish(vel_msg)
	rate.sleep()
    curses.endwin()
if __name__ == '__main__':
    try:
        talker()

    except rospy.ROSInterruptException:
        pass
