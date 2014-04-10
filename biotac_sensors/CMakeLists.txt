cmake_minimum_required(VERSION 2.8.3)
project(biotac_sensors)

find_package(catkin REQUIRED COMPONENTS roscpp cheetah_lib message_generation std_msgs)


include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

link_directories(${catkin_LIBRARY_DIRS})

add_message_files(
  DIRECTORY msg
  FILES
    BioTacData.msg
    BioTacHand.msg
    BioTacTime.msg
)

generate_messages(
  DEPENDENCIES std_msgs
)

catkin_package(
  DEPENDS 
  CATKIN_DEPENDS message_runtime roscpp cheetah_lib std_msgs
  INCLUDE_DIRS include
  LIBRARIES
)

add_executable(biotac_pub src/biotac.c src/cheetah.c src/biotac_hand_class.cpp src/biotac_pub.cpp)
target_link_libraries(biotac_pub ${catkin_LIBRARIES} -ldl)
add_dependencies(biotac_pub ${PROJECT_NAME}_gencpp)

install(TARGETS biotac_pub
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
