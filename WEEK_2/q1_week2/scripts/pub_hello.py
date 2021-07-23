#!usr/bin/env python

import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    rospy.init_node('hello_node')
    pub=rospy.Publisher('/hello',String,queue_size=10)
    rate=rospy.Rate(2)
    while not rospy.is_shutdown():
        msg=String()
        msg.data="Hello,"
        pub.publish(msg.data)
        rate.sleep()

