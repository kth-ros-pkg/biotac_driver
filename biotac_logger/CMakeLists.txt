cmake_minimum_required(VERSION 2.8.3)
project(biotac_logger)

find_package(catkin REQUIRED COMPONENTS rospy biotac_sensors rosjson_time)

catkin_python_setup()

catkin_package(
    CATKIN_DEPENDS rospy biotac_sensors rosjson_time
)

install(PROGRAMS scripts/biotac_json_logger.py 
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})