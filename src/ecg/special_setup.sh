#!/bin/bash
# Assumes PATH_TO is from ros_ecgworkbench/scripts

echo Running
export PATH_TO=$PWD/../src/ecg

#export PATH_TO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd )"
export ECG_FED=FED1
#export SOLVER=ecg/ecg_interface/robot_code/src/main/robots/ros_solver.py ProblemSolver
python2.7 $PATH_TO/ecg_interface/robot_code/src/main/robots/ros_solver.py ProblemSolver &
#python2.7 $PATH_TO/$SOLVER &
#python2.7 ecg_interface/robot_code/src/main/robots/ros_solver.py ProblemSolver &

export JYTHONPATH=$JYTHONPATH:$PATH_TO/ecg_interface/framework_code/build/compling.core.jar:$PATH_TO/ecg_interface/framework_code/src/main/nluas/language
jython -m analyzer $PATH_TO/ecg_interface/ecg_grammars/compRobots.prefs &
python2.7 $PATH_TO/ecg_interface/robot_code/src/main/robots/robots_ui.py AgentUI 
