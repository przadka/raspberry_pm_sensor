# coding=utf-8
'''
Publish data found in measure.log to a remoe Plotly service. Assumes
Plotly account is already in place and set up on the system. 
'''

import os
import plotly.plotly as py
from plotly.graph_objs import *
import math

DATA_TAIL = 50

content = []
x_labels = []
pm25_data = []
pm10_data = []

#load the file to memory
with open(os.path.join(os.path.dirname(__file__), 'measure.log')) as fp:
	for line in fp:
		content = line.strip().split(',')
		x_labels.append(content[0].strip())
		pm25_data.append(float(content[2]))
		pm10_data.append(float(content[1]))

pm10_data = pm10_data[-DATA_TAIL:]
pm25_data = pm25_data[-DATA_TAIL:]
x_labels = x_labels[-DATA_TAIL:] 

max_y = math.ceil((max(pm10_data)*1.5)/50.0)*50 #calculate maximum y value to show on the chart

pm25 = Scatter(
    x = x_labels,
    y =  pm25_data,
    mode = 'lines',
    name = 'PM 2.5',
    line = dict(
        shape='spline'
    )
)

pm10 = Scatter(
    x = x_labels,
    y =  pm10_data,
    mode = 'lines',
    name = 'PM 10',
    line = dict(
        shape='spline'
    )
)

data = Data([pm25, pm10])

layout = Layout(
    yaxis=dict(
        range=[0, max_y]
    )
)

fig = Figure(data=data, layout=layout)
py.plot(fig, filename = 'basic-line')
