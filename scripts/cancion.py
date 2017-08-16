#!/usr/bin/env python

import pyglet
import rospy
from std_msgs.msg import Int16

def callback(data):
	print("Calback")
	sound = pyglet.media.load('/home/rissa/Documentos/song.wav', streaming=False)
	sound.play()
	pyglet.app.run()

def listener():
    rospy.init_node('cancion', anonymous=True)
    rospy.Subscriber('cantar',Int16, callback)
    rospy.spin()
    

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass

