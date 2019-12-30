#===========================================================================================
# PLOT THE RESULTS
#===========================================================================================

#%%
# libraries
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Percent for 2019
1387+1959+792+1152+1071+945 # total mentions 7306
1387/7306*100 
1959/7306*100 
792/7306*100 
1152/7306*100 
1071/7306*100 
945/7306*100 

# Percent for 2018
788+1177+542+547+753+455 # Total mentions: 4262
788/4262*100 
1177/4262*100 
542/4262*100 
547/4262*100
753/4262*100
455/4262*100 

# Percent for 2012-2017
2650+3200+1732+1553+2697+1191 # Total: 13023
2650/13023*100
3200/13023*100 
1732/13023*100 
1553/13023*100 
2697/13023*100 
1191/13023*100 


#%%
#===========================================================================================
# PLOT FOR MOST DISCUSSED TOPICS 
#===========================================================================================

labels = ['Brand', 'Service', 'Delivery', 'Money', 'Products', 'Return']

year_2012_2017 = [20.3, 24.6, 13.3, 11.9, 20.7, 9.1] # Order: Brand, Service, Delivery, Money, Products, Return
year_2018 = [18.5, 27.6, 12.7, 12.8, 17.7, 10.7]     
year_2019 = [19.0, 26.8, 10.8, 15.8, 14.7, 12.9]     
 
x = np.arange(len(labels))  # The label locations
width = 0.25                # The width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - 0.28, year_2012_2017, width, label='2012-2017', color = '#C2DBFF')
rects2 = ax.bar(x, year_2018, width, label='2018', color='#5E8CCC')
rects3 = ax.bar(x + 0.28, year_2019, width, label='2019', color='#3A577F')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylim([0,30])
ax.set_ylabel('Mentions of the topic in percentages')
ax.set_xlabel('Topics')
ax.set_title('Topic mentions')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', 
                    size = 7)

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

fig.tight_layout()
plt.show()

# %%
#===========================================================================================
# PLOT FOR SENTIMENT PER TOPIC 
#===========================================================================================

labels = ['Brand', 'Service', 'Delivery', 'Money', 'Products', 'Return']
year_2012_2017 = [28.5, 31.9, 26.0, 26.7, 26.6, 26.2] # Order: Brand, Service, Delivery, Money, Products, Return
year_2018 = [30.6, 34.6, 27.3, 25.6, 27.8, 24.4] 
year_2019 = [37.8, 43.0, 33.8, 31.8, 33.3, 27.8] 

x = np.arange(len(labels))  # The label locations
width = 0.25                # The width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - 0.28, year_2012_2017, width, label='2012-2017', color = '#C2DBFF')
rects2 = ax.bar(x, year_2018, width, label='2018', color='#5E8CCC')
rects3 = ax.bar(x + 0.28, year_2019, width, label='2019', color='#3A577F')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylim([0,50])
ax.set_ylabel('Percentage of negative mentions')
ax.set_xlabel('Topics')
ax.set_title('Sentiment Scores')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', 
                    size = 7)

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

fig.tight_layout()
plt.show()
