#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

minDistance = 1

def scanCb(msg):
	global minDistance
	minDistance = min(msg.ranges)
#	print minDistance

scan_sub = rospy.Subscriber('scan',LaserScan,scanCb)
cmd_vel_pub = rospy.Publisher('cmd_vel',Twist,queue_size=1)
rospy.init_node('move_turn')

move_twist = Twist()
move_twist.linear.x = 0.5
turn_twist = Twist()
turn_twist.angular.z = 0.5

light_change_time = rospy.Time.now()
rate = rospy.Rate(10)

while not rospy.is_shutdown():
	print minDistance
	if math.isnan(minDistance) or minDistance <= 1 :
		cmd_vel_pub.publish(turn_twist)
	else:
		cmd_vel_pub.publish(move_twist)
	rate.sleep()
