import pandas as pd
import copy
import folium

def addChoices(form, file_path = 'data/nodes.csv'):
    node_rename_pairs = []
    nodes = pd.read_csv(file_path)
    for i, node in nodes.iterrows():
        if node[-1]!="Null":
            node_rename_pairs.append((node[0],node[-1]))

    form.start.choices = node_rename_pairs
    form.destination.choices = node_rename_pairs
    return form

def initMap(tiles, latitude = 22.336251, longtitude = 114.265612,):
    base_map = folium.Map(location=[latitude, longtitude], zoom_start=17, \
                         tiles=tiles, attr='default')
    return base_map

def buildMarker(p, graph):
    p_loc = [graph.nodes[p]['lat'], graph.nodes[p]['lon']]
    if graph.nodes[p]['rename'] == 'Null':
        marker = folium.Marker(
            location=p_loc,
            icon=folium.DivIcon(html=f'''<div style="color:red;">Turn</div>'''),
        )
    else:
        marker = folium.Marker(
            location=p_loc,
            popup = graph.nodes[p]['rename'],
        )
    return marker

def roadColor(density):
    if density<10: return 'green'
    elif density<20: return 'blue'
    elif density<30: return 'yellow'
    elif density<40: return 'orange'
    else: return 'red'

def roadWeight(density):

    return 5 * (abs(density / 5) + 1.5)

def roadDelay(density):

    return 600 + abs(density) * 50


def read_coordiantes_file(file_path = 'data/nodes.csv'):
    '''Load coordinates data, Default:(data/nodes.csv)'''
    coordinates = pd.read_csv(file_path, index_col=0)
    return coordinates

def read_line_modification(file_path = 'data/line_modification'):
    '''Refine some roads by adding additional unseen nodes'''
    point_pairs = []
    with open(file_path, "r", encoding="UTF-8") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            line = line.split(" ")
            line = [[line[2*i], line[2*i+1]] for i in range(int(len(line)/2))]
            point_pairs.append(line)
    return point_pairs

def hash_map(point_pairs):
    hash_table = dict()
    for i in range(len(point_pairs)):

        pairs = point_pairs[i][0]
        pairs.sort()
        hash_key = hash(pairs[0]+pairs[1])
        points = [[float(point_pairs[i][j][0]), float(point_pairs[i][j][1])] for j in range(1,len(point_pairs[i]))]
        hash_table[hash_key] = [points, point_pairs[i][0]]
    return hash_table

