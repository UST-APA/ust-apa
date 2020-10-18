# Copyright (c) 2020 by APA Group. All Rights Reserved.
# -*- coding:utf-8 -*-
'''
@File: Graph.py
@Date: 2020/10/08
@Author: Haokun WANG
@Contact: hwangeh@connect.ust.hk
@Description:
'''
import pandas as pd
import networkx as nx

class Node(object):
    def __init__(self, name, altitude, location):
        self.name = name
        self.altitude = altitude
        self.location = location


class Edge(object):
    # TO DO: add indoor/outdoor flag
    def __init__(self, distance, weight, start, end):
        self.distance = distance
        self.weight = weight
        self.nodes = [start, end]


class Graph(object):
    def __init__(self):
        self.edgs = None
        self.nodes = None

    def draw_from_npy(self, file_name):
        pass

    def neighbors(self, node_name):
        return neighbors_name_list

    # def get_edge_data(self, node_a, node_b):
    #     edg = 
    #     return {'distance': edg.distance, 'weight': edg.weight}


def generate_graph(edges_csv, nodes_csv):
    graph = nx.Graph()
    edgelist = pd.read_csv(edges_csv)
    nodelist = pd.read_csv(nodes_csv)

    for i, element in edgelist.iterrows():
        graph.add_edge(element[0], element[1], 
                       weight=None,
                       distance=element[2], density=None, temp=None,
                       d_attitude=None, indoor=element[3], area=element[4])

    for i, element in nodelist.iterrows():
        graph.add_node(element[0], 
                       lat=element[1], lon=element[2], altitude=element[3], rename=element[4])

    return graph

