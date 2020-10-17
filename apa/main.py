from Graph import generate_graph
from Model import *
import networkx as nx

import matplotlib.pyplot as plt

temperature_m = TemperatureSeed('temp', 20)
density_m = DensitySeed('density')
simple_m = SimpleModel({'density': density_m, 'temperature': temperature_m})

print("generating graph...")
graph = generate_graph('../data/edges.csv', '../data/nodes.csv')

print("updating graph...")
graph = simple_m.update_graph(graph, 10.5)
path = nx.shortest_path(graph, source='1', target='54')

print(path)