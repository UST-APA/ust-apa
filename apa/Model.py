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
        self.super_parameters = [10, 1, 3, 1]
        
    def initial_data(self, data_seeds):
        # TO DO: temperature can be a interface from Internet
        self.density_seed = data_seeds['density']
        self.temperature_seed = data_seeds['temperature']

    def update_weight(self, edge, graph, t):
        # TO_DO: get_io_flag(), get_distance(), get_altitude(), f(dens), g(tem, io)
        node_a = edge[0]
        node_b = edge[1]

        distance = graph[node_a][node_b]['distance']
        altitude = graph.nodes[node_a]['altitude'] - graph.nodes[node_b]['altitude']
        area = graph[node_a][node_b]['area']
        density = self.density_seed.run(t, area)
        temperature = self.temperature_seed.run(t)

        weight = np.array(self.super_parameters).dot(np.array([distance, altitude, self.f(density, t), self.g(temperature, io, t)]))

        graph[node_a][node_b]['weight'] = weight

    def update_graph(self, graph, t):
        for edge in graph.edgs:
            self.update_weight(edge, graph, t)
        return graph

    def f(self, density, t):
        sample = np.random.normal(loc=density, scale=0.1*density, size=1)
        return sample[0]
    
    def g(self, temperature, io):
        if io:
            return temperature
        else:
            return 2*temperature


class TemperatureSeed(object):
    def __init__(self, name):
        self.name = name

    def run(time):
        return 20.0


class DensitySeed(object):
    def __init__(self, name):
        self.name = name

    def run(time, area):
        if area==1:
            return density_area1(time)
        elif area==2:
            return density_area2(time)
        elif area==3:
            return density_area3(time)
        else:
            return density_area4(time)

    def density_area1(time):
        if 6<=time<9:
            density=func_a1(time)
        elif 9<=time<10.7:
            density=func_a2(time)
        elif 10.7<=time<14.75:
            density=func_a3(time)
        elif 14.75<=time<16.85:
            density=func_a4(time)
        elif 16.85<=time<22:
            density=func_a5(time)
        else:
            density=func_a6(time)
        return density

    def density_area2(time):
        if 6<=time<7.33:
            density=func_b1(time)
        elif 7.33<=time<9:
            density=func_b2(time)
        elif time==9:
            density=func_b3(time)
        elif 9<time<11.43:
            density=func_b4(time)
        elif time==11.43:
            density=func_b5(time)
        elif 11.43<time<14.2:
            density=func_b6(time)
        elif 14.2<=time<16.6:
            density=func_b7(time)
        elif 16.6<=time<18.55:
            density=func_b8(time)
        elif 18.55<=time<22:
            density=func_b9(time)
        else:
            density=func_b10(time)
        return density

    def density_area3(time):
        if 6<=time<16.42:
            density=func_c1(time)
        elif time==16.42:
            density=func_c2(time)
        elif 16.42<time<22:
            density=func_c3(time)
        else:
            density=func_c4(time)
        return density

    def density_area4(time):
        d1=density_area1(time)
        d2=density_area2(time)
        density = func_d(time, d1, d2)
        return density

    def func_a1(time):
        return -28.77+7.92*time-0.47*(time**2)

    def func_a2(time):
        return 1.16*time-6

    def func_a3(time):
        return 6.13+37.5*math.exp(-0.5*((time-12.88)/0.7)**2)

    def func_a4(time):
        return 2.42*time-29.565

    def func_a5(time):
        return 3.02+22.9*math.exp(-0.5*((time-17.99)/0.795)**2)

    def func_a6(time):
        return 0

    def func_b1(time):
        return 0.72*time-3.32

    def func_b2(time):
        return -221.3+55.27*time-3.385*(time**2)

    def func_b3(time):
        2

    def func_b4(time):
        return 136.794-27.27*time+1.369*(time**2)

    def func_b5(time):
        return 5.5

    def func_b6(time):
        return 3.668+23.53*math.exp(-0.5((time-12.6)/0.578)**2)

    def func_b7(time):
        return 0.665*time-5.123

    def func_b8(time):
        return 5.75+12.7*math.exp(-0.5((time-17.92)/0.274)**2)

    def func_b9(time):
        return -1.64*time+37.08

    def func_b10(time):
        return 0

    def func_c1(time):
        return 2.5+9.34*math.exp(-0.5((time-13.2)/1.37)**2)

    def func_c2(time):
        return 3.5

    def func_c3(time):
        return 0.896+5.9*math.exp(-0.5((time-18.06)/1.385)**2)

    def func_c4(time):
        return 0

    def func_d(time, d_1, d_2):
        return 0.5*(d_1 + d_2)
