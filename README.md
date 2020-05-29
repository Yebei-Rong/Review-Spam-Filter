# Review Spam Filter Based on Taobao
A review spam filter for Taobao, the world's  biggest e-commerce website.

## 1 Introduction

## 2 Model Construction
It is important to analyze the review itself to establish a spam filter. However, users who write fake reviews can imitate honest users to post their reviews. Thus, it is difficult to detect unreliable reviews only through analyzing the review itself. Based on this insight, this project has constructed a model in terms of three aspects -- review, reviewer and seller. The following figure shows our model for classifying the reliability of reviews for online goods.

![Model](https://github.com/Yebei-Rong/Review-Spam-Filter/blob/master/image/model.png?raw=true)

Thus, all the model indicators are either the features of the review or sentiment polarity. Let's have a look at each indicator.

### 2.1 The Length of review
The usefulness of one review is positively related with the review content. Fake reviews tend to express the subjectivity of customers which is often as simple as 'good!'. Thus, it becomes more trustworthy if the length of review is longer.

### 2.2 The Repetition Rate of Words
Fake reviews often repeat certain words to increase the length of a review in order to increase the weight of this review in the system. So a review is less trustworthy if the repetition rate of words is higher.

### 2.3 The Gregariousness of Sentiment Polarity

### 2.4 Whether Write Repeatedly

### 2.5 Credibility

### 2.6 Ratings

## 3 Implementation
### 3.1 Web Crawler

### 3.2 Data Preprocessing
#### 3.2.1 Data Cleaning
#### 3.2.2 Data Transformation
#### 3.2.3 Feature Extraction

### 3.3 Cluster Analysis of Reviews

### 3.4 Classification Model Construction and Evaluation 

## 4 Conclusion 


