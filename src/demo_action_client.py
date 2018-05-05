#!/usr/bin/env python
import rospy

import actionlib
from vejoe_slam.msg import pushupAction, pushupGoal, pushupResult, pushupFeedback


class PushupActionClient(object):
	"""docstring for PushupActionClient"""
	def __init__(self, name):
		self.name = name
		self.rate = rospy.Rate(1)
		self._client = actionlib.SimpleActionClient('pushup',pushupAction)
		self._client.wait_for_server()

	def ShowWork(self):
		goal = pushupGoal()
		goal.push_up_count = 3
		self._client.send_goal(goal, feedback_cb = self.feedbackCb)
		self.showResult()

	def showInvalid(self):
		goal = pushupGoal()
		goal.push_up_count = 0
		self._client.send_goal(goal, feedback_cb = self.feedbackCb)
		self.showResult()

	def showCancel(self):
		goal = pushupGoal()
		goal.push_up_count = 3
		self._client.send_goal(goal, feedback_cb = self.feedbackCb)
		self.rate.sleep()
		self._client.cancel_goal()
		self.showResult()

	def showResult(self):
		self._client.wait_for_result()
		print 'exe result:', self._client.get_goal_status_text()

	def feedbackCb(self,feedback):
		print 'time used:', str(feedback.time_elapsed.to_sec())
		print 'finish:',str(feedback.finish_count)
		print 'remain:', str(feedback.remain_count)

if __name__ == '__main__':
	rospy.init_node('pushup_action_client')
	client = PushupActionClient(rospy.get_name())
	print '============='
	client.ShowWork()
	print '#############'
	client.showCancel()
	print '*************'
	client.showInvalid()
	rospy.spin()
