#! /usr/bin/python
import rospy
import numpy as np
import matplotlib.pyplot as plt
from q2_week2.srv import robot_states, robot_statesResponse
dt=0.05
n=50
response = robot_statesResponse() 

def response_callback(request):
    

    x_points=[]
    y_points=[]
    for i in range(0,n):
       
        #response.x_cord.append(request.x)
        #response.y_cord.append(request.y)
        response.x_cord=(request.v*np.sin(request.w*i*dt+request.theta)/request.w) -(request.v*np.sin(request.theta)/request.w)
        response.y_cord=-(request.v*np.cos(request.w*i*dt+request.theta)/request.w) +(request.v*np.cos(request.theta)/request.w)
        x_points.append(response.x_cord)
        y_points.append(response.y_cord)
    plt.xlabel("X-Coordinates")
    plt.ylabel("Y-Coordinates")
    plt.plot(x_points,y_points, color="red", alpha=0.75)
    plt.grid()
    plt.show()
    return response

if __name__ == '__main__':
    rospy.init_node('server_node')
    # create the Service called my_service with the defined callback

    # subscribe to the /scan topic and get the required data


    service_trajectory = rospy.Service('/trajectory_srv', robot_states, response_callback)
    rospy.loginfo("Custom service is running!")
    rospy.spin() # maintain the service open.