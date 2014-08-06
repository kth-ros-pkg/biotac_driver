cmake_minimum_required(VERSION 2.8.3)
project(cheetah_lib)

set(CHEETAH_VERSION v3.05)
set(TARBALL_NAME cheetah-library-${CHEETAH_VERSION})

include(ExternalProject)
ExternalProject_Add(cheetah_
  PREFIX ${CMAKE_CURRENT_BINARY_DIR}
  DOWNLOAD_DIR ${CMAKE_CURRENT_BINARY_DIR}/download
  URL http://csc.kth.se/~fevb/downloads/${TARBALL_NAME}.zip
  CONFIGURE_COMMAND ""
  BINARY_DIR ""
  BUILD_COMMAND ""
  INSTALL_COMMAND "" 
)

add_custom_target(
  copy_cheetah ALL
  COMMAND cmake -E copy ${CMAKE_CURRENT_BINARY_DIR}/src/cheetah_/cheetah.so ${CATKIN_DEVEL_PREFIX}/${CATKIN_GLOBAL_LIB_DESTINATION}/cheetah.so)

add_library(cheetah SHARED)
set_target_properties(cheetah PROPERTIES LINKER_LANGUAGE CXX)

add_dependencies(copy_cheetah cheetah)
add_dependencies(copy_cheetah cheetah_)
add_dependencies(cheetah_ cheetah)

catkin_package(
    DEPENDS
    CATKIN_DEPENDS
    INCLUDE_DIRS 
    LIBRARIES cheetah
)