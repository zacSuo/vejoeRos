#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

rospy.init_node('publish_demo')

pub = rospy.Publisher('number_communicate',Int32)

rate = rospy.Rate(5)

idx=0
while not rospy.is_shutdown():
  pub.publish(idx)
  idx+=1
  rate.sleep()

