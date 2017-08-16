#!/usr/bin/env python
import roslib
roslib.load_manifest('face_recognition')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

#from __future__ import print_function

class image_converter:
 
  def __init__(self):
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("imagen_face",Image,self.callback)

  def callback(self,data):
    cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    cv2.imshow("Rostro", cv_image)
    cv2.waitKey(3)

def main(args):
  ic = image_converter()
  rospy.init_node('imagen', anonymous=True)

  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':

    main(sys.argv)
