#==========================================================================
# Rule-based system
'''
        - Imports
        - Rule-based system
        - Use the class to create topic dimensions
'''
#==========================================================================

#%% 
# Imports
import pandas as pd           
import csv                

data =  pd.read_csv("zalando_pre_small.csv")
data = data.drop(columns = "Unnamed: 0.1")

#%%
#==========================================================================                              
# Rule-based system
#==========================================================================  

class topic_classification:
    # Set topics
    def __init__(self):
        self.topic_payment = ["udbetaling", "betale", "betaling", "bankoverførsel", "betalingsmulighed",
                            "betalingsformer", "pris", "penge", "krone", "billigt", "dyr", "tilbud",
                            "overføre", "overførsel", "dankort", "paypal"]
        self.topic_delivery =["postnord", "post nord", "levering", "leveringsdygtig", "modtage",
                            "leveringstid", "leveringsstid", "ventetid", "behandlingstid", "forsendelse",
                            "track", "trace", "fringe"] # fringe = fragt
        self.topic_return =  ["retur", "returnering", "reklamation", "returret", "refundere", "betale tilbage", "bytte"]
        self.topic_products = ["udvalg", "kvalitet", "tøj", "produkt", "vare", "mærke", "sko", "jakke", "taske"]
        self.topic_service = ["kundeservice", "service", "support", "spørge", "svare", "telefon", "telefonkø",
                            "telefonsupport", "chat", "kontakt", "betjening", "mail", "tale", "ring", "behandling",
                            "medarbejder", "telefonmedarbejde", "kundeservicemedarbejde", "kunde", "kommunikere",
                            "kommunikation", "dialog"]
        self.topic_brand =   ["netbutik", "zalando", "virksomhed", "firma", "webshop", "hjemmeside", "onlin", "app",
                            "oplevelse", "behandling", "anbefale", "anbefaling", "forretning"]
        
    # Functions
    def payment(self, review):
        value = 0
        for word in self.topic_payment:
            value += review.count(word)
        if value > 0: return 1
        else: return 0

    def delivery(self, review):
        value = 0
        for word in self.topic_delivery:
            value += review.count(word)
        if value > 0: return 1
        else: return 0

    def returns(self, review):
        value = 0
        for word in self.topic_return:
            value += review.count(word)
        if value > 0: return 1
        else: return 0

    def products(self, review):
        value = 0
        for word in self.topic_products:
            value += review.count(word)
        if value > 0: return 1
        else: return 0

    def service(self, review):
        value = 0
        for word in self.topic_service:
            value += review.count(word)
        if value > 0: return 1
        else: return 0

    def brand(self, review):
        value = 0
        for word in self.topic_brand:
            value += review.count(word)
        if value > 0: return 1
        else: return 0

#%%
#==========================================================================                              
# Create topic dimensions
#==========================================================================  

find_topic = topic_classification()

# Create columns for all dimensions
data['money_related'] = [find_topic.payment(i) for i in data['sent_toke']]
data['delivery_service'] = [find_topic.delivery(i) for i in data['sent_toke']]
data['return_service'] = [find_topic.returns(i) for i in data['sent_toke']]
data['products'] = [find_topic.products(i) for i in data['sent_toke']]
data['customer_service'] = [find_topic.service(i) for i in data['sent_toke']]
data['brand'] = [find_topic.brand(i) for i in data['sent_toke']]

data.to_csv("z_topics.csv")

#%%
#==========================================================================                              
# How many topics overlap?
#==========================================================================

data = pd.read_csv("/Users/juliesohn/Desktop/zalando_sentiment_NEWEST.csv")
data = data.drop(columns = "Unnamed: 0.1")
data = data.drop(columns = "X1")
data.shape # 19481, 16

# New column adding up no. of dimensions for each row
data['CountTopics']= data.iloc[:, 10:16].sum(axis=1)

# Count occurrences of sentences only allocated to NO topic
print(len(data[data['CountTopics'] == 0])) # 5998

# Count occurrences of sentences only allocated to ONE topic
print(len(data[data['CountTopics'] == 1])) # 6497

# Count occurrences of sentences only allocated to MORE THAN ONE topic
print(len(data[data['CountTopics'] > 1])) # 6986

#==========================================================================

# Count occurrences of sentences only allocated to TWO topics
print(len(data[data['CountTopics'] == 2])) # 4074

# Count occurrences of sentences only allocated to THREE topics
print(len(data[data['CountTopics'] == 3])) # 1996

# Count occurrences of sentences only allocated to FOUR topics
print(len(data[data['CountTopics'] == 4])) # 665

# Count occurrences of sentences only allocated to FIVE topics
print(len(data[data['CountTopics'] == 5])) # 208

# Count occurrences of sentences only allocated to SIX topics
print(len(data[data['CountTopics'] == 6])) # 43