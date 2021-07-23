#! /usr/bin/python
import rospy
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist


rospy.init_node("radius_node")
radius=0.5
while not rospy.is_shutdown():
    radius_pub = rospy.Publisher('/radius_topic',Float32, latch= True, queue_size=10)
    radius_pub.publish(radius)
    r=rospy.Rate(5)
    r.sleep()
    