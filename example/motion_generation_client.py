#!/usr/bin/env python3
import numpy as np 
import rospy
from geometry_msgs.msg import PoseStamped
from ros_dmp.srv import *
import os

if __name__ == "__main__":

    rospy.init_node('generate_motion_service_test_client')
    req = GenerateMotionRequest() # type: ignore

    # Compose request message
    folder = rospy.get_param('/learn_dmp_service_node/weights_file_path', '../../data/weights/')
    req.dmp_name = os.path.join(folder, "example.yaml")
    req.tau = 1.0
    req.dt = 0.01
    req.goal_pose = PoseStamped()
    req.goal_pose.header.frame_id = "map"
    req.goal_pose.pose.position.x = 4.0
    req.goal_pose.pose.position.y = 4.0
    req.goal_pose.pose.position.z = 1.0
    req.goal_pose.pose.orientation.x = 1.0
    req.goal_pose.pose.orientation.y = 1.0
    req.goal_pose.pose.orientation.z = 1.0
    req.goal_pose.pose.orientation.w = 1.0
    req.initial_pose.header.frame_id = "map"
    req.initial_pose.pose.position.x = 0.0
    req.initial_pose.pose.position.y = 0.0
    req.initial_pose.pose.position.z = 0.0
    req.initial_pose.pose.orientation.x = 1.0
    req.initial_pose.pose.orientation.y = 1.0
    req.initial_pose.pose.orientation.z = 1.0
    req.initial_pose.pose.orientation.w = 1.0

    try:
        service_client = rospy.ServiceProxy('/generate_motion_service', GenerateMotion) # type: ignore
        rospy.loginfo(service_client(req))
    except :
        rospy.loginfo("Service call failed")
    