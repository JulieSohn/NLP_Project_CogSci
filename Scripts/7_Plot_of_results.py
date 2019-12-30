
#===========================================================================================
#--- PLOT THE RESULTS
#===========================================================================================

#%%
# libraries
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#%%

# percent for 2019
1387/5606*100 # percent
1959/5606*100 # percent
792/5606*100 # percent
1152/5606*100 # percent
1071/5606*100 # percent
945/5606*100 # percent

# 24.74, 34.94, 14.13, 20.55, 19.10, 16.86

# Percent for 2018
788/3351*100 # percent
1177/3351*100 # percent
542/3351*100 # percent
547/3351*100 # percent
753/3351*100 # percent
455/3351*100 # percent

# 23.52, 35.12, 16.17, 16.32, 22.47, 13.58


# Percent for 2012-2017
2650/10524*100 # percent
3200/10524*100 # percent
1732/10524*100 # percent
1553/10524*100 # percent
2697/10524*100 # percent
1191/10524*100 # percent

# 25.18, 30.41, 16.46, 14.76, 25.63, 11.32


#%%
#===========================================================================================
#--- PLOT FOR MOST DISCUSSED TOPICS 
#===========================================================================================

labels = ['Brand', 'Service', 'Delivery', 'Money', 'Products', 'Return']

year_2012_2017 = [24.7, 34.9, 14.1, 20.6, 19.1, 16.9] # Order: Brand, Service, Delivery, Money, Products, Return
year_2018 = [23.5, 35.1, 16.2, 16.3, 22.8, 13.6]     # Order: Brand, Service, Delivery, Money, Products, Return
year_2019 = [25.2, 30.4, 16.5, 14.8, 25.6, 11.3]     # Order: Brand, Service, Delivery, Money, Products, Return

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - 0.28, year_2012_2017, width, label='2012-2017', color = '#C2DBFF')
rects2 = ax.bar(x, year_2018, width, label='2018', color='#5E8CCC')
rects3 = ax.bar(x + 0.28, year_2019, width, label='2019', color='#3A577F')

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


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

fig.tight_layout()
plt.show()


# %%
#===========================================================================================
#--- PLOT FOR SENTIMENT PER TOPIC 
#===========================================================================================

labels = ['Brand', 'Service', 'Delivery', 'Money', 'Products', 'Return']
year_2012_2017 = [28.5, 31.9, 26.0, 26.7, 26.6, 26.2] # Order: Brand, Service, Delivery, Money, Products, Return
year_2018 = [30.6, 34.6, 27.3, 25.6, 27.8, 24.4] # Order: Brand, Service, Delivery, Money, Products, Return
year_2019 = [37.8, 43.0, 33.8, 31.8, 33.3, 27.8] # Order: Brand, Service, Delivery, Money, Products, Return

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - 0.28, year_2012_2017, width, label='2012-2017', color = '#C2DBFF')
rects2 = ax.bar(x, year_2018, width, label='2018', color='#5E8CCC')
rects3 = ax.bar(x + 0.28, year_2019, width, label='2019', color='#3A577F')

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


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

fig.tight_layout()
plt.show()


# %%
