__author__ = 'beahacker'
from sklearn.naive_bayes import GaussianNB
from time import time
from sklearn.metrics import accuracy_score

def NBAccuracy(features_train, labels_train, features_test, labels_test):
    """ compute the accuracy of your Naive Bayes classifier """

    ### create classifier
    clf = GaussianNB()

    ### fit the classifier on the training features and labels
    t0 = time()
    clf.fit(features_train, labels_train)
    print "Training time: %fs", round(time() - t0, 3)

    ### use the trained classifier to predict labels for the test features
    t0 = time()
    pred = clf.predict(features_test)
    print "Testing time: %fs", round(time() - t0, 3)

    ### calculate and return the accuracy on the test data
    ### this is slightly different than the example,
    ### where we just print the accuracy
    ### you might need to import an sklearn module
    accuracy = accuracy_score(labels_test, pred)
    return accuracy
