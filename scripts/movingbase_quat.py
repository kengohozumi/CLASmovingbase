#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Imu
import math
import tf

class movingbaseNode:
    def __init__(self):
        # Initialize message and publisher
        self.sub_movingbase  = rospy.Subscriber('movingbase_yaw',Imu,self.movingbase_callback) 
        self.movingbase_msg = Imu()
        self.heading_pub = rospy.Publisher('movingbase/quat', Imu, queue_size=10)
        self.movingbase_info = []
        
    def movingbase_callback(self,data):
        rospy.loginfo('ok')
        self.movingbase_data = data
        self.movingbase_info.append(data.header.stamp)#0
        self.movingbase_info.append(data.orientation.z)#2 yaw
        
    def movingbase_publish_msg(self):
        rate = rospy.Rate(10)
        if len(self.movingbase_info) != 0:
            #print(self.movingbase_data.orientation.z)
            roll = 0
            pitch = 0
            q = tf.transformations.quaternion_from_euler(roll, pitch, self.movingbase_data.orientation.z)        
            #print("orientation.x",q1,"orientation.y",q2,"orientation.z",q3,"orientation.w",q0)
            self.movingbase_msg.header.stamp = rospy.Time.now()###########################################
            self.movingbase_msg.header.frame_id = "imu_link"
            self.movingbase_msg.orientation.x = q[0]
            self.movingbase_msg.orientation.y = q[1]
            self.movingbase_msg.orientation.z = -q[2]
            self.movingbase_msg.orientation.w = q[3]
            self.heading_pub.publish(self.movingbase_msg)        
            self.movingbase_info.clear()
    
        
if  __name__ == "__main__":
    # init node
    rospy.init_node("movingbase")
    movingbasequo = movingbaseNode()####
    while not rospy.is_shutdown():
        movingbasequo.movingbase_publish_msg()
