# Copyright (c) 2020 by APA Group. All Rights Reserved.
# -*- coding:utf-8 -*-
'''
@File: Model.py
@Date: 2020/10/08
@Author: Haokun WANG
@Contact: hwangeh@connect.ust.hk
@Description:
'''
import math
import numpy as np

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
        self.super_parameters = [10, 1, 8, 3.5]
        
    def initial_data(self, data_seeds):
        # TO DO: temperature can be a interface from Internet
        self.density_seed = data_seeds['density']
        self.temperature_seed = data_seeds['temperature']

    def update_weight(self, edge, graph, t):
        # TO_DO: get_io_flag(), get_distance(), get_altitude(), f(dens), g(tem, io)
        node_a = edge[0]
        node_b = edge[1]

        distance = graph[node_a][node_b]['distance']
        d_altitude = graph.nodes[node_a]['altitude'] - graph.nodes[node_b]['altitude']
        area = graph[node_a][node_b]['area']
        io = graph[node_a][node_b]['indoor']
        density = self.density_seed.run(t, area)
        temperature = self.temperature_seed.run(t)

        weight = np.array(self.super_parameters).dot(np.array([distance, d_altitude, self.f(density, t), self.g(temperature, io)]))

        # update edge
        graph[node_a][node_b]['weight'] = weight
        graph[node_a][node_b]['density'] = density
        graph[node_a][node_b]['temp'] = temperature
        graph[node_a][node_b]['d_altitude'] = d_altitude

    def update_graph(self, graph, t):
        for edge in graph.edges:
            self.update_weight(edge, graph, t)
        return graph

    def f(self, density, t):
        sample = np.random.normal(loc=density, scale=0.01*density, size=1)
        return sample[0]
    
    def g(self, temperature, io):
        if io:
            return temperature
        else:
            return 2*temperature


class TemperatureSeed(object):
    def __init__(self, name, tem):
        self.name = name
        self.tem = tem

    def run(self, time):
        return self.tem


class DensitySeed(object):
    def __init__(self, name):
        self.name = name

    def run(self, time, area):
        if area==1:
            return self.density_area1(time)
        elif area==2:
            return self.density_area2(time)
        elif area==3:
            return self.density_area3(time)
        else:
            return self.density_area4(time)

    def density_area1(self, time):
        if 6<=time<9:
            density=self.func_a1(time)
        elif 9<=time<10.7:
            density=self.func_a2(time)
        elif 10.7<=time<14.75:
            density=self.func_a3(time)
        elif 14.75<=time<16.85:
            density=self.func_a4(time)
        elif 16.85<=time<22:
            density=self.func_a5(time)
        else:
            density=self.func_a6(time)
        return density

    def density_area2(self, time):
        if 6<=time<7.33:
            density=self.func_b1(time)
        elif 7.33<=time<9:
            density=self.func_b2(time)
        elif time==9:
            density=self.func_b3(time)
        elif 9<time<11.43:
            density=self.func_b4(time)
        elif time==11.43:
            density=self.func_b5(time)
        elif 11.43<time<14.2:
            density=self.func_b6(time)
        elif 14.2<=time<16.6:
            density=self.func_b7(time)
        elif 16.6<=time<18.55:
            density=self.func_b8(time)
        elif 18.55<=time<22:
            density=self.func_b9(time)
        else:
            density=self.func_b10(time)
        return density

    def density_area3(self, time):
        if 6<=time<16.42:
            density=self.func_c1(time)
        elif time==16.42:
            density=self.func_c2(time)
        elif 16.42<time<22:
            density=self.func_c3(time)
        else:
            density=self.func_c4(time)
        return density

    def density_area4(self, time):
        d1=self.density_area1(time)
        d2=self.density_area2(time)
        density = self.func_d(time, d1, d2)
        return density

    def func_a1(self, time):
        return -28.77+7.92*time-0.47*(time**2)

    def func_a2(self, time):
        return 1.16*time-6

    def func_a3(self, time):
        return 6.13+37.5*math.exp(-0.5*((time-12.88)/0.7)**2)

    def func_a4(self, time):
        return 2.42*time-29.565

    def func_a5(self, time):
        return 3.02+22.9*math.exp(-0.5*((time-17.99)/0.795)**2)

    def func_a6(self, time):
        return 0

    def func_b1(self, time):
        return 0.72*time-3.32

    def func_b2(self, time):
        return -221.3+55.27*time-3.385*(time**2)

    def func_b3(self, time):
        2

    def func_b4(self, time):
        return 136.794-27.27*time+1.369*(time**2)

    def func_b5(self, time):
        return 5.5

    def func_b6(self, time):
        return 3.668+23.53*math.exp(-0.5*((time-12.6)/0.578)**2)

    def func_b7(self, time):
        return 0.665*time-5.123

    def func_b8(self, time):
        return 5.75+12.7*math.exp(-0.5*((time-17.92)/0.274)**2)

    def func_b9(self, time):
        return -1.64*time+37.08

    def func_b10(self, time):
        return 0

    def func_c1(self, time):
        return 2.5+9.34*math.exp(-0.5*((time-13.2)/1.37)**2)

    def func_c2(self, time):
        return 3.5

    def func_c3(self, time):
        return 0.896+5.9*math.exp(-0.5*((time-18.06)/1.385)**2)

    def func_c4(self, time):
        return 0

    def func_d(self, time, d_1, d_2):
        return 0.5*(d_1 + d_2)
