# customer sentiment analyzer
# Overview 
The customer experience is more important than ever before. Increased globalization
means consumers have no shortage of options to choose from when they’re in the market
for products and services. In many cases, the customer experience is the only thing setting
one business apart from another. Given the importance of customer service, it’s no
surprise that companies are turning to call center outsourcing services for support.
We have a task tracking system that is used by Agents/Supervisors to capture customer
requests and process them.
# Goals
1. Identify the sentiment in the customer service request to access the level of support
needed so Agents/Supervisors can ensure 100% satisfaction to customers.
2. Analyze trends that show reputation and scope for improvements with the product
or support system.

# Specifications
- [x] Develop a machine learning model that can be trained or tuned in future by
supervisors.
- [x] Need UI for supervisors to review the decisions made by model
- [x] Need ability to rerun the model by changing train/test data.
- [ ] Need API endpoints to interact with the deployed model from any internal MAP
systems.
- [x] Analyze trends based on prediction history
  - [x] To show reputation of task categories
  - [x] Accounts that have series of negative feedbacks so supervisors can follow up
with them using different mechanisms
## Sentiment Analysis
Sentiment analysis is the use of natural language processing, text analysis, computational linguistics, and biometrics to systematically identify, extract, quantify, and study affective states and subjective information.
Helping a business to understand the social sentiment of their brand, product or service while monitoring online conversations. 
### Flow diagram
![image](https://user-images.githubusercontent.com/42908255/124773040-3427b400-df5a-11eb-8eee-271a240b85e4.png)
# technologies used
* fromt-end - html/css/js
* back-end - flask(python3)
* database - SQLite 
* machine learning algorithms tested for sentiment analysis - logistic regression, decison tree, xgboost and naive bayes 
* machine learning algorithms tested for emotional analysis - LSTM+GLOVE, ROBERTA, ALBERT
* machine learning algorithms used after performance analysis - naive bayse and ALBERT
# feedback page
![Screenshot (2272)](https://user-images.githubusercontent.com/65475955/125712517-67afb4ab-50de-4cb0-9305-03ee8aaf4e39.png)
# login page
![Screenshot (2283)](https://user-images.githubusercontent.com/65475955/125712576-0b389042-716a-49e0-bc71-d746c505f2e3.png)
# Supervisor's UI
![Screenshot (2282)](https://user-images.githubusercontent.com/65475955/125712711-2e7f8ea1-ba9f-41fd-b8d7-a0c2730ab94e.png)
# Agent's UI
![Screenshot (2274)](https://user-images.githubusercontent.com/65475955/125712653-75593070-ba89-4dcb-9c07-f7f42cdb29df.png)
![Screenshot (2275)](https://user-images.githubusercontent.com/65475955/125712658-6ae52455-e7c1-439b-af2c-f8a29e8f39b6.png)
![Screenshot (2276)](https://user-images.githubusercontent.com/65475955/125712672-f1038816-0470-49fd-9ae8-ba5a45e43803.png)
# Trends
![Screenshot (2277)](https://user-images.githubusercontent.com/65475955/125712675-e2558161-68b0-40b9-b29a-ead4fb3306b6.png)
# Charts
![Screenshot (2278)](https://user-images.githubusercontent.com/65475955/125712679-60267fd7-f46d-49ab-91f3-9c517f846480.png)
![Screenshot (2279)](https://user-images.githubusercontent.com/65475955/125712686-d1eb8fcd-1784-4a65-8a97-e442d62b452a.png)
# Emotional Analysis
![Screenshot (2280)](https://user-images.githubusercontent.com/65475955/125712699-e4713729-c311-47d6-aa4b-9150917d80f8.png)





