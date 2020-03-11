# Purpose - This file is used to create a classifier and store it in a .pkl file. You can modify the contents of this
# file to create your own version of the classifier.

#import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score, classification_report
# from sklearn import metrics
import joblib

data_file = pd.read_csv("dataset/dataset.csv")

# Get all the columns from the dataFrame
columns = data_file.columns.tolist()

# Filter the columns to remove data we do not want
columns = [c for c in columns if c not in ["index","Result"]]

# Store the variable we'll be predicting on
target = "Result"

features_train = data_file[columns]
labels_train = data_file[target]

#features_test=features_train[10000:]
# labels_test=labels_train[10000:]

clf4 = RandomForestClassifier(min_samples_split=7, verbose=True)
clf4.fit(features_train, labels_train)

#print("\n\n ""Random Forest Algorithm Results"" ")
#pred = clf4.predict(features_test)
#print(pred)
#print(classification_report(labels_test, pred))
#print('The accuracy is:', accuracy_score(labels_test, pred))
#print(clf.score(features_train, labels_train))
#print(metrics.confusion_matrix(labels_test, pred))

#importances = clf4.feature_importances_
#std = np.std([tree.feature_importances_ for tree in clf4.estimators_], axis=0)
#indices = np.argsort(importances)[::-1]
# Print the feature ranking
#for f in range(features_train.shape[1]):
#    print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

# sys.setrecursionlimit(9999999)
#joblib.dump(clf4, 'C:/Bitnami/xampp/htdocs/protection/Module/classifier/random_forest.pkl', compress=9)
joblib.dump(clf4, 'classifier/random_forest.pkl', compress=9)
