#!/usr/bin/env python
import rospy
import inspect
<<<<<<< HEAD
from std_msgs.msg import *
from ecg_uas.ecg_uas import UserAgentSolver
from gazebo_msgs.msg import ModelStates,LinkStates
=======



from ecg.ecg import UserAgentSolver
>>>>>>> 3a74ad6af6299623e78892fb1f48bb47f7f24466

if __name__=="__main__":

    rospy.loginfo("Starting NLU")

    rospy.init_node("ecg_nlu")

<<<<<<< HEAD
    uas = UserAgentSolver()
    pub = rospy.Publisher('/cqi/command', String, queue_size=5)
    rospy.sleep(1)
=======
    uas = NLUSystem()
>>>>>>> 3a74ad6af6299623e78892fb1f48bb47f7f24466

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