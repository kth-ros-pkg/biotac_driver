cmake_minimum_required(VERSION 2.8.3)
project(biotac_log_parser)

find_package(catkin REQUIRED COMPONENTS rospy biotac_sensors rosjson_time rosbag)

catkin_python_setup()

catkin_package(
    CATKIN_DEPENDS rospy biotac_sensors rosjson_time rosbag
)

install(PROGRAMS src/parse_log_hdf5.py src/parse_log_json.py src/parse_log_pytable.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})