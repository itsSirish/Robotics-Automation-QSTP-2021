#! /usr/bin/python
import rospy
from q3_week2.srv import ang_vel, ang_velResponse
from std_msgs.msg import Float32

rospy.init_node("server_node")
response = ang_velResponse()
v=0.1

def serv_handler_function(request):

    response.w = v/request.radius
    
    print(response.w)
    return response

 
 
 
if __name__=='__main__' :
   
   serv=rospy.Service("/compute_ang_vel",ang_vel,serv_handler_function)
   rospy.loginfo("running succ")
   rospy.spin()