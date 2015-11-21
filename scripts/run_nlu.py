#!/usr/bin/env python
import rospy
import inspect



from ecg.ecg import UserAgentSolver

if __name__=="__main__":

    rospy.loginfo("Starting NLU")

    rospy.init_node("ecg_nlu")

    uas = NLUSystem()

    while True:
        print "Please enter text; press ENTER to quit."
        text = raw_input()

        if text == "":
            break
        
        command = uas.parse(text)

        
    
    rospy.loginfo("NLU quit")