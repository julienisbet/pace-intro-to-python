import csv, os
import plotly.graph_objects as go

my_file = open('ip-data.csv')
data_reader = csv.reader(my_file)
dates = []
data = []
header = next(data_reader)
for row in data_reader:
  dates.append(row[0])
  data.append(row[-1])

fig = go.Figure(data=go.Scatter(x=dates, y=data))
fig.show()

# import csv
# my_file = open('bluths.csv')
# data_reader = csv.DictReader(my_file)
# for line in data_reader:
#   print(line)
