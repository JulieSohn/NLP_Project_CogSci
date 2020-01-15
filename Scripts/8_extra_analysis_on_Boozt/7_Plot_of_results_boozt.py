
#===========================================================================================
# PLOT THE RESULTS
#===========================================================================================

#%%
# libraries
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#%%

# percent for 2019 & 2020
872/5356*100 # percent
473/5356*100 # percent
717/5356*100 # percent
510/5356*100 # percent
1164/5356*100 # percent
773/5356*100 # percent

# 16.28, 8.83, 13.39, 9.52, 21.73, 14.43


#%%
#===========================================================================================
# PLOT FOR MOST DISCUSSED TOPICS 
#===========================================================================================

labels = ['Brand', 'Service', 'Delivery', 'Money', 'Products', 'Return']

year_2019 = [16.3, 8.8, 13.4, 9.5, 21.7, 14.4]     # Order: Brand, Service, Delivery, Money, Products, Return

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
#rects1 = ax.bar(x - 0.28, year_2012_2017, width, label='2012-2017', color = '#C2DBFF')
rects2 = ax.bar(x, year_2019, width, label='2019-2020', color='#5E8CCC')
#rects3 = ax.bar(x + 0.28, year_2019, width, label='2019', color='#3A577F')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylim([0,40])
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


#autolabel(rects1)
autolabel(rects2)
#autolabel(rects3)

fig.tight_layout()
plt.show()


# %%
#===========================================================================================
# PLOT FOR SENTIMENT PER TOPIC 
#===========================================================================================

labels = ['Brand', 'Service', 'Delivery', 'Money', 'Products', 'Return']

year_2019 = [19.6, 17.8, 10.5, 12.4, 16.8, 22.8] # Order: Brand, Service, Delivery, Money, Products, Return

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
#rects1 = ax.bar(x - 0.28, year_2012_2017, width, label='2012-2017', color = '#C2DBFF')
rects2 = ax.bar(x, year_2019, width, label='2019-2020', color='#5E8CCC')
#rects3 = ax.bar(x + 0.28, year_2019, width, label='2019', color='#3A577F')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylim([0,50])
ax.set_ylabel('Percentage of negative mentions')
ax.set_xlabel('Topics')
ax.set_title('Negative Sentiment Scores')
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


#autolabel(rects1)
autolabel(rects2)
#autolabel(rects3)

fig.tight_layout()
plt.show()


# %%
