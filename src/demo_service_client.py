#!/usr/bin/env python

import rospy

from vejoe_slam.msg import Personinfo
from vejoe_slam.srv import PersoninfoShow

rospy.init_node('service_demo_client')

rospy.wait_for_service('show_person_info')

showClient = rospy.ServiceProxy('show_person_info',PersoninfoShow)

person = Personinfo()
person.name = 'Zac'
person.sex = True
person.age = 20

strPrint = showClient(person)

print 'format show:', strPrint
