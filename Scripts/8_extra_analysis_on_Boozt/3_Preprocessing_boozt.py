#==========================================================================
  # TABLE OF CONTENTS
"""
      - Load packages
      - Load data
      - Cleaning data using regex
      - Tokenizing & lemmatizing
      - Save to CSV file
      - Extra: Visualize most frequent terms
"""
#==========================================================================

#%%
#==========================================================================
# Load packages
#==========================================================================
from nltk import sent_tokenize, word_tokenize, sent_tokenize, pos_tag
from nltk.corpus import stopwords
import numpy as np
import re, string
import pandas as pd
import stanfordnlp 
# stanfordnlp.download('da') # run this only the first time

#%%
#==========================================================================
# Loading data
#==========================================================================
data = pd.read_csv('boozt_raw_reviews.csv')
data.shape # 3596, 5

#%%  
#==========================================================================
# Cleaning data using regular expressions (RE)
#==========================================================================

# In the column 'ReviewDate', extract the date (xxxx-xx-xx) in the strings.
data['ReviewDate'] = data['ReviewDate'].str.extract('(....-..-..)', expand=True)

# Extract the year from column 'ReviewDate'
data['year'] = data['ReviewDate'].str.extract('(....)', expand=True)

# RE removing numbers, as we can't use the information for neither topic detection nor sentiment analysis. 
data['clean_text']= [re.sub(r'\d+','', x) for x in data['Review']]

# RE removing some punctuation
data['clean_text'] = [re.sub(r'[\,\-\'\"\:\;\_\=\(\)\|\*\@\#\&\$\"\/\%\+]+','', x) for x in data['clean_text']]

# RE removing non-ASCII characters. Keeps all ASCII and æ, ø and å
data['clean_text'] = [re.sub(r'[^\x00-\x7Fæøå]+','', x) for x in data['clean_text']]

#%% 
#==========================================================================
# Tokenizing & lemmatizing
#==========================================================================

# # Exclude one row because it was empty after cleaning it (raw review only contained numbers)
# data = data[data['clean_text'] != '']

# # Lemmatize and POS-tag with StanfordNLP 
# stanford_nlp = stanfordnlp.Pipeline(processors='tokenize,pos,lemma', lang="da")
# data['lemmatized'] = [stanford_nlp(i) for i in data['clean_text']]
# data['lemmatized'] = [" ".join([(word.lemma) for sentence in i.sentences for word in sentence.words]) for i in data['lemmatized']]

# # Tokenize by sentences: First, replace 'men' with full stop before sentence tokenizing.
# # It's ok that 'men' is replaced as it has a sentiment score of 0
# data['sent_toke'] = [i.replace(' men ', ' . ') for i in data['lemmatized']]

# # Split by punctuation
# data['sent_toke'] = [sent_tokenize(text.lower(), language = "danish") for text in data['sent_toke']]
# data['sent_toke']

# # Create a row for each list element
# s = data.apply(lambda x: pd.Series(x['sent_toke']),axis=1).stack().reset_index(level=1, drop=True)
# s.name = 'sent_toke'
# df = data.drop('sent_toke', axis=1).join(s)



# For the sentiment analysis

# It's ok that 'men' is replaced as it has a sentiment score of 0
data['sent_toke_senti'] = [i.replace(' men ', ' . ') for i in data['clean_text']]

# Split by punctuation
data['sent_toke_senti'] = [sent_tokenize(text.lower(), language = "danish") for text in data['sent_toke_senti']]
data['sent_toke_senti']

# Create a row for each list element
s = data.apply(lambda x: pd.Series(x['sent_toke_senti']),axis=1).stack().reset_index(level=1, drop=True)
s.name = 'sent_toke_senti'
df = data.drop('sent_toke_senti', axis=1).join(s)

# Exclude one row because it was empty after cleaning it (raw review only contained numbers)
df = df[df['sent_toke_senti'] != '']

# Lemmatize and POS-tag with StanfordNLP 
stanford_nlp = stanfordnlp.Pipeline(processors='tokenize,pos,lemma', lang="da")
df['lemmatized'] = [stanford_nlp(str(i)) for i in df['sent_toke_senti']]
df['lemmatized'] = [" ".join([(word.lemma) for sentence in i.sentences for word in sentence.words]) for i in df['lemmatized']]


#%% 
#==========================================================================
# Save to csv file
#==========================================================================
df.to_csv("preprocessed_reviews.csv")

#%%
#==========================================================================
# Extra: Visualize most frequent terms
#==========================================================================

data = pd.read_csv('preprocessed_reviews.csv')

import nltk
from nltk import FreqDist
import matplotlib.pyplot as plt
import seaborn as sns

def freq_words(x, terms = 30):
  all_words = ' '.join([text for text in x])
  all_words = all_words.split()

  fdist = FreqDist(all_words)
  words_df = pd.DataFrame({'word':list(fdist.keys()), 'count':list(fdist.values())})

  # selecting top 20 most frequent words
  d = words_df.nlargest(columns="count", n = terms) 
  plt.figure(figsize=(20,5))
  ax = sns.barplot(data=d, x= "word", y = "count")
  ax.set(ylabel = 'Count')
  plt.show()

# Most common words in dataset
freq_words(data['sent_toke'])

# Most common words when stopwords are removed
stoplist = stopwords.words('danish') 
sentences = data["sent_toke"]
all_reviews = joinStrings(sentences)
toke = nltk.word_tokenize(all_reviews)

words = []
for i in toke:
    if not i in stoplist:
        words.append(i)

freq_words(words)