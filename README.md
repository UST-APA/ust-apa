### UST-APA -- The Optimal Path Planning in Dynamic Scenario: An Advanced HKUST Path Advisor (covid-19 version)
HKUST path advisor a pathfinding application often used by HKUST students and employees. Our project focuses on the upgrade version of the HKUST path advisor, by which users can query the route which contains the external part. Moreover, our model takes distance, temperature, altitude, and crowed density into account. 
These four factors are ascribed different weights to influence the cost of the edge in the graph. The data of these four factors are generated from the real situation in HKUST, which ensures the rationality and reliability of the outputs of our model. The algorithm used in our model is the Dijkstra algorithm that is an optimal-guarantee shortest path search algorithm. After obtaining the shortest path from the model, we make the web page to display the shortest path on the real map of HKUST and design the user-friendly interactive interface to enable users to access our upgrade version of path advisor easily.
![system-overview](https://github.com/UST-APA/ust-apa/blob/main/docs/figs/system-overview.PNG)

### Installation
#### Requirements
Our program has been tested with Windows 10.0 + Anaconda + Python 3.8.
Before using UST-APA, please ensure you have installed all following Python packages.
- flask-wtf
- folium

#### Install from source
Clone repository from Github:

    git clone https://github.com/UST-APA/ust-apa.git 
    cd ust-apa

Run a demo:

    cd app
    python app.py
Then open your browser, visit the page `http://127.0.0.1:5000/`
