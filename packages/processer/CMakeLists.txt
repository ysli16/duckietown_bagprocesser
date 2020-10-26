cmake_minimum_required(VERSION 2.8.3)
project(processer)

find_package(catkin REQUIRED COMPONENTS
  rospy
  rosbag
  cv_bridge
)

catkin_package()
