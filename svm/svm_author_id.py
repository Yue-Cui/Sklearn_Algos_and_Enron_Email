#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from collections import counter
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###
#clasifier
clf=SVC(kernal='rbf',C=10000)

#training
time_start=time()
clf.fit(features_train,labels_train)
print "training took" , time()-time_start ,"seconds"

#inferencing
time_start=time()
pred=clf.predict(features_test)
print "inferencing took" , time()-time_start ,"seconds"

print "accuracy:"+ accuracy_score(labels_test, pred)


#########################################################
