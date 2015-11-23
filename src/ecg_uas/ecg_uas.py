#!/usr/bin/env python
from geometry_msgs.msg import Twist,Pose,Quaternion,Point
from gazebo_msgs.msg import ModelStates,LinkStates
import rospy

class UserAgentSolver:
	def __init__(self):
		self.modelPoses = {}
		self.sub = rospy.Subscriber("/gazebo/model_states",ModelStates,self._cb_modeldata,queue_size=1)
        rospy.sleep(1)
		# return

	# Callback function to store the model poses of objects in the environment.         
	def _cb_modeldata(self,msg):
		# print "cb model called"
		for pos,item in enumerate(msg.name):            
			# print item
			self.modelPoses[item] = msg.pose[pos]

	def parse(self,text):
		
		# Some stuff to play around with...
		x = 5
		y = 5
		for item,pos in self.modelPoses.items():
			if text == item:
				print "Yes, there is " + item + "! I'll go there!"
				x = pos.position.x
				y = pos.position.y
				break


		# Insert code to connect to ECG User Agent and Solver here

		commandName = "moveToXY"
		commArgs = [x,y]

		
		# Generate a string from command name and arguments (ROS can not send lists or tuples as messages, but Strings work. )
		retStr = commandName + "(" 
		for a in commArgs:
			retStr += str(a) + ","
		retStr = retStr[:-1] + ")"
		return retStr

	

