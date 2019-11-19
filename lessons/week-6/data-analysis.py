# python3 -m pip install --user matplotlib
import matplotlib.pyplot as plt
# python3 -m pip install --user plotly
from plotly.graph_objs import Bar, Layout
from plotly import offline



# squares = [1, 4, 9, 16, 25]
# input_values = [1, 2, 3, 4, 5]

# plt.style.use('fivethirtyeight')
# fig, ax = plt.subplots()

# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
# ax.tick_params(axis="both", labelsize=14)

# ax.plot(input_values, squares, linewidth=3)


# use built in styles
print(plt.style.available)

# scatter plots
# ax.scatter(input_values, squares, s=200)


# plt.show()


results = {
  "Option 1": 2,
  "Option 2": 3,
  "Option 3": 3,
  "Option 4": 1,
  "Option 5": 5,
  "Option 6": 5
}

data = [Bar(x=list(results.keys()), y = list(results.values()))]
x_axis_config = {'title': 'Turtle Drawing'}
y_axis_config = {'title': 'Number of Votes'}
my_layout = Layout(title='Turtle Voting Results', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='results.html')