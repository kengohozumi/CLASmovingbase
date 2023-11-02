cmake_minimum_required(VERSION 2.8.3)
project(CLASmovingbase)
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  tf
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES py_lecture
#  CATKIN_DEPENDS roscpp rospy std_msgs tf
#  DEPENDS system_lib
)
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)


