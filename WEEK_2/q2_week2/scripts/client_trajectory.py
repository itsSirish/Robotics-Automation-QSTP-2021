#! /usr/bin/python
import rospy
import numpy as np
from q2_week2.srv import robot_states, robot_statesRequest
import matplotlib.pyplot as plt





def plot_graph(x,y,theta,v,w):
    rospy.init_node('service_client')

    rospy.wait_for_service('/trajectory_srv')
    client_trajectory = rospy.ServiceProxy('/trajectory_srv', robot_states)
    trajectory_object = robot_statesRequest()
    trajectory_object.x=x
    trajectory_object.y=y
    trajectory_object.theta=theta
    trajectory_object.v=v
    trajectory_object.w=w
    final_pos = client_trajectory(trajectory_object)
    print(final_pos.x_cord)
    print(final_pos.y_cord)


if __name__ == '__main__':
    plot_graph(0.0,0.0,0.0,1.0,0.5)