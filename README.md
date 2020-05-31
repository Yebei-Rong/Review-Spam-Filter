# Review Spam Filter Based on Taobao

## 1 Introduction
A review spam filter for Taobao, the world's  biggest e-commerce website.

## 2 Model Construction
It is important to analyze the review itself to establish a spam filter. However, users who write fake reviews can imitate honest users to post their reviews. Thus, it is difficult to detect unreliable reviews only through analyzing the review itself. Based on this insight, this project has constructed a model in terms of three aspects -- review, reviewer and seller. The following figure shows our model for classifying the reliability of reviews for online goods.

![Model](https://github.com/Yebei-Rong/Review-Spam-Filter/blob/master/image/model.png?raw=true)

Thus, all the model indicators are either the features of the review or sentiment polarity. Let's have a look at each indicator.

### 2.1 The Length of review
The usefulness of one review is positively related with the review content. Fake reviews tend to express the subjectivity of customers which is often as simple as 'good!'. Thus, it becomes more trustworthy if the length of review is longer.

### 2.2 The Repetition Rate of Words
Fake reviews often repeat certain words to increase the length of a review in order to increase the weight of this review in the system. So a review is less trustworthy if the repetition rate of words is higher.

### 2.3 The Gregariousness of Sentiment Polarity
It is assumed that a review is more useful and trustworthy if its sentiment is affluent and thorough. On the other hand, if reviews expressed extremly negative sentiment, it may be doubtful.

### 2.4 Whether Write Repeatedly
If one reviewer write reviews for the same product many times and their sentiment are similar, then it is probable that these reviews are fake. Thus, we take this binary indicator into consideration when constructing the reliability model.

### 2.5 Credibility
The credibility of seller is an important factor for online shoppers, and determines the weight of this seller in the whole system. Sellers with high credibility are trustworthy. However, sellers with low credibility are more likely to hire someone to write fake reviews. Thus, it is necessary to consider seller's credibility.

### 2.6 Ratings
Likewise, ratings of seller are important for customers. And sellers with low ratings are more likely to hire people to write fake reviews in order to improve sales and ratings at the same time.

## 3 Implementation
### 3.1 Web Crawler
We crawled over 20,000 reviews from Taobao by Python selenium. Specifically, we used webdriver to imitate the real web browser and then go to the link to get the data of sellers, products and reviews. Finally, we stored all the data in mongodb database which is shown in the figure below. The code detail can be seen in file crawl_taobao.py.

![db](https://github.com/Yebei-Rong/Review-Spam-Filter/blob/master/image/db.png?raw=true)

### 3.2 Data Preprocessing
In this stage, we performed data cleaning, transformation and feature extraction on crawled data, which is an very important  step and directly influenced the effect of clustering and classification models.

For data cleaning, we focused on the missing values. Because Taobao doesn't assign credibility and ratings to flagship store in Tianmao, we used the highest credibility and ratings as their values since flagship stores are of greart credit themselves.

For data transformation, we actually calculated the indicators we need from the original data. In particular, the sentiment coefficient is obtained by *snownlp*, a well-known package for Chinese NLP tasks. And we fisrt performed segmentation on reviews before feeding them to calculate sentiment coefficient. (data_preprocessing.py)

In the original model, we considered the posted time of reviews. However, we observed that this indicator is almost the same among over 20,000 reivews. Moreover, we found the *Silhouette Coefficient* of our clustering model was improved, which means this facotr can be removed from our model and will have little impact on the prediction.

### 3.3 Cluster Analysis of Reviews
It is important to tag data in order to build classification model in the later. In our experiemnt, we took the clustering method, K-means and use *Silhouette Coefficient* to evaulate the results of different models. We found when k=5, the model performed the best whose clustering result is visualized below. 

![clustering](https://github.com/Yebei-Rong/Review-Spam-Filter/blob/master/image/clustering.png?raw=true)

Besides, by looking at the data of different groups. We found the features of reviews from category 0 to 4 as below:

|                          | 0             | 1           | 2      | 3        | 4       |
| ------------------------ | ------------- | ----------- | ------ | -------- | ------- |   
| Overall                  | useful        | very useful | normal | doubtful | useless |


### 3.4 Classification Model Construction and Evaluation 
We adopted four well-known classification algorithms -- decision tree, naive bayes, support vector machine (SVM) and k-nearest neighbors (KNN) algorithms. After constructing these models, we split the data into training and testing sets. The table below is the accuracy results of these models. We can see the best one is the decision tree model. Howverve, since our data is high dimensional, we here pick SVM model, which is only inferior to the decision tree. 

| Classification model | SVM      | Naive bayes | KNN      | Desicion tree |
| -------------------- | ---------| ----------- | -------- | ------------- |  
| Accurary             | 0.993689 | 0..979611   | 0.993203 | 0.998058      |


