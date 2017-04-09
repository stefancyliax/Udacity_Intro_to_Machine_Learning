#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 


from sklearn import tree
from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)

print clf.score(features_test, labels_test)
print len(features[0])
print len(features[:0])
print clf.predict(features_test)
print labels_test

from sklearn.metrics import confusion_matrix, precision_score, recall_score
print "Confusion matrix: "
print confusion_matrix(labels_test, clf.predict(features_test))
print "Precision: ", precision_score(labels_test, clf.predict(features_test))
print "Recall: ", recall_score(labels_test, clf.predict(features_test))