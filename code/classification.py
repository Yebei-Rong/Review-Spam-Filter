from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

df_train = pd.read_csv('user_after_cluster_clf.csv')

train_X, test_X, train_y, test_y = train_test_split(df_train.loc[:, ['卖家信誉', '好评率', '评论数', 'rate', 'repect_rate', 'length']],
                                                                 df_train['cluster'],  test_size=0.3,  random_state=0)


clf_SVM = SVC()
clf_SVM.fit(train_X, train_y)

clf_NB = GaussianNB()
clf_NB.fit(train_X, train_y)

clf_KNN = KNeighborsClassifier()
clf_KNN.fit(train_X, train_y)

clf_DT = DecisionTreeClassifier()
clf_DT.fit(train_X, train_y)


pred_y_svm = clf_SVM.predict(test_X)
accuracy_svm = metrics.accuracy_score(test_y, pred_y_svm)

pred_y_nb = clf_NB.predict(test_X)
accuracy_nb = metrics.accuracy_score(test_y, pred_y_nb)

pred_y_knn = clf_KNN.predict(test_X)
accuracy_knn = metrics.accuracy_score(test_y, pred_y_knn)

pred_y_dt = clf_DT.predict(test_X)
accuracy_dt = metrics.accuracy_score(test_y, pred_y_dt)

print(accuracy_svm)
print(accuracy_nb)
print(accuracy_knn)
print(accuracy_dt)

