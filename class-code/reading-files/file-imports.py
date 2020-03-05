import csv, os
import plotly.graph_objects as go
import json

my_file = open('ip-data.csv')
data_reader = csv.reader(my_file)
data = {}
header = next(data_reader)
for row in data_reader:
  date = row[0]
  login_count = int(row[-1])
  if date in data.keys():
    data[date] += login_count
  else:
    data[date] = login_count
fig = go.Figure(data=go.Scatter(x=list(data.keys()), y=list(data.values())))
fig.show()

# import csv
# my_file = open('bluths.csv')
# data_reader = csv.DictReader(my_file)
# for line in data_reader:
#   print(line)

# with open('bluths.json') as f:
#   data = json.load(f)
#   print(data)
#   print(type(data))
#   print(data[0])
#   print(type(data[0]))
