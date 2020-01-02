# NLP_Project_CogSci
*CogSci Master, 7th semester*

### Product Reviews from Online Retailers on Trustpilot
We will look at Danish product reviews from Trustpilot about Zalando. We want to do topic categorization and sentiment analysis on the reviews. Our idea is similar to Trustpilot’s Review Insights, where you get a sentiment and topic score, but we seek to further develop on this idea by also comparing scores across time. 
 
##### Our approach: 
- Extract approximately 3.500 Danish reviews from Zalando on Trustpilot.

- Make a rule-based system to recognize a category, let’s say price, by the words “pris”, “dyrt”, “billigt”, “penge”, “kroner”, “kr” and so on.

- Sentiment analysis: of all the reviews, specifically each sentence within the reviews, in the category “price”, how many are positive and how many are negative?

- Report findings, e.g. “36% of customers who commented on the price are dissatisfied with your prices.” Such reports would give an indication of what Zalando needs to focus on improving. 

For further development, scores could also be compared to similar companies or to the Norwegian and Swedish reviews of Zalando. Zalando (or any other brand) can then use this insight to set their KPIs (key performance indicators), competitiveness with other brands in the online shopping field, and to make improvements in their customer service, collection of brands (brand monitoring) and so on. The idea behind this NLP project could also be used for other business analyses such as NPS (net promoter score).

##### Relevant prior work:
Trustpilot’s Review Insights: https://support.trustpilot.com/hc/en-us/articles/360012057153,
Calheiros, A. C., Moro, S., & Rita, P. (2017). Sentiment classification of consumer-generated online reviews using topic modeling. Journal of Hospitality Marketing & Management, 26(7), 675-693.

##### Dataset: 
- A python script was used to extract data from Trustpilot (the data is labeled from 1-5 stars).

##### Pre-existing software will be used to accomplish the analysis task:
- SENTIDA: With SENTIDA it is possible to get the valence of the Danish words, which will help us in the sentiment analysis. Negation word 'ikke' is also included in this r-package.

- NLTK

- Topic detection of the reviews. Topics: delivery, price, quality, brand and customer service.
