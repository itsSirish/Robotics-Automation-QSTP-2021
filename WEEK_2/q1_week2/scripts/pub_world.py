#!usr/bin/env python

import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    rospy.init_node('world_node')
    pub=rospy.Publisher('/world',String,queue_size=10)
    rate=rospy.Rate(2)
    while not rospy.is_shutdown():
        msg=String()
        msg.data="World!"
        pub.publish(msg.data)
        rate.sleep()