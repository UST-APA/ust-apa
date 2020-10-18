from core.Graph import generate_graph
from core.Model import *
import networkx as nx


def initiate_model(nodes_csv, edges_csv, temperature_seed):
    temperature_m = temperature_seed
    # temperature_m = TemperatureSeed('temp', 20)
    density_m = DensitySeed('density')
    simple_m = SimpleModel({'density': density_m, 'temperature': temperature_m})

    print("generating graph...")
    graph = generate_graph(edges_csv, nodes_csv)

    return graph, simple_m


def update_model(graph, model, time):
    print("updating graph...")
    graph = model.update_graph(graph, time)
    return graph


def shortest_path(graph, source, target):
    path = nx.shortest_path(graph, source=source, target=target)
    return path
