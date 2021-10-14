import pandas as pd
import numpy as np
import pydotplus
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from IPython.display import Image
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from imblearn.over_sampling import SMOTE
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pylab as pl
#Doc du lieu
df = pd.read_csv("bike_buyers_clean.csv")
#Tien xu ly du lieu
data = df[["Purchased Bike", "Age", "Region", "Commute Distance", "Cars", "Home Owner", "Occupation", "Education", "Children", "Income", "Gender", "Marital Status", "ID"]].copy(True)
data = data.dropna()
print("Du lieu:\n", data)
LanberEncoder = preprocessing.LabelEncoder()
data['Occupation_class'] = LanberEncoder.fit_transform(data['Occupation'])
data['Commute Distance_class'] = LanberEncoder.fit_transform(data['Commute Distance'])
data['Purchased Bike_class'] = LanberEncoder.fit_transform(data['Purchased Bike'])
data_train = data.drop(["Occupation", "Commute Distance",], axis=1)
print("Du lieu chuan hoa:\n", data_train.head(20))

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

#clf = SVC(gamma='auto')

X = np.asarray(data_train[['Income','Children','Occupation_class','Commute Distance_class', "Cars"]])
Y = np.asarray(data_train['Purchased Bike_class'])
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
print('Data:\n', data_train.shape)
# clf.fit(X_train, Y_train)
# score = clf.score(X_test, Y_test)
# print("Score", score)
# Du doan voi tao du lieu train X_test , y_test
decsionTreeEntropy = DecisionTreeClassifier(criterion="entropy", random_state=100, max_depth=5, min_samples_leaf=5)
decsionTreeEntropy.fit(X_train, Y_train)
y_preEntropy = decsionTreeEntropy.predict(X_test)
print("Du doan bang Entrophy", y_preEntropy)
from sklearn.metrics import classification_report
print("Bao cao:\n", classification_report(Y_test, y_preEntropy))

print('Before OverSampling:')

print('No =', sum(Y_train == 0))

print('Yes =', sum(Y_train == 1))

sm = SMOTE(random_state=2)

X_train_res, y_train_res = sm.fit_sample(X_train, Y_train)

print("After OverSampling, counts of label 0: {}".format(sum(y_train_res == 0)))

print("After OverSampling, counts of label 1: {}".format(sum(y_train_res == 1)))
decsionTreeEntropy = DecisionTreeClassifier(criterion="entropy", random_state=100, max_depth=5, min_samples_leaf=5)
decsionTreeEntropy.fit(X_train_res, y_train_res)
y_preEntropHy = decsionTreeEntropy.predict(X_test)
print("Du doan bang Entrophy", y_preEntropHy)
print("Bao cao sau can bang:\n", classification_report(Y_test, y_preEntropHy))

# gini = DecisionTreeClassifier(criterion="gini", random_state=100, max_depth=5, min_samples_leaf=5)
# gini.fit(X_train, y_train)
# y_preGini =gini.predict(X_test)
#print("Du doan bang Gini",y_preGini)
#Confusion matrix
from sklearn.metrics import confusion_matrix
print('Ma tran hon loan truoc can bang:\n', confusion_matrix(Y_test, y_preEntropy))
print('Ma tran hon loan sau can bang:\n', confusion_matrix(Y_test, y_preEntropHy))
#Bước 3: Đánh giá mô hình học dựa trên kết quả dự đoán (với độ đo đơn giản Accuracy, Precision, Recall)
print("Accuracy Score truoc can bang:", accuracy_score(Y_test, y_preEntropy)*100)
print("Accuracy Score sau cân bằng:", accuracy_score(Y_test, y_preEntropHy)*100)
# cm = confusion_matrix(Y_test, y_preEntropy)
# pl.matshow(cm)
# pl.title('Ma trận nhầm lẫn của bộ phân loại')
# pl.colorbar()
# pl.show()

#Bieu dien du lieu
#Giam chieu PCA
# pca = PCA(n_components=1)
# X_scat = pca.fit_transform(X_train)
#Plot
# plt.scatter(X_train,Y_train,s=100,c='green',edgecolors='black',)
# plt.xlabel("Giá trị X")
# plt.ylabel("Giá trị Y")
# plt.title("Biểu đồ tương quan X và Y")
# plt.show()
# fig = plt.figure(figsize=(10,7))
# colors=['red' if l==0 else 'blue' for l in Y_train]
# plt.scatter(X_train[:, 0], X_train[:, 1], label='Logistics regression', color=colors)
# plt.plot(X_train, Y_train, label='Decision Boundary')
# plt.show()
#Tao dot data
dot_data = tree.export_graphviz(decsionTreeEntropy, out_file=None)
#Ma tran sau can bang
