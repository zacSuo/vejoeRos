#!/usr/bin/env python

import rospy
from vejoe_slam.msg import Personinfo

def personCb(msg):
  print 'Name is : ', msg.name
  print 'Age is : ', msg.age
  if msg.sex == True:
    print 'Male'
  else:
    print 'Female'

rospy.init_node('subscriber_demo')

sub = rospy.Subscriber('person_communicate',Personinfo,personCb)

rospy.spin()
