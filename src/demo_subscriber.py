#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def numCb(msg):
  print msg.data

rospy.init_node('subscriber_demo')

sub = rospy.Subscriber('number_communicate',Int32,numCb)

rospy.spin()
