from rospy_message_converter import message_converter
from sitebots_msgs.msg import GeometryGraph
from nav_msgs.msg import OccupancyGrid
from networkx.readwrite import json_graph

import rospy
import json
import os

from voronoi import map_to_graph
from util import hashabledict

from graph_processing import *

if os.path.isfile("voronoi.json"):
    with open("voronoi.json") as infile:
        js_graph = hashabledict(json.load(infile))
        G = json_graph.node_link_graph(js_graph)
else:
    with open("map.json") as outfile:
        map_msg = message_converter.convert_dictionary_to_ros_message("nav_msgs/OccupancyGrid", json.load(outfile))
        G = map_to_graph(map_msg, distance=10.0)
        with open("voronoi.json", "w") as outfile2:
            outfile2.write(json.dumps(json_graph.node_link_data(G)))

