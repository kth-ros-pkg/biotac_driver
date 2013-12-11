cmake_minimum_required(VERSION 2.8.3)
project(rosjson_time)

find_package(catkin REQUIRED COMPONENTS rospy roslib)

catkin_python_setup()

catkin_package(
    CATKIN_DEPENDS rospy roslib
)

install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/src
  DESTINATION ${CATKIN_PACKAGE_PYTHON_DESTINATION}
  FILES_MATCHING PATTERN "*.py"
)