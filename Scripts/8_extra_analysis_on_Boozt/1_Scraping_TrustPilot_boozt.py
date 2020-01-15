#==========================================================================
# Scraping Trustpilot
#==========================================================================

'''
Scraping the Internet w. Beautiful Soup and Request

We'll use the lxml parser, not html5lib (even though this is popular as well)

If you check the source code of a website, you'll often see
                <head> blablabla </head>
All in between the above is a single head tag/heading
                <h2> is anoter heading
                <p> is a paragraph tag
Source: https://www.youtube.com/watch?v=ng2o98k983k&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=46
'''
#%%
# Imports
import requests
from bs4 import BeautifulSoup as bs
import json
import math
import pandas as pd
import csv

# Functions
def getInfo(url):
    res=requests.get(url) # this is equal to the html of the website
    soup = bs(res.content, 'lxml')
    data = json.loads(soup.select_one('[type="application/ld+json"]').text.strip()[:-1])[0]
    return data

def addItems(data):
    result = [] # get our data in the way we like it (i.e. reviews, ranking, date)
    for item in data['review']:

        review = {    
                  'Headline': item['headline'] ,
                  'Ranking': item['reviewRating']['ratingValue'],
                  'Review': item['reviewBody'],
                  'ReviewDate': item['datePublished']
                }

        result.append(review)
    return result

#url = 'https://dk.trustpilot.com/review/zalando.dk?languages=da&page={}'
#url = 'https://www.trustpilot.com/review/www.boozt.dk?languages=da&page={}'
url = 'https://dk.trustpilot.com/review/www.boozt.com?page={}'

# Go through all pages of reviews and append them to an empty list, 'results'
results = []
data = getInfo(url.format(1))
results.append(addItems(data))  
totalReviews = int(data['aggregateRating']['reviewCount'])
reviewsPerPage = len(data['review'])
totalPages = math.ceil(totalReviews/reviewsPerPage)

if totalPages > 1:
    for page in range(2, totalPages + 1):
        data = getInfo(url.format(page))
        results.append(addItems(data)) 

final = [item for result in results for item in result]
df = pd.DataFrame(final)

# Save to csv
df.to_csv('boozt_raw_reviews.csv')


# %%
