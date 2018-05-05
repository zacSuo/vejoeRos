#! /usr/bin/env python

import rospy

import time
import actionlib
from vejoe_slam.msg import pushupAction, pushupGoal, pushupResult,pushupFeedback


class PushupAction(object):
	"""docstring for PushupAction"""
	def __init__(self, name):
		self.name = name
		self._server = actionlib.SimpleActionServer('pushup',pushupAction,execute_cb=self.executeCb,auto_start=False)
		self._server.start()
		

	def executeCb(self,goal):
		result = pushupResult()
		startTime = time.time()
		rate = rospy.Rate(1)
		idx = 0
		if goal.push_up_count <= 0:		
			result.time_used = rospy.Duration.from_sec(time.time() - startTime)
			self._server.set_aborted(result,"Number is invalid.")
			return

		while(idx < goal.push_up_count):
			if self._server.is_preempt_requested():
				result.time_used = rospy.Duration.from_sec(time.time() - startTime)
				self._server.set_preempted(result,"Other Client Send Command")
				return

			feedback = pushupFeedback()
			feedback.time_elapsed = rospy.Duration.from_sec(time.time() - startTime)
			feedback.finish_count = idx
			feedback.remain_count = goal.push_up_count - idx
			self._server.publish_feedback(feedback)

                        idx += 1

			rate.sleep()

		result.time_used = rospy.Duration.from_sec(time.time() - startTime)
		self._server.set_succeeded(result,"Finish push-up")


if __name__ == '__main__':
	rospy.init_node('pushup_action')
	PushupAction(rospy.get_name())
	rospy.spin()
