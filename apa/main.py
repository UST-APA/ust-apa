from Graph import generate_graph
from Model import *


temperature_m = TemperatureSeed('temp')
density_m = DensitySeed('density')
simple_m = SimpleModel({'density': density_m, 'temperature': temperature_m})

graph = generate_graph('../data/edges.csv', '../data/nodes.csv')
