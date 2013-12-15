cmake_minimum_required(VERSION 2.8.3)
project(rosjson_time)

find_package(catkin REQUIRED COMPONENTS rospy roslib)

catkin_python_setup()

catkin_package(
    CATKIN_DEPENDS rospy roslib
)