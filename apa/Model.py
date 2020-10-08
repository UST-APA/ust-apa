# Copyright (c) 2020 by BionicDL Lab. All Rights Reserved.
# -*- coding:utf-8 -*-
'''
@File: Model.py
@Date: 2020/10/08
@Author: Haokun WANG
@Contact: hwangeh@connect.ust.hk
@Description:
'''

class Model(object):
    def __init__(self):
        pass

    def initial_data(self, *args, **kwargs):
        raise NotImplementedError(' Does not implement initial_data function. ')

    def update_weight(self, *args, **kwargs):
        raise NotImplementedError(' Does not implement update_weight function. ')

    def update_graph(self, *args, **kwargs):
        raise NotImplementedError(' Does not implement update_graph function. ')


class SimpleModel(Model):
    def __init__(self, data_seeds):
        super(Model, self).__init__()
        self.initial_data(data_seeds)
        self.super_parameters = [w0, w1, w2, w3]
        
    def initial_data(self, data_seeds):
        self.density_seed = data_seeds['density']
        self.temperature_seed = data_seeds['temperature']

    def update_weight(self, node_a, node_b, edge, t):
        # TO_DO: get_io_flag(), get_distance(), get_altitude(), f(dens), g(tem, io)
        io = edge.get_io_flag()
        distance = edge.distance
        altitude = node_a.altitude - node_b.altitude
        density = self.density_seed.run(t)
        temperature = self.temperature_seed.run(t)

        weight = np.array(self.super_parameters).dot(np.array([distance, altitude, self.f(density), self.g(temperature, io)]))

        edge.weight = weight

    def update_graph(self, graph, t):
        for edge in graph.edgs:
            self.update_weight(edge.nodes[0], edge.nodes[1], edge, t)
        return graph

    def f(self, density):
        return 0
    
    def g(self, temperature, io):
        return 0
