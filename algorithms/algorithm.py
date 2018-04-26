# -*- coding: utf-8 -*-

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 
from sklearn import preprocessing

dataset = pd.read_csv("numpy_formatted.txt")
original_data = dataset.copy()

# This function will encode our data into a format so that we can use it for machine learning models
def format_data_encoding(data_set):
    # We need to convert all the value of the data in the value of 0 to 1 
    for column in data_set.columns:
        le = preprocessing.LabelEncoder()
        data_set[column] = le.fit_transform(data_set[column])
    return data_set


encoded_data_set = format_data_encoding(dataset)
encoded_data_set_2 = encoded_data_set.copy()



from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
#names = ["age", "workclass", "educationum","maritalstatus", "occupation","relationship","race","hoursperweek"]
lr = LinearRegression()

features = encoded_data_set.drop("income",axis = 1)
target = encoded_data_set.income
names  = encoded_data_set.columns.values.tolist();
#rank all features, i.e continue the elimination until the last one
rfe = RFE(lr, n_features_to_select=1)
rfe.fit(features,target)
print ("Features sorted by their rank:")
print (sorted(zip(map(lambda x: round(x, 4), rfe.ranking_), names)))



from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()

X_train, X_test, y_train, y_test = train_test_split(features,target,test_size = 0.33, random_state = 1242)

logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)



from sklearn.metrics import accuracy_score
print ("Accuarcy Score for logistic regression ")
print(accuracy_score(y_test, y_pred))


from sklearn.metrics import classification_report
print ("Classification Report ")
print(classification_report(y_test, y_pred))


from sklearn import model_selection
from sklearn.model_selection import cross_val_score
kfold = model_selection.KFold(n_splits=9, random_state=7)
scores = cross_val_score(LogisticRegression(), X_train, y_train, cv=9, scoring='accuracy')
print("9-fold cross validation average accuracy: %.5f" % (scores.mean()))




# Use KNN to predict the model 
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics


features = encoded_data_set[["educationnum","maritalstatus","relationship","race", "sex"]]

XKnn_train, XKnn_test, yKnn_train, yKnn_test = train_test_split(features,target,test_size = 0.33, random_state = 1242)

algorithms = ["auto", "ball_tree", "kd_tree", "brute"]
for algorithm in algorithms:    
    knn = KNeighborsClassifier(n_neighbors = 5, algorithm=algorithm)
    knn.fit(XKnn_train, yKnn_train)
    knn_pred = knn.predict(XKnn_test)
    final_score = metrics.accuracy_score(yKnn_test, knn_pred)
    print ("Accuarcy for (%s) Algorithm is: %.5f " %(algorithm,final_score) )


    # This will print out the nomial attribute
    #print((original_data["workclass"].value_counts() / original_data.shape[0]).head())

   
    
#Boosting Algorithm
from xgboost import XGBClassifier
from xgboost import plot_importance

X = encoded_data_set.drop(["income","fnlwgt","education","relationship"],axis=1)
y = encoded_data_set["income"]
model = XGBClassifier()
model.fit(X, y)
print(model.feature_importances_)
plot_importance(model)
plt.show()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=7)

xg_pred = model.predict(X_test)
accuracy = metrics.accuracy_score(y_test, xg_pred)
print("Accuracy for XG BOOSTING : %.3f%%" % (accuracy * 100.0))


from sklearn.ensemble import AdaBoostClassifier
adaBoost = AdaBoostClassifier(n_estimators=100, random_state = 100)

X = encoded_data_set.drop(["income","education","relationship"],axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=7)

adaBoost.fit(X,y)

ada_pred = adaBoost.predict(X_test)

accuracy = metrics.accuracy_score(y_test, xg_pred)
print("Accuracy for ADa BOOSTING : %.3f%%" % (accuracy * 100.0))



# Random forest. Set of sub Decision Tree
from sklearn.ensemble import RandomForestClassifier
X = encoded_data_set.drop(["income","fnlwgt"], axis=1)
names = X.columns.values.tolist()
number_of_trees = [1,10,100]


for tree in number_of_trees:
    
    rf = RandomForestClassifier(n_estimators=tree, oob_score=True, random_state=123456)
    rf.fit(X_train, y_train)
    random_pred = rf.predict(X_test)
    accuracy = accuracy_score(y_test, random_pred)
    print('Random Forest estimate for %d sub tree is %.3f%%: ' %(tree, accuracy * 100.0))
    print (sorted(zip(map(lambda x: round(x, 4), rf.feature_importances_), names), 
             reverse=True))



# Extra Tree not powefull than RF

from sklearn.ensemble import ExtraTreesClassifier
X = encoded_data_set.drop(["income","capitalgain","capitalloss","fnlwgt","education","relationship"],axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=7)

extraTree = ExtraTreesClassifier(n_estimators=100, oob_score=True, random_state=123456,max_depth=10,bootstrap=True)
extraTree.fit(X_train, y_train)
pred = extraTree.predict(X_test)
accuracy = accuracy_score(y_test, pred)
 
print ("Extra Tree Classifier accuracy is %.3f%%" %(accuracy*100.0))
print('Random Forest estimate for %d sub tree is %.3f%%: ' %(tree, accuracy * 100.0))
print (sorted(zip(map(lambda x: round(x, 4), extraTree.feature_importances_), names), 
             reverse=True))




# Backpropagation 



from sklearn.neural_network import MLPClassifier

ann = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=17, random_state=12345)
ann.fit(X_train, y_train)
pred = extraTree.predict(X_test)
accuracy = accuracy_score(y_test, pred)

print ("Neural Network Classifier accuracy is %.3f%%" %(accuracy*100.0))


from sklearn import svm 
X = encoded_data_set_2.drop(["income"],axis=1)
y= encoded_data_set_2["income"]
svm_c = svm.SVC()
svm_c.fit(X,y)
pred = svm_c.predict(X_test)
accuracy = accuracy_score(y_test, pred)

print (accuracy)














