import plotly.figure_factory as ff
import pandas as pd

dataframe = pd.read_csv("data.csv")

graph2 = ff.create_distplot([dataframe["Mobile Brand"].tolist()],["mobile brand"],)
graph2.show()