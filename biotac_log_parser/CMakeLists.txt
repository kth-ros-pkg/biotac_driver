cmake_minimum_required(VERSION 2.8.3)
project(biotac_log_parser)

find_package(catkin REQUIRED COMPONENTS rospy biotac_sensors rosjson_time rosbag)

catkin_python_setup()

catkin_package(
    CATKIN_DEPENDS rospy biotac_sensors rosjson_time rosbag
)


install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/src
  DESTINATION ${CATKIN_PACKAGE_PYTHON_DESTINATION}
  FILES_MATCHING PATTERN "*.py"
)