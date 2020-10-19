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
    path = nx.shortest_path(graph, weight='weight', source=source, target=target)
    return path


def get_cost_time(graph, path):
    cost_time = 0
    for i in range(len(path)-1):
        cost_time += graph.get_edge_data(path[i], path[i+1])['weight']
    return cost_time