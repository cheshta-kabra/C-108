import random
import plotly.figure_factory as ff 
import plotly.express as px
Diresult=[]
count=[]
for i in range(0,100): 
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    sum=dice1+dice2
    Diresult.append(sum)
    count.append(i)
print(Diresult)
#fig=ff.create_distplot([Diresult],['result'])
fig=px.bar(x=Diresult,y=count)
fig.show()