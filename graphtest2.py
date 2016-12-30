from bokeh.plotting import figure, output_file, show

import math
import random

x = [n * .01 for n in range(1000)]
y0 = [math.sin(n) for n in x]
y1 = [2 * math.sin(n + 1) for n in x]

output_file('scatter_plot.html')

p = figure(tools='reset,wheel_zoom,pan,box_select')

p.circle(x, y0)
p.asterisk(x, y1, size=10)

show(p)

