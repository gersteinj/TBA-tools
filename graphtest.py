import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as offline

import random
import math
x_vals = []
y_vals = []
size_vals = []
col_vals = []
for n in range(1000):
    x = n * .01
    y = math.sin(x)
    size = abs(y)
    r = size * 255
    g = 0
    b = 255 - (size * 255)
    x_vals.append(x)
    y_vals.append(y)
    size_vals.append(5 + size * 10)
    col_vals.append('rgb(' + str(r) + ', ' + str(g) + ', ' + str(b) + ')')

trace = go.Scatter(x=x_vals, y=y_vals, mode='markers', marker = dict(size=size_vals, color=col_vals))

data = go.Data([trace])

layout = go.Layout(title='sample plot', xaxis={'title':'x1'}, yaxis={'title':'y1'})

fig = go.Figure(data=data, layout=layout)

offline.plot(fig)
