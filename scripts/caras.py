#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
import pyglet
import time
import sys
reload(sys)


def callback(data):
	sys.setdefaultencoding('Cp1252')
	print(data.data)
	print("la cara recibe")
	if (data.data == 1):
		ag_file = "Alegre.gif"
	if (data.data == 2):
		ag_file = "duda.gif"
		print("cara de duda")
	if (data.data == 3):
		ag_file = "Espera.gif"
	if (data.data == 4):
		ag_file = "Neutra.gif"
	if (data.data == 5):
		ag_file = "Sorpresa.gif"
	if (data.data == 6):
		ag_file = "Triste.gif"

	animation = pyglet.resource.animation(ag_file)
	sprite = pyglet.sprite.Sprite(animation)
	# create a window and set it to the image size
	##screen = display.get_screens()
	win = pyglet.window.Window(fullscreen=False)
	# set window background color = r, g, b, alpha
	# each value goes from 0.0 to 1.0
	green = 1, 1, 1, 1
	pyglet.gl.glClearColor(*green)
	@win.event
	def on_draw():
		win.clear()
		sprite.draw()
        pyglet.app.run()
	time.sleep(2)
        even_loop.exit()
def caras():


    rospy.init_node('caras', anonymous=True)
    rospy.Subscriber('expresion', Int16, callback)
    rospy.spin()

if __name__ == '__main__':
    caras()
