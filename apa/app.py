from flask import Flask
from flask import render_template, flash, redirect, url_for, request
import folium
from folium.plugins import MeasureControl
from folium import FeatureGroup, LayerControl,Marker

from forms import LoginForm
from config import Config

# load model
from core.Model import TemperatureSeed
from demo import *

#model initialization
temperature_m = TemperatureSeed('temp', 20)
graph, model = initiate_model('../data/nodes.csv', '../data/edges.csv', temperature_m)

app = Flask(__name__)
#add config info
app.config.from_object(Config)

#set basic map tiles
google_tiles = 'http://mt.google.com/vt/lyrs=m&x={x}&y={y}&z={z}'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/menu',methods=['GET','POST'])
def menu():
    form = LoginForm()
    '''NTD: Auto fill the selectFiled tables'''

    if form.validate_on_submit():
        flash(f"Start from : {form.start.data}, Your Destination : {form.destination.data}")
        return redirect(url_for('runMap',start=form.start.data,end=form.destination.data))
    return render_template('menu.html',form=form)

@app.route('/map',methods=['GET','POST'])
def runMap():
    #use url to pass params
    start = request.args.get('start')
    end = request.args.get('end')
    print(start,end)

    '''NTD: model part'''
    ## update model
    # graph = update_model(graph, model, time)
    # path = shortest_path(graph, source, target)

    #初始位置
    latitude, longtitude = 22.336251, 114.265612
    ust_map = folium.Map(location=[latitude,longtitude],zoom_start=17,\
        tiles=google_tiles,attr='default')

    feature_group = FeatureGroup(name='Base icons')
    cyt,crs=[22.334974,114.264033],[22.334745,114.264354]
    Marker(location=cyt, popup=folium.Popup(folium.IFrame('test popup',width=70, height=45),default_open=True)).add_to(feature_group)
    Marker(location=crs, popup='crs').add_to(feature_group)
    # 描绘直线
    poly = folium.PolyLine([cyt, crs], tooltip='This road', smooth_factor=0.1).add_to(feature_group)
    feature_group.add_to(ust_map)

    #添加地图图层控件
    LayerControl().add_to(ust_map)

    #添加测距控件
    ust_map.add_child(MeasureControl())

    return ust_map._repr_html_()

if __name__ == '__main__':
    app.run()
