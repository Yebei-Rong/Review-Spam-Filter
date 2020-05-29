import pandas as pd
from snownlp import SnowNLP
import jieba
import re
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
punc = u'[’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'


def comp_rate(content):
    a = SnowNLP(content)
    rate = a.sentiments
    return rate


def comp_repect(content):
    content = re.sub(punc, '', content)
    #     aa = SnowNLP(content)
    token = jieba.cut(content, cut_all=False)
    token = [x for x in token]
    #     print(token)
    for i in token:
        if i in stopword:
            token.remove(i)
    content_len = len(token)
    word_count = {}
    for item in token:
        word_count[item] = word_count.get(item, 0) + 1

    dit_out = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
    try:
        repeat_rate = dit_out[0][1] / content_len

    except:
        repeat_rate = 0
    return repeat_rate


def fun(x):
    if x == 0:
        return cc
    else:
        return x


# import raw data
user = pd.read_csv('user_initial.csv', engine='python')
with open('stopword.txt', 'r') as file:
    stopword = file.read().split('\n')

user['rate'] = user['content'].apply(comp_rate)
user['repect_rate'] = user['content'].apply(comp_repect)
user['length'] = user['content'].apply(len)

global cc
cc = user['卖家信誉'].max()
user['卖家信誉'] = user['卖家信誉'].apply(fun)

plt.hist(user['卖家信誉'], bins=4)
plt.show()

user.loc[(user['卖家信誉'] >= 0) & (user['卖家信誉'] < 0.25), '卖家信誉'] = 10
user.loc[(user['卖家信誉'] >= 0.25) & (user['卖家信誉'] < 0.5), '卖家信誉'] = 20
user.loc[(user['卖家信誉'] >= 0.5) & (user['卖家信誉'] < 0.75), '卖家信誉'] = 30
user.loc[(user['卖家信誉'] >= 0.75) & (user['卖家信誉'] <= 1.01), '卖家信誉'] = 40

content_count = user.groupby(['usernick', 'itemid'])['content'].count().to_frame('评论数')
user = user.merge(content_count, left_on=['usernick', 'itemid'], right_index=True, how='left')

# 分割数据集
sample = np.random.choice(range(len(user)), int(len(user) * 0.3))
sample_data = user.loc[sample]
cluster_data = user.drop(sample)

cluster_data.to_csv('user_after_preprocessing_clt.csv', index=False)
sample_data.to_csv('user_after_preprocessing_clf.csv', index=False)
