#! /usr/bin/python
import rospy
from std_msgs.msg import Float32
from q3_week2.srv import ang_vel, ang_velRequest
from geometry_msgs.msg import Twist

import time
import math
v=0.1
rospy.init_node("client_node")

def radius(message):
    msg=message.data
    print(msg)
    client(msg)

def client(val):
    rospy.wait_for_service('compute_ang_vel')
    rospy.loginfo("Service is running!")
    
    service_client = rospy.ServiceProxy('compute_ang_vel', ang_vel)
    radius_obj=ang_velRequest()
    radius_obj.radius=val
    angular_vel=service_client(radius_obj)
    print(angular_vel.w)
    move_infinity(angular_vel.w)
    

def move_infinity(vel):
    vel_cmd=Twist()
    path=rospy.Publisher('/cmd_vel',Twist,queue_size=10)

    while not rospy.is_shutdown():

        vel_cmd.linear.x=v
        vel_cmd.angular.z=vel
        path.publish(vel_cmd)

        r=rospy.Rate(5)    
        r.sleep
if __name__=='__main__' :
    subs=rospy.Subscriber("/radius_topic",Float32,radius)
    rospy.spin()