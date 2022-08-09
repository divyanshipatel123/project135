import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv

df = pd.read_csv("new.csv")

##plotting the graphs 
fig1 = plt.figure(figsize=[10,8])
sns.barplot(x = 'Star_Name',y = 'Star_Mass',data = df)
plt.xticks(rotation=75)
plt.title("Name X Mass")
fig1.show()

fig2 = plt.figure(figsize=[10,8])
sns.barplot(x = 'Star_Name',y = 'Star_Radiuses',data = df)
plt.xticks(rotation=75)
plt.title("Name X Radius")
fig2.show()


fig3 = plt.figure(figsize=[10,8])
sns.barplot(x = 'Star_Name',y = 'Star_Distance',data = df)
plt.xticks(rotation=75)
plt.title("Name X Distance")
fig3.show()


fig4 = plt.figure(figsize=[10,8])
sns.barplot(x = 'Star_Name',y = 'Star_Gravity',data = df)
plt.xticks(rotation=75)
plt.title("Name X Gravity")
fig4.show()


### FINDINGS ########3
# mass and radius are kind of correlated 
#distance is not correlated at all
# starnge that when both massand radius graph go down the garvity incresases
#-this may be beacuse radius squared is dividing the mass ones 