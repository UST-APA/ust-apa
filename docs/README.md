# The Optimal Path Planning in Dynamic Scenario: An Advanced HKUST Path Advisor (covid-19 version)

## Proposed Research Topic
The Optimal Path Planning in Dynamic Scenario: An Advanced HKUST Path Advisor (covid-19 version)

## Purposes
The purpose of this project is to produce an application generating optimal path in HKUST. This open-sourced application enables students or stuff in HKUST to query route in a very efficient way. Considering actual distance, static altitude, and dynamic parameters like crowd density and temperature, our application can propose the most comfortable path. To simulate data as the same as reality, a carefully considered data generator is proposed in this project. User-friendly graphics interface is provided for path visualization. Since documentations are provided at public website, developers can contribute to this project too.

## Expertise requirement breakdown
20%-Mathematics (optimization, modeling); 20%-Practice (field survey, data collection); 60%-Programming (python, algorithm implementation, data visualization).

## Background
One of the highlights of our project is that our generation is based on crowd density, which is also a frequently mentioned research topic. A research on pedestrian flow on railway station shows that there will be several peaks in crowd density during a whole day in crowded places [1]. Another study focuses on one peak and specifically studies its distribution [2], which might also be helpful to us. After collecting enough data on crowd density, we will then do optimal path generation, which is a popular problem in path planning study field. Obtaining the optimal route in dynamic conditions is more difficult than general path planning problem. Finally, in data visualization, Unity has been accepted as a powerful software which can implement unreal environment rendering and simulate 3D map [3]. However, because Unity needs enormous computational resources, it is difficult to construct an enormous number of building models in 3D map. Unreal engine is also a fully mission software which can provide better rendering function. And it may be easier to deal with numerous building models in 3D map [4].  As for the construction of 2D map, both Unity and Unreal engine can exhibit the power in rendering map.

## Scope 
In our model, six parameters are considered to obtain the edge weight: Manhattan distance d, altitude a, crowd density dens, trip mode m, temperature tem, and indoor or outdoor flag io. Manhattan distance, altitude, and indoor/outdoor flag of the path between two nodes are static values, while other three parameters are dynamic. All parameters will be collected through field visits and this model can simulate reality well. Related documentations and source code will be uploaded to public website. Developers can contribute new algorithms there. Besides, because of the complexity of the construction of 3D map, we will just consider the 2D map construction. We can prioritize some feasible paths by which user can combine their preference and our suggestions to choose one path.

## Theoretical framework
In the study on railway station [1], their method of collecting data is to count the number of pedestrians passing by in a certain area and period, which will be consulted in our project. Since the research on peak hours concludes that the relationship between crowd density and time is Gaussian function [2], we will also use Gaussian function for several peaks when doing data fitting. Because the crowd density increases rapidly at the peak, we will recommend the path to users according to the peak value instead of the growing real-time crowd density in the period corresponding to half height width of the peak. In this way, we make sure that people will not meet the crowd peak on the halfway. The general solutions for dynamic path planning problems include Particle Swarm Optimization (PSO) planner, Minimum Spanning Forest (MSF), and so on [5][6]. PSO algorithm generates global optimal paths by subjecting the valid paths. MSF defines a modified data structure called edge-ordered dynamic tree to obtain the optimal path in dynamic planar graph. In this project, we will provide several general planners to obtain optimal path for users. About visualization part, the Python library folium has been employed to display geographical distributions of lightning strike locations, which is an interactive visualization package [7]. The geemap is also a python library that has the function of interactive mapping with Google Earth Engine. We will select the folium package as our display tool and renderer for simple installation [8].

## Method 
- Divide the HKUST map and mark the roads.
- Collect crowd density data and other parameters at different times and on different roads. 
- Fit the relationship between crowd density and time period on each road and use Gaussian function at the peaks.
- Build our algorithm. Edge weight: $v_e= w_0 d+w_1 a+w_2 f(dens,m)+w_3 g(dens)+w_4 h(tem,io)$.
- Realize visualization.

## Expected outcome 
This project will introduce three modules: the simulation data generator, the dynamic path planer, and the visualization of path in HKUST. Our project can provide path advices with users, which can help students and staffs in UST to find their preferred path. These path advices are optimized by different shortest path search algorithm. And our methods take the crowding, weather, distance into consideration. Moreover, our methods can display some feasible paths by which the user can combine their preference with path advices to choose path.

## Timetable: 
- Prepare proposal by 26 Sept
- Draw the basic map (confirm key nodes) by 27 Sept
- Simulate data by 3 Oct
- Complete modeling by 7 Oct
- Complete visualization by 10 Oct
- Refine system by 12 Oct
- Complete final Report by 16 Oct

## References
[1] J. Shah, G. J. Joshi and P. Parida, “Behavioral characteristics of pedestrian flow on stairway at railway station,” Biology Letters, vol. 104, pp. 688-697, 2013
[2] T. Q. Tang, B. T. Zhang, J. Zhang and T. Wang, “Statistical analysis and modeling of pedestrian flow in university canteen during peak period,” Physica A: Statistical Mechanics and its Applications, vol. 521, pp. 29-40, 2019
[3] A. nckevičius and R. Dude, “Physically based shading in Unity,” Game Developer's Conference, 2014.
[4] B. Karis and E. Games, “Real shading in unreal engine 4,” Proceeding of Physically Based Shading Theory Practice, 2013.
[5] P. Raja and S. Pugazhenthi, "Path Planning for Mobile Robots in Dynamic Environments Using Particle Swarm Optimization," 2009 International Conference on Advances in Recent Technologies in Communication and Computing, Kottayam, Kerala, pp. 401-405, 2009, doi: 10.1109/ARTCom.2009.24.
[6] D. Eppstein, G. F. Italiano, R. Tamassia, R. E. Tarjan, J. Westbrook, M. Yung, “Maintenance of a minimum spanning forest in a dynamic plane graph,” Journal of Algorithms, vol. 13, Issue 1, pp. 33-54, 1992, ISSN 0196-6774, https://doi.org/10.1016/0196-6774(92)90004-V.
[7] P. Sarajcev and H. Matijasevic, “Python in Lightning Detection Network Data Analysis,” The 25th International Lightning Detection Conference and 7th International Lightning Meteorology Conference, 2018.
[8] Q. Wu, “geemap: A Python package for interactive mapping with Google Earth Engine,” Journal of Open Source Software, vol. 5, pp. 2305, 2020.
