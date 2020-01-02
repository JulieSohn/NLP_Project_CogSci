#===========================================================================================
# Sentiment Analysis
'''
    - Imports
    - Transforming data
        - Money
        - Delivery
        - Return
        - Products
        - Customer service
        - Brand
    - Tokenise, bigrams, frequency distribution and plot
    - WordCloud
'''
#===========================================================================================
#%%
#==========================================================================
# Imports
#==========================================================================
import pandas as pd 
import pandas as pd             
import csv                      
import nltk
from nltk import FreqDist
from nltk.util import ngrams
import re
from nltk.corpus import stopwords

stoplist = stopwords.words('danish') 

# Function to join multiple strings into one 
def joinStrings(stringList):
    return ''.join(string for string in stringList)

data = pd.read_csv("sentiment_scored_reviews.csv")
data.drop(columns = "Unnamed: 0.1")

#%%
#==========================================================================                              
# Transforming data
#==========================================================================

# The sentiment score has to be above 0 to the positive
data['senti'] = data.sentiment.map(lambda s:1 if s > 0 else 0) # label as pos (=1) and neg (=0) reviews
data = data.drop(columns = "Unnamed: 0.1")
data = data.drop(columns = "X1")

data2019 = data[data.year == 2019]      # Shape: 5606,17
data2018 = data[data.year == 2018]      # Shape: 3351,17
data2012_17 = data[data.year < 2018]    # Shape: 10524,17

data2019.to_csv("data2019_results.csv")
data2018.to_csv("data2018_results.csv")
data2012_17.to_csv("data2012_17_results.csv")

#%%
#==========
# Money
#==========
money = data2019[data2019.money_related == 1] # 1152 sentences
money.shape
money['senti'].value_counts()

money = data2018[data2018.money_related == 1] # 547 sentences
money.shape
money['senti'].value_counts()

money = data2012_17[data2012_17.money_related == 1] # 1553 sentences
money.shape
money['senti'].value_counts()

money_pos = money[money.senti == 1]
money_neg = money[money.senti == 0]
# How many percent are negative? 
money_neg.shape[0] / (money_pos.shape[0] + money_neg.shape[0]) * 100

#==========
# Delivery
#==========
delivery = data2019[data2019.delivery_service == 1] # 792 sentences
delivery.shape
delivery['senti'].value_counts()

delivery = data2018[data2018.delivery_service == 1] # 542 sentences
delivery.shape
delivery['senti'].value_counts()

delivery = data2012_17[data2012_17.delivery_service == 1] # 1732 sentences
delivery.shape
delivery['senti'].value_counts()

delivery_pos = delivery[delivery.senti == 1]
delivery_neg = delivery[delivery.senti == 0]
# How many percent are negative?
delivery_neg.shape[0] / (delivery_pos.shape[0] + delivery_neg.shape[0]) * 100


#==========
# Return
#==========
returning = data2019[data2019.return_service == 1] # 945 sentences
returning.shape
returning['senti'].value_counts()

returning = data2018[data2018.return_service == 1] # 455 sentences
returning.shape
returning['senti'].value_counts()

returning = data2012_17[data2012_17.return_service == 1] # 1191 sentences
returning.shape
returning['senti'].value_counts()

returning_pos = returning[returning.senti == 1]
returning_neg = returning[returning.senti == 0]
# How many percent are negative?
returning_neg.shape[0] / (returning_pos.shape[0] + returning_neg.shape[0]) * 100


#==========
# Products
#==========
products = data2019[data2019.products == 1] # 1071 sentences
products.shape
products['senti'].value_counts()

products = data2018[data2018.products == 1] # 753 sentences
products.shape
products['senti'].value_counts()

products = data2012_17[data2012_17.products == 1] # 2697 sentences
products.shape
products['senti'].value_counts()

products_pos = products[products.senti == 1]
products_neg = products[products.senti == 0]
# How many percent are negative?
products_neg.shape[0] / (products_pos.shape[0] + products_neg.shape[0]) * 100


#==========
# Service
#==========
service = data2019[data2019.customer_service == 1] # 1959 sentences
service.shape
service['senti'].value_counts()

service = data2018[data2018.customer_service == 1] # 1177 sentences
service.shape
service['senti'].value_counts()

service = data2012_17[data2012_17.customer_service == 1] # 3200 sentences
service.shape
service['senti'].value_counts()

service_pos = service[service.senti == 1]
service_neg = service[service.senti == 0]
# How many percent are negative?
service_neg.shape[0] / (service_pos.shape[0] + service_neg.shape[0]) * 100


#==========
# Brand
#==========
brand = data2019[data2019.brand == 1] # 1387 sentences 
brand.shape
brand['senti'].value_counts()

brand = data2018[data2018.brand == 1] # 788 sentences 
brand.shape
brand['senti'].value_counts()

brand = data2012_17[data2012_17.brand == 1] # 2650 sentences 
brand.shape
brand['senti'].value_counts()

brand_pos = brand[brand.senti == 1]
brand_neg = brand[brand.senti == 0]
# How many percent are negative?
brand_neg.shape[0] / (brand_pos.shape[0] + brand_neg.shape[0]) * 100


#%%
#=======================================================
# TOKENIZE, BIGRAMS, FREQUENCY DISTRIBUTION AND PLOT
#=======================================================
sentences_neg = [money_neg["sent_toke"],
                delivery_neg["sent_toke"],
                returning_neg["sent_toke"],
                products_neg["sent_toke"],
                service_neg["sent_toke"],
                brand_neg["sent_toke"],
                ]

sentences_pos = [money_pos["sent_toke"],
                delivery_pos["sent_toke"],
                returning_pos["sent_toke"],
                products_pos["sent_toke"],
                service_pos["sent_toke"],
                brand_pos["sent_toke"],
                ]

def bigramming(noget):
    for sentences in noget:
        all_reviews = joinStrings(sentences)
        toke = nltk.word_tokenize(all_reviews) 

        words = []
        for i in toke:
            if not i in stoplist:
                words.append(i)
    
        bigrams = nltk.bigrams(words)
        freq = nltk.FreqDist(bigrams)
        freq.plot(20)

bigramming(sentences_neg)
bigramming(sentences_pos)
