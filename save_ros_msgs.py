from rospy_message_converter import message_converter
from sitebots_msgs.msg import GeometryGraph
from nav_msgs.msg import OccupancyGrid

import rospy
import json
import functools

def msg_callback(filename, msg):
    d = message_converter.convert_ros_message_to_dictionary(msg)
    with open("voronoi/map.json", "w") as outfile:
        json.dump(d, outfile)

rospy.init_node("save_ros_msgs")

subscriptions = {
    "voronoi/map.json": ("/web/map", OccupancyGrid)
}

for filename, subscription in subscriptions.items():
    rospy.Subscriber(subscription[0], subscription[1], functools.partial(msg_callback, filename))

ros_rate = rospy.Rate(10)
while not rospy.is_shutdown():
    ros_rate.sleep()
