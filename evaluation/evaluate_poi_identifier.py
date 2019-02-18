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
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from skelarn.cross_validation import train_test_split

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

#splitting the dataset
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.30, random_state=36)

#test accuracy of DecisionTreeClassifier
### your code goes here
clf1=DecisionTreeClassifier()
clf1.fit(features_train,labels_train)
pred1=clf1.predict(features_test)
print "decision tree accuracy: ", accuracy_score(labels_test, pred1)
