#!/usr/bin/env python


import rospy
from std_msgs.msg import Float32
import numpy
from beginner_tutorials.msg import Num
from geometry_msgs.msg import Twist
import sys, curses

def talker():
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
    vel_msg = Twist()
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0


    #'''
    X = 80
    Y = 90
    Z = 90
    THETA = 90
    G = 0
    R1 = 90
    R2 = 90
    while not rospy.is_shutdown():
	tecla = stdscr.getch()
        #stdscr.refresh()
	if(tecla == ord('8')):
		vel_msg.linear.x = abs(0.05)
		vel_msg.angular.z = abs(0)
		mover.publish(vel_msg)
	if(tecla == ord('5')):
		vel_msg.linear.x = -abs(0.05)
		vel_msg.angular.z = abs(0)
		mover.publish(vel_msg)
	if(tecla == ord('4')):
		vel_msg.angular.z = abs(0.5)
		vel_msg.linear.x = abs(0)
		mover.publish(vel_msg)
	if(tecla == ord('6')):
		vel_msg.angular.z = -abs(0.55)
		vel_msg.linear.x = abs(0)
	
	if(tecla == ord('s')):
		X = 10
		Y = 80
		THETA = 180
		for ff in range(0,3):
			Z = 0
			a = numpASy.array([X,Y,Z,THETA,G],dtype=numpy.float32)
			pub.publish(a)
			Z = 50
			a = numpy.array([X,Y,Z,THETA,G],dtype=numpy.float32)
			pub.publish(a)
		
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
