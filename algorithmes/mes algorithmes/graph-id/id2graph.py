import csv

x = []
y = []
anomaly = []

with open("data/HDFS_1M.csv") as file:
    csv = csv.reader(file)
    
    next(csv)
    
    for row in csv:
        x.append(row[0])
        y.append(row[2])
        anomaly.append(row[-1])
        


import numpy as np
import plotly.graph_objects as go
from lenspy import DynamicPlot


fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='lines'))
fig.add_trace(go.Scatter(x=x, y=anomaly, mode='lines+markers'))
fig.update_layout(title=f"{len(x):,} Data Points.", autotypenumbers='convert types')

# Use DynamicPlot.show to view the plot
plot = DynamicPlot(fig)
plot.show()

# Plot will be available in the browser at http://127.0.0.1:8050/
