#!usr/bin/env python

from codecs import xmlcharrefreplace_errors
import rospy
from std_msgs.msg import String


    

    
def callback(msg):
    print(msg.data)
    pub_2.publish(msg.data)


rospy.init_node('subscriber_helloworld')
sub1=rospy.Subscriber('/hello',String,callback)
sub2=rospy.Subscriber('/world',String,callback)
pub_2=rospy.Publisher('/hello_world',String,queue_size=10)



rospy.spin()

    
