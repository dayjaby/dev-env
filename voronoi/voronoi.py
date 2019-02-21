import networkx as nx
from scipy.spatial import Voronoi
import numpy as np

def map_to_graph(msg, distance=10.0):
    G = nx.Graph()
    points = []
    for x in range(msg.info.width):
        for y in range(msg.info.height):
            i = x + y*msg.info.width
            if msg.data[i] != 0:
                points.append([x,y])
    points = np.array(points)
    vor = Voronoi(points)
    nodes = []

    for i, v in enumerate(vor.vertices):
        node = (v[0], v[1])
        nodes.append(node)
        G.add_node(node)

    for i, ridge in enumerate(vor.ridge_vertices):
        p1, p2 = points[vor.ridge_points[i]]
        u, v = ridge
        if u >= 0 and v >= 0:
            v1, v2 = vor.vertices[ridge]
            d = v2 - v1
            if d[0] != 0:
                t = (p1[0] - v1[0]) / d[0]
            else:
                t = (p1[1] - v1[1]) / d[1]
            d1 = np.linalg.norm(v1+t*d - p1)
            if d[0] != 0:
                t = (p2[0] - v1[0]) / d[0]
            else:
                t = (p2[1] - v1[1]) / d[1]
            d2 = np.linalg.norm(v1+t*d - p2)
            if d1+d2>distance:
                G.add_edge(nodes[u], nodes[v], weight=np.linalg.norm(d))

    return G
