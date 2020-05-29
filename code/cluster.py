import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from sklearn import metrics
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

user = pd.read_csv('user_after_preprocessing_clt.csv')
user_to_clf = pd.read_csv('user_after_preprocessing_clf.csv')

user['好评率'] = user['好评率'].apply(lambda x: 1 if x == 0 else x)
user_to_clf['好评率'] = user_to_clf['好评率'].apply(lambda x: 1 if x == 0 else x)

# 数据标准化
scaler = MinMaxScaler()
scaler.fit(user.loc[:, ['卖家信誉', '好评率', '评论数', 'rate', 'repect_rate', 'length']])
user.loc[:, ['卖家信誉', '好评率', '评论数', 'rate', 'repect_rate', 'length']] = scaler.transform(user.loc[:, ['卖家信誉', '好评率', '评论数', 'rate', 'repect_rate', 'length']])

scaler_clf = MinMaxScaler()
scaler_clf.fit(user_to_clf.loc[:, ['卖家信誉', '好评率', '评论数', 'rate', 'repect_rate', 'length']])
user_to_clf.loc[:, ['卖家信誉', '好评率', '评论数', 'rate', 'repect_rate', 'length']] = scaler_clf.transform(user_to_clf.loc[:, ['卖家信誉', '好评率', '评论数', 'rate', 'repect_rate', 'length']])

# k-means聚类
clt = KMeans(n_clusters=5)
cluster = clt.fit_predict(user.loc[:, ['卖家信誉', '好评率', '评论数', 'rate', 'repect_rate', 'length']])
cluster_clf = clt.predict(user_to_clf.loc[:, ['卖家信誉', '好评率', '评论数', 'rate', 'repect_rate', 'length']])
user['cluster'] = cluster
user_to_clf['cluster'] = cluster_clf

# 各类别的统计
print(user.groupby('cluster')['content'].count())
print(user.groupby('cluster')['卖家信誉', '好评率', '评论数', 'rate', 'repect_rate', 'length'].mean())

user.to_csv('user_after_cluster.csv', index=False)
user_to_clf.to_csv('user_after_cluster_clf.csv', index=False)

# 计算聚类的效果
label = clt.labels_
silhouette = metrics.silhouette_score(user.loc[:, ['卖家信誉', '好评率', '评论数', 'rate', 'repect_rate', 'length']], label, metric='euclidean')
print(silhouette)

# 聚类结果可视化
pca = PCA(n_components=3)
user_pca = pca.fit_transform(user.loc[:, ['卖家信誉', '好评率', '评论数', 'rate', 'repect_rate', 'length']])
user_pca = pd.DataFrame(user_pca, columns=['X1', 'X2', 'X3'])
user_pca['cluster'] = cluster

clt_0 = user_pca.loc[user_pca['cluster'] == 0]
clt_1 = user_pca.loc[user_pca['cluster'] == 1]
clt_2 = user_pca.loc[user_pca['cluster'] == 2]
clt_3 = user_pca.loc[user_pca['cluster'] == 3]
clt_4 = user_pca.loc[user_pca['cluster'] == 4]

ax = plt.subplot(111, projection='3d')  # 创建一个三维的绘图工程
#  将数据点分成三部分画，在颜色上有区分度
ax.scatter(clt_0['X1'], clt_0['X2'], clt_0['X3'], c='y')  # 绘制数据点
ax.scatter(clt_1['X1'], clt_1['X2'], clt_1['X3'], c='r')
ax.scatter(clt_2['X1'], clt_2['X2'], clt_2['X3'], c='g')
ax.scatter(clt_3['X1'], clt_3['X2'], clt_3['X3'], c='c')
ax.scatter(clt_4['X1'], clt_4['X2'], clt_4['X3'], c='m')
ax.set_zlabel('Z')  # 坐标轴
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.show()









