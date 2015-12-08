#!/usr/bin/env python
import rospy
import subprocess
import os

from robots.robots_ui import RobotUserAgent
if __name__=="__main__":
    dir_name = os.path.dirname(os.path.realpath(__file__))
    path = dir_name + "/../src/ecg/special_setup.sh"
    #path = os.getcwd() + "/../src/ecg/special_setup.sh"
    rospy.loginfo("Starting NLU system...")
    rospy.init_node("ecg_nlu")

    subprocess.Popen(["sh", path])
    rua = RobotUserAgent(["AgentUI"])
    rua.prompt()


