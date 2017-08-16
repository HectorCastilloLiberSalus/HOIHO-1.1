#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import rospy
from espeak import espeak
from std_msgs.msg import String
#espeak.synth('Hello, world')
#espeak.list_voices()# Ver lista de idiomas
#Ingles EUA 'en'
#Español lationoamerica 'es-la'
#Alema 'de'
global lang
lang = 'en'
espeak.set_parameter(espeak.Parameter.Pitch, 50) # proporcional con el grado de agudeza de la voz
espeak.set_parameter(espeak.Parameter.Rate, 150) # proporcional con la velocidad de las voces
espeak.set_parameter(espeak.Parameter.Range, 700)

def texto(data):
	global lang
	espeak.set_voice(lang)
	espeak.synth(data.data)

def idioma(data):
	global lang
	espeak.set_voice(data.data)
	lang = data.data
def tts():

	rospy.init_node('tts_espeak',anonymous=True)
	rospy.Subscriber("idioma",String,idioma)
	rospy.Subscriber("text",String,texto)
	rospy.spin()

if __name__=='__main__':
	tts()
