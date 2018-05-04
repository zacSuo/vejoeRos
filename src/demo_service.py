#!/usr/bin/env python

import rospy

from vejoe_slam.srv import PersoninfoShow

def createStrCb(request):
  strResult = 'Person Name :' + request.person.name
  strResult += ' Age:' + str(request.person.age)
  if request.person.sex == True:
    strResult += ' Male'
  else:
    strResult += ' Female'
  return strResult

rospy.init_node('service_demo')

srv = rospy.Service('show_person_info',PersoninfoShow,createStrCb)

rospy.spin()
