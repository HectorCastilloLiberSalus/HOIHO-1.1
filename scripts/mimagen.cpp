#include <ros/ros.h>
#include <actionlib/server/simple_action_server.h>
#include <face_recognition/FaceRecognitionAction.h>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>
#include <sensor_msgs/image_encodings.h>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <vector>
#include <cvaux.h>
#include <cxcore.hpp>
#include <sys/stat.h>
#include <termios.h>
#include <unistd.h>
#include "face_recognition_lib.cpp"

using namespace std;

class FaceRecognition
{
public:
    
  FaceRecognition(std::string name) : 
    frl(),
    it_(nh_),
    pnh_("~"),
    as_(nh_, name, boost::bind(&FaceRecognition::executeCB, this, _1), false)
  {
    //a face recognized with confidence value higher than the confidence_value threshold is accepted as valid.
    pnh_.param<double>("confidence_value", confidence_value, 0.88);
    //if output screen is shown
    pnh_.param<bool>("show_screen_flag", show_screen_flag, true);
    ROS_INFO("show_screen_flag: %s", show_screen_flag ? "true" : "false");
    //a parameter for the "add_face_images" goal which determines the number of training images for a new face (person) to be acquired from the video stream 
    pnh_.param<int>("add_face_number", add_face_number, 25);
    add_face_number = 25;
    //the number of persons in the training file (train.txt)
    person_number=0;
    //starting the actionlib server
    as_.start();
    //if the number of persons in the training file is not equal with the number of persons in the trained database, the database is not updated and user should be notified to retrain the database if new tarining images are to be considered.

  }


void imageCB(const sensor_msgs::ImageConstPtr& msg)
  {
  


    IplImage img_input = cv_ptr->image;
    IplImage *img= cvCloneImage(&img_input); 
    IplImage *greyImg;
    IplImage *faceImg;
    IplImage *sizedImg;
    IplImage *equalizedImg;
    CvRect faceRect;

    greyImg = frl.convertImageToGreyscale(img);

    faceRect = frl.detectFaceInImage(greyImg,frl.faceCascade);


      cvRectangle(img, cvPoint(faceRect.x, faceRect.y), cvPoint(faceRect.x + faceRect.width-1, faceRect.y + faceRect.height-1), CV_RGB(0,255,0), 1, 8, 0);
    




       cvShowImage("Input", img); /// MOdificar aqui para apublicar la imagen.
       cvWaitKey(1);
  
    r.sleep();
    mutex_.unlock();
    return;		
  }




int main(int argc, char** argv)
{
  ros::init(argc, argv, "mimagen");
//  FaceRecognition face_recognition(ros::this_node::getName());
  ros::NodeHandle n;
  ros::Suscriber sub = n.Subscribe("/camera/image_raw", 1, &FaceRecognition::imageCB, this);
//CvRect faceRect;
  //faceRect = frl.detectFaceInImage(greyImg,frl.faceCascade);
  //cvRectangle(img, cvPoint(faceRect.x, faceRect.y), cvPoint(faceRect.x + faceRect.width-1, faceRect.y + faceRect.height-1), CV_RGB(0,255,0), 1, 8, 0);
  ros::spin();
 
 return 0;
}

