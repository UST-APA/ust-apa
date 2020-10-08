# Copyright (c) 2020 by BionicDL Lab. All Rights Reserved.
# -*- coding:utf-8 -*-
'''
@File: Graph.py
@Date: 2020/10/08
@Author: Haokun WANG
@Contact: hwangeh@connect.ust.hk
@Description:
'''

class Node(object):
    def __init__(self, name, altitude, location):
        self.name = name
        self.altitude = altitude
        self.location = location


class Edge(object):
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

    def get_edge_data(self, node_a, node_b):
        edg = 
        return {'distance': edg.distance, 'weight': edg.weight}