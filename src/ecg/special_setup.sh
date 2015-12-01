#!/bin/bash
# Assumes PATH_TO is from ros_ecgworkbench/scripts


export PATH_TO=$PWD/../src/ecg
export ECG_FED=FED1
python2.7 $PATH_TO/ecg_interface/robot_code/src/main/robots/cci_solver.py ProblemSolver &
#python2.7 $PATH_TO/ecg_interface/robot_code/src/main/robots/cci_solver.py ProblemSolver &

export JYTHONPATH=$JYTHONPATH:$PATH_TO/ecg_interface/framework_code/build/compling.core.jar:$PATH_TO/ecg_interface/framework_code/src/main/nluas/language
jython -m analyzer $PATH_TO/ecg_interface/ecg_grammars/compRobots.prefs &
#python2.7 $PATH_TO/ecg_interface/robot_code/src/main/robots/robots_ui.py AgentUI 

