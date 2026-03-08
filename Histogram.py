import matplotlib
import numpy as np
import matplotlib.pyplot as plt


#Histogram Date
histogram_date="15/06/2024"
#Bar width
bar_width=0.4
#Start - Data preperation
hours=["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
#Get the total of vehiccles for each hour for Elm Avenue/Rabbit Road
juction1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
#Get the total of vehiccles for each hour for Hanley Highway/Westway
juction2=[3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49]
#End - Data preperation
bar1=np.arange(len(hours))
bar2=[i+bar_width for i in bar1]


#Create Bar 1 - Elm Avenue/Rabbit Road
plt.bar(bar1,juction1,bar_width,label="Elm Avenue/Rabbit Road")

#Create Bar 1 - Hanley Highway/Westway
plt.bar(bar2,juction2,bar_width,label="Hanley Highway/Westway") 
#plt.bar(hours,juction2,bar_width,bottom=juction1,label="Hanley Highway/Westway")

#Set props
plt.legend(prop ={'size': 5})
#Set axis-X
plt.xlabel("Hours 00:00 to 24:00", size=6) 
#Set axis-Y
#plt.ylabel("Count", size=6)
#Set title
plt.title(f"Histogram of Vehicle Frequency per Hour ({histogram_date})")
#Align bar 2 next to bar 1
plt.xticks(bar1+bar_width/2,hours,fontsize=5)
#Set font size of axis-Y
plt.yticks(fontsize=5)
#Remove outside box lines
ax=plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.yaxis.set_major_locator(plt.NullLocator())
#Set the values top of the bar 1
for index, value in enumerate(juction1):
    plt.text(index, value, s=f"{value}", ha="center", size=5)
#Set the values top of the bar 2
for index, value in enumerate(juction2):
    plt.text(index, value, s=f"{value}", ha="center", size=5)

plt.show()