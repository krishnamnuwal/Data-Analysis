##importing all the required modules in project
import csv
import plotly.express as px
import plotly
import pandas as pd  

##storing the data of file in the variable DF
df=pd.read_csv('data.csv')

##finding the mean attempt of each student at each level and converting it into dataframe
meen=df.groupby(['student_id','level'],as_index=False)['attempt'].mean()

print(meen) ##printing the mean

##creating a scatter plot graph of attempts of each student at each level 
fig=px.scatter(meen,x="student_id",y="level",size="attempt",color="attempt")
plotly.offline.plot(fig)





















