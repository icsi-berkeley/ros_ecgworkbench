#!/usr/bin/env python
import rospy
import subprocess
import os

from robots.robots_ui import RobotUserAgent
if __name__=="__main__":
    path = os.getcwd() + "/../src/ecg/test.sh"
    #path = os.getcwd() + "/../src/ecg/special_setup.sh"
    rospy.loginfo("Starting NLU system...")
    rospy.init_node("ecg_nlu")

    subprocess.Popen(["sh", path])
    rua = RobotUserAgent(["AgentUI"])
    rua.prompt()


