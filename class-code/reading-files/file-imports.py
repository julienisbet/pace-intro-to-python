import csv
import plotly.graph_objects as go

with open('ip-data.csv') as f:
    raw_data = list(csv.DictReader(f))
print(raw_data[0])
print(raw_data[1])
data = {}
for row in raw_data:
    date = row['date']
    if date in data.keys():
        data[date] += int(row['f'])
    else:
        data[date] = int(row['f'])
fig = go.Figure(data=go.Scatter(
    x=list(data.keys()),
    y=list(data.values())
))
fig.show()
fig.write_html("ip-data.html")
# fig.write_image("ip-data.png")

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
