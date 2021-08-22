import plotly.figure_factory as ff 
import plotly.express as px
import pandas as pd

df=pd.read_csv('data.csv')
fig=ff.create_distplot([df['Weight'].tolist()],['Weight'])
fig.show()