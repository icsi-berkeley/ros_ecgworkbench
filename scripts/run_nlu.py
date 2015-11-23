#!/usr/bin/env python
import rospy
import inspect

from std_msgs.msg import *
from ecg_uas.ecg_uas import UserAgentSolver
from gazebo_msgs.msg import ModelStates,LinkStates




from ecg.ecg import UserAgentSolver


if __name__=="__main__":

    rospy.loginfo("Starting NLU")

    rospy.init_node("ecg_nlu")


    uas = UserAgentSolver()
    pub = rospy.Publisher('/cqi/command', String, queue_size=5)
    rospy.sleep(1)

    # Commented this out for now... Sean, please fix as appropriate. 
    # uas = NLUSystem()


    while True:
        print "Please enter destination; press ENTER to quit."
        print "Possible destinations: "
        for item in uas.modelPoses.keys():
            print item

        text = raw_input()

        if text == "":
            break
        
        command = uas.parse(text)

        rospy.loginfo("Publishing CQI command " + command)

        pub.publish(String(command))

        
    
    rospy.loginfo("NLU quit")