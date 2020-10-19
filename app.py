from flask import Flask
from flask import render_template, flash, redirect, url_for, request
from forms import MenuForm
from config import Config
#import visulization parts
import folium
from folium.plugins import MeasureControl,AntPath
from folium import FeatureGroup, LayerControl, Marker
#from utils.py import funcs
from utils import *
#load model
from core.Model import TemperatureSeed
from core.demo import *

# model initialization
temperature_m = TemperatureSeed('temp', 20)
graph, model = initiate_model('data/nodes.csv', 'data/edges.csv', temperature_m)

app = Flask(__name__)
#add config info
app.config.from_object(Config)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/menu',methods=['GET','POST'])
def menu():
    form = MenuForm() #NTD: Auto fill the selectFiled tables
    form = addChoices(form)
    form = addDateChoices(form)

    if form.validate_on_submit():
        # flash(f" Last time, Start from : {form.start.data}, Destination : {form.destination.data}")
        return redirect(url_for('runMap', start=form.start.data, end=form.destination.data, time=form.time.data,
                                temp=form.date.data))
    return render_template('menu.html',form=form)

@app.route('/map',methods=['GET','POST'])
def runMap():
    #use url to pass params
    start = request.args.get('start')
    end = request.args.get('end')
    time = float(request.args.get('time'))
    temp = float(request.args.get('temp'))

    '''model part'''
    global graph
    global model
    model.temperature_seed.tem = temp
    graph = update_model(graph, model, time)
    path = shortest_path(graph, source = start, target = end)
    cost_time = get_cost_time(graph, path)

    '''visualization'''
    #Init Map
    google_tiles = 'http://mt.google.com/vt/lyrs=m&x={x}&y={y}&z={z}'
    ust_map = initMap(tiles=google_tiles)

    #Add Optimal Path
    feature_group = FeatureGroup(name='Base icons')

    #Get each road's start and end point
    point_pairs = [[path[i], path[i+1]] for i in range(len(path)-1)]
    #Load Refined data
    line_modification = read_line_modification()
    hash_table = hash_map(line_modification)

    for i in range(len(point_pairs)):
        p1,p2 = point_pairs[i][0], point_pairs[i][1] #p1:start, p2:end
        pair = [p1,p2]
        temp_pair = pair.copy()
        temp_pair.sort()
        hash_index = hash(temp_pair[0]+temp_pair[1])

        #Visualize nodes
        p1_loc, p2_loc = [graph.nodes[p1]['lat'], graph.nodes[p1]['lon']], [graph.nodes[p2]['lat'], graph.nodes[p2]['lon']]
        buildMarker(p1,graph).add_to(feature_group)
        buildMarker(p2,graph).add_to(feature_group)

        #visualize road
        #if road can be curved:
        if hash_index in hash_table:
            if pair == hash_table[hash_index][1]:
                edge = [p1_loc] + hash_table[hash_index][0] + [p2_loc]
            else:
                intermediate_node = hash_table[hash_index][0]
                intermediate_node.reverse()
                edge = [p1_loc] + intermediate_node + [p2_loc]
        else:
            edge = [p1_loc, p2_loc]
        AntPath(edge, reverse=False,
                dash_array=[20, 30],
                delay = roadDelay(graph[p1][p2]['density']),
                weight = roadWeight(graph[p1][p2]['density']),
                color = roadColor(graph[p1][p2]['density']),
                ).add_to(feature_group)

    #Add whole feature_group to basic map
    feature_group.add_to(ust_map)
    LayerControl().add_to(ust_map)

    html_string = ust_map.get_root().render()
    return render_template('map.html', html_string = html_string, time_cost = round(cost_time/550.0,1), path = path_to_text(path,graph))
    # return ust_map._repr_html_()

if __name__ == '__main__':
    app.run()

#add customized size of text based on popup:
#Marker(location=cyt, popup=folium.Popup(folium.IFrame('test popup',width=70, height=45),default_open=True)).add_to(feature_group)
# OR：
# popup = '<i>Term1:</i>'+str(xxx)+'<br><i>Term2:</i>'+str(xxx)

#draw polyLine
#poly = folium.PolyLine([cyt, crs], tooltip='This road', smooth_factor=0.1, weight = 5, opacity = 0.5).add_to(feature_group)

#add Measure Control Plugins:
#ust_map.add_child(MeasureControl())