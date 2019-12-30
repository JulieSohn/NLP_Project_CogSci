# NLP_Project
*CogSci Master, 7th semester*

### Product Reviews from Online Retailers on TrustPilot
We will look at Danish product reviews from Trustpilot from Zalando. We want to do text classification and sentiment analysis on the reviews. Our idea is similar to Trustpilot’s Review Insights, where you get a sentiment and topic score, but we seek to further develop on this idea by also comparing scores across time, similar companies, and countries.
 
##### Our approach: 
- Extract approximately 3.000 Danish reviews from Zalando (and other companies alike) on TrustPilot.

- Then, we will try to make a rule-based classifier to recognise a category, let’s say price by the words “pris”, “dyrt”, “billigt”, “penge”, “kroner”, “kr” and so on.

- Next up is the sentiment analysis: of all the reviews in the category “price”, how many are positive and how many are negative?
Quality check: Which words keep coming up as strong contributors? 
(show_most_informative_features)

- Finally, Zalando will receive a report: “6/10 of customers who commented on the price are dissatisfied with your prices. This is better than that of Nelly.com (7/10), but worse than that of Boozt (3/10).” 
It would also be cool to compare one’s own scores Y-o-Y (year of year): how was your score January last year compared to Jan this year? Has it improved, and what do people say now compared to last year? Or for the last 3-4 months/one quarter (TrustPilot already does something like this)

Another cool feature would be to compare the Danish reviews of Zalando to the Norwegian and Swedish reviews.
Zalando (or any other brand) can then use this insight to set their KPIs (key performance indicators), competitiveness with other brands in the online shopping field, and to make improvements in their customer service, collection of brands (brand monitoring) and so on. The idea behind this NLP project could also be used for other business analyses such as NPS (net promoter score).

##### Relevant prior work:
Trustpilot’s Review Insights: https://support.trustpilot.com/hc/en-us/articles/360012057153,
Calheiros, A. C., Moro, S., & Rita, P. (2017). Sentiment classification of consumer-generated online reviews using topic modeling. Journal of Hospitality Marketing & Management, 26(7), 675-693.

##### Dataset: 
- We have a python script to extract data from TrustPilot (the data is labeled from 1-5 stars). As the data is already labeled, we need no human annotation for this part, but we may need to annotate the topic (such as whether a review is about the price or not).

- There are between 1500-3000 reviews per brand. Therefore, we’ll look at the 1500 newest reviews.

##### Pre-existing software will be used to accomplish the analysis task:
- SENTIDA: With SENTIDA it is possible to get the valence of the Danish words, which will help us in the sentiment analysis. Negation word 'ikke' is also included in this r-package.

- NLTK: useful for sentiment analysis / text classification

- Visualization (maybe using e.g. PyLDAvis?)

- Topic classification of the reviews. Topics: delivery, price, quality, brand and customer service.

##### Proposes a preliminary experiment to run on the data (this will be reported on in the progress report), as well as the scope of the final total project.
We will first do a topic classification - i.e. dividing reviews into different categories. Second, we willrun the sentiment analysis on the Danish reviews from Zalando using AFINN or SENTIDA to see if this works in Danish. Lastly, we will make suggestions for improvement for Zalando based on the reviews of similar companies. 
