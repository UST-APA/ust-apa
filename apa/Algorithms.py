# Copyright (c) 2020 by BionicDL Lab. All Rights Reserved.
# -*- coding:utf-8 -*-
'''
@File: Algorithms.py
@Date: 2020/10/08
@Author: Haokun WANG
@Contact: hwangeh@connect.ust.hk
@Description:
'''


class Algorithms(object):
    def __init__(self):
        pass

    def run(self, *args, **kwargs):
        raise NotImplementedError(' Does not implement run function. ')


class Dijakstra(Algorithms):
    import sys
    MAX = sys.maxsize
    PATH = []
    V = []
    DIST = {}
    PREV = {}
    RELAXED_NODES = []
    ORDER = 0
    FLAG = 0

    def __init__(self):
        super(Model, self).__init__()

    def run(self, graph, source_name, target_name):
        for node in list(graph.nodes):
            self.DIST[node.name] = self.MAX
            self.PREV[node.name] = None
            self.V.append(node.name)
        self.DIST[source_name] = 0

        if source_name == target_name:
            return DIST, PREV

        while len(self.V) != 0:
            self.ORDER += 1
            self.DIST = sorted(self.DIST.items(), key=lambda x: x[1], reverse=False)
            for i in range(len(self.DIST)):
                if self.DIST[i][0] in self.V:
                    u = self.DIST[i][0]
                    break
            self.V.remove(u)
            self.DIST = dict(self.DIST)
            
            for v in graph.neighbors(u):
                if v in self.V:
                    alt = self.DIST[u] + graph.get_edge_data(u, v)['weight']
                    if alt < self.DIST[v]:
                        self.DIST[v] = alt
                        self.PREV[v] = u
                    if v == target_name:
                        self.FLAG = 1
                    self.RELAXED_NODES.append([v, self.ORDER])
            if self.FLAG == 1:
                break
        return self.DIST, self.PREV, self.RELAXED_NODES

    def obtain_path(self, prev, target_name):
        path = []
        relaxed_nodes = []
        tem_node = target_name
        while tem_node is not None:
            path.append(tem_node)
            tem_node = prev[tem_node]
        path.reverse()
        return path