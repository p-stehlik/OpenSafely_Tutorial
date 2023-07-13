import pandas as pd

data = pd.read_csv("output/input.csv.gz")

fig = data.age.plot.hist().get_figure()
fig.savefig("output/descriptive.png")