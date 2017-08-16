#!/usr/bin/env python

#!/usr/bin/env python  
import rospy
import tf
import geometry_msgs.msg
import numpy
from beginner_tutorials.msg import Num
import time

if __name__ == '__main__':
    rospy.init_node('tf_lookup_example')

    listener = tf.TransformListener()

    rate = rospy.Rate(5)
    X = 90
    Y = 180
    Z = 150
    THETA = 40
    G = 04
    it = 0

    while not rospy.is_shutdown():
        try:
            pubD = rospy.Publisher('derecho', Num, queue_size=10)
            pub = rospy.Publisher('izquierdo', Num, queue_size=10)

            (trans,rot) = listener.lookupTransform('/head_1', '/right_shoulder_1', rospy.Time(0))
            (trans1,rot1) = listener.lookupTransform('/right_shoulder_1', '/right_elbow_1',rospy.Time(0))
		
            #rospy.loginfo("Distance between the hands is = {0:f}".format(np.linalg.norm(trans)))
	    print(rot)
	    if (it == 10):		  
		Xt =round( (180*rot[1]) + 90)
 		Yt =round( (200*rot[2]) + 110)
 		Zt =round( (257*rot1[1])+ 180)	
		print(Xt)	
		if (Xt <= 5):
			Xt = 5
		if (Yt>= 180):
			Yt = 180	
		if (Yt<=90):
			Yt = 90
		if (Zt>=180):
			Zt=180
		if (Zt<=5):
			Zt=5
		if (Xt>X-10 and Xt<X+10):
			X = Xt
		if (Yt>Y-10 and Yt<Y+10):
			Y = Yt
		if (Zt>Z-10 and Zt<Z+10):
			Z = Zt
		#print(X)
		i = numpy.array([X,Y,Z,THETA,G],dtype=numpy.float32)
		rospy.loginfo(i)		
		pub.publish(i) 
            	rate.sleep()
		it = 0
	    it = it +1 

	    #time.sleep(5)  
	    #rospy.spin()      
	except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        #rate.sleep()
