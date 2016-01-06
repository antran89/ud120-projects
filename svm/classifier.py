import sklearn.svm as svm
from time import time

def linearSvmClassifier(features_train, labels_train, features_test):
    '''
    Classifying using linear svm.
    '''
    clf = svm.LinearSVC()

    # fit the classifier on the training features and labels
    t0 = time()
    clf.fit(features_train, labels_train)
    print "Training time: %fs" % (round(time() - t0, 3))

    # use the trained classifier to predict labels for the test features
    t0 = time()
    pred = clf.predict(features_test)
    print "Testing time: %fs" % (round(time() - t0, 3))

    return pred

def svmClassifier(features_train, labels_train, features_test):
    '''
    Classifying using SVC.
    '''
    clf = svm.SVC(kernel='rbf', C=10000)

    # fit the classifier on the training features and labels
    t0 = time()
    clf.fit(features_train, labels_train)
    print "Training time: %fs" % (round(time() - t0, 3))

    # use the trained classifier to predict labels for the test features
    t0 = time()
    pred = clf.predict(features_test)
    print "Testing time: %fs" % (round(time() - t0, 3))

    return pred
