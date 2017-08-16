#!/usr/bin/env python

import rospy
from face_recognition.msg import FaceRecognitionActionFeedback

def nombre(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.feedback.names)
    nombre_encontrado = str(data.feedback.names)
    a = nombre_encontrado.replace("[","")
    b = a.replace("]","")
    c = b.replace("'","")
    print(c)

def faces():

    rospy.init_node('rostros', anonymous=True)

    rospy.Subscriber('/face_recognition/feedback', FaceRecognitionActionFeedback, nombre)

    rospy.spin()

if __name__ == '__main__':
    faces()
