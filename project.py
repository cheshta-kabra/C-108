import plotly.figure_factory as ff 
import pandas as pd
import plotly.express as px

df=pd.read_csv('data1.csv')
#fig=ff.create_distplot([df['Avg Rating'].tolist()],['Avg Rating'])
fig=px.bar(df,x='Avg Rating',y='Mobile Brand',color="Avg Rating")
fig.show()