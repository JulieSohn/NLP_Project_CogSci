#==========================================================================
# Exploring data
'''
    - Import packages and data
    - Length of reviews
    - Time trends
        - Plotting frequency of ratings
        - Plotting frequency of reviews: year, month, year-month
        - Plotting ratings
'''
#==========================================================================

#%%
#==========================================================================
# Import packages and data
#==========================================================================
import numpy as np 
import pandas as pd            
import csv                      
import matplotlib.pyplot as plt
import re, string
data =  pd.read_csv("raw_reviews.csv")

#%%
#==========================================================================
# Length of reviews
#==========================================================================
pos_len = []
for i, x in zip(data.Review, data.Ranking):
    if x == 5:
        pos_len.append(len(i))

neg_len = []
for i, x in zip(data.Review, data.Ranking):
    if x == 1:
        neg_len.append(len(i))

print("Avg. length of positive reviews: ", np.mean(pos_len))           # 238.65
print("Avg. length of negative reviews: ", np.mean(neg_len))           # 640.22

print("Standard deviation of positive reviews: ", np.std(pos_len))     # 217.80
print("Standard deviation of negative reviews: ", np.std(neg_len))     # 518.25

data.shape # 3596
data[data.Ranking == 5].shape # 1488
data[data.Ranking == 4].shape # 383
data[data.Ranking == 3].shape # 228
data[data.Ranking == 2].shape # 351
data[data.Ranking == 1].shape # 1146


#%%
#==========================================================================
# TIME TRENDS
#==========================================================================
data['ReviewDate'] = data['ReviewDate'].str.extract('(....-..-..)', expand=True)

#make a new column only containing month + one with year
data['year'] = data['ReviewDate'].str.extract('(....)', expand=True)
data['yearmonth'] = data['ReviewDate'].str.extract('(....-..)', expand=True)
data['month'] = data['ReviewDate'].str.extract('(-..-)', expand=True)
data['month'] = [re.sub(r'[\-\'\"\!\?\:\;\_\=\(\)\|\*\@\#\&\$\"\/\%\+\!]+','', x) for x in data['month']]

#%%
#==========================================================================                              
# Plotting frequency of ratings in two different ways
#==========================================================================
# ONE: Plot overall rating
total_reviews = data.groupby(['Ranking'])['Unnamed: 0'].count().reset_index()
total_reviews.plot(x="Ranking",y="Unnamed: 0",kind="bar",title="Total no. of reviews")
plt.show()

# TWO: create a figure and axis 
fig, ax = plt.subplots() 
# count the occurrence of each class 
dt = data['Ranking'].value_counts() 
# get x and y data 
points = dt.index
frequency = dt.values
# create bar chart 
ax.bar(points, frequency, color = '#5E8CCC') 
# set title and labels 
ax.set_title('TrustPilot Review Scores') 
ax.set_xlabel('Ranking') 
ax.set_ylabel('Frequency')

#%%
#==========================================================================                              
# Plotting frequency of reviews: year, month, year-month
#==========================================================================

# Total no. of reviews are increasing. Maybe because TrustPilot has become more popular.
yearly=data.groupby(['year'])['Unnamed: 0'].count().reset_index()
yearly.plot(x="year",y="Unnamed: 0",kind="bar",title="No. of reviews over year", color = '#5E8CCC')
plt.show()

# More reviews are given in 2018-2019
year_month = data.groupby(['yearmonth'])['Unnamed: 0'].count().reset_index()
year_month.plot(x="yearmonth",y="Unnamed: 0",kind="line",title="No. of reviews over months in a year")
plt.show()

# In general, more reviews are given in October and December
monthly = data.groupby(['month'])['Unnamed: 0'].count().reset_index()
monthly.plot(x="month",y="Unnamed: 0",kind="bar",title="No. of reviews over months")
plt.show()

#%%
#==========================================================================                              
# Plotting Ratings
#==========================================================================

# The avg. rating has become lower during the years
Yearly_Avg_Rating=data.groupby(['year'])['Ranking'].mean().reset_index()
Yearly_Avg_Rating.plot(x="year",y=["Ranking"],kind="bar",title="Avg. overall ratings over the years")
plt.show()

# A peak in 2015, now it is decreasing
year_monthly_Avg_Rating=data.groupby(['yearmonth'])['Ranking'].mean().reset_index()
year_monthly_Avg_Rating.plot(x="yearmonth",y=["Ranking"],kind="line",title="Avg. overall ratings over the years sorted by months")
plt.show()

# In general, the rating has been lover in October, November and December
monthly_Avg_Rating=data.groupby(['month'])['Ranking'].mean().reset_index()
monthly_Avg_Rating.plot(x="month",y=["Ranking"],kind="bar",title="Avg. overall ratings over months (year disregarded)")
plt.show()

'''
inspiration from
https://github.com/Maha41/Sentiment-analysis-on-Amazon-Reviews-using-Python/tree/master/Analysis
https://www.earthdatascience.org/courses/scientists-guide-to-plotting-data-in-python/plot-with-matplotlib/customize-plot-colors-labels-matplotlib/
'''
