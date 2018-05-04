#!/usr/bin/env python

import rospy
from vejoe_slam.msg import Personinfo

rospy.init_node('publish_demo')

pub = rospy.Publisher('person_communicate',Personinfo)

rate = rospy.Rate(5)

while not rospy.is_shutdown():
  tmpMsg = Personinfo()
  tmpMsg.name = 'Zac'
  tmpMsg.sex = True
  tmpMsg.age = 20
  pub.publish(tmpMsg)
  rate.sleep()

