from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn import linear_model
from sklearn.cross_validation import cross_val_score
from sklearn.calibration import CalibratedClassifierCV
import numpy as np
from sklearn.preprocessing import Imputer #imputer to handle missing values
imp = Imputer(missing_values= 999, strategy='mean', axis=0)

#####this part is to convert training set file to proper format#####
lines = [line.rstrip('\n') for line in open('5000Sampling29_string_processed_feature_vector.txt')]
label = []
matrix = []
for l in lines:
    l = l[1:-1]
    vector = l.split(', ')
    x = np.array(vector[:-1], dtype = '|S4')
    y = x.astype(np.float)
    matrix.append(y)
    label.append(vector[24])   #this depends on the number of the columns
a = np.array(label, dtype = '|S4')
b = a.astype(np.float)
label = b

#####this part is to convert testing set file to proper format#####
lines_test = [line.rstrip('\n') for line in open('5000Test29_string_processed_feature_vector.txt')]
label_test = []
matrix_test = []
for l in lines_test:
    l = l[1:-1]
    vector_test = l.split(', ')
    x_test = np.array(vector_test[:-1], dtype = '|S4')
    y_test = x_test.astype(np.float)
    matrix_test.append(y_test)
    label_test.append(vector_test[24])
a_test = np.array(label_test, dtype = '|S4')
b_test = a_test.astype(np.float)
label_test = b_test
'''
###DecisionTreeClassifier#######
clf = DecisionTreeClassifier()
imp.fit(matrix)#fit the imputer on training matrix
matrix_t = imp.transform(matrix)# handling missing values of training matrix
clf = clf.fit(matrix_t, label) # fit classifier on transformed matrix_t

matrix_test_t = imp.transform(matrix_test)#handling missing values of testing matrix
scores = cross_val_score(clf, matrix_test_t, label_test)
print('DecisionTreeClassifier:')
print(scores.mean())
print('predicted classes:')
print(clf.predict(matrix_test_t))#testing code to print out preditced methods

###GaussianNB#######
clf = GaussianNB()
imp.fit(matrix)#fit the imputer on training matrix
matrix_t = imp.transform(matrix)# handling missing values of training matrix
clf = clf.fit(matrix_t, label) # fit classifier on transformed matrix_t
matrix_test_t = imp.transform(matrix_test)#handling missing values of testing matrix
scores = cross_val_score(clf, matrix_test_t, label_test)
print('GaussianNB:')
print(scores.mean())
print('predicted classes:')
print(clf.predict(matrix_test_t))#testing code to print out preditced methods
'''
###RandomForestClassifier#####

'''
### regular CLF###
clf = RandomForestClassifier(n_estimators = 10)
imp.fit(matrix)#fit the imputer on training matrix
matrix_t = imp.transform(matrix)# handling missing values of training matrix
clf = clf.fit(matrix_t, label) # fit classifier on transformed matrix_t
matrix_test_t = imp.transform(matrix_test)#handling missing values of testing matrix
'''
# Gaussian Naive-Bayes with isotonic calibration
clf = RandomForestClassifier(n_estimators = 10)
imp.fit(matrix)#fit the imputer on training matrix
matrix_t = imp.transform(matrix)# handling missing values of training matrix
clf = clf.fit(matrix_t, label) # fit classifier on transformed matrix_t
clf_isotonic = CalibratedClassifierCV(clf, cv=5, method='isotonic')
clf_isotonic.fit(matrix_t, label)
matrix_test_t = imp.transform(matrix_test)#handling missing values of testing matrix
# Gaussian Naive-Bayes with sigmoid calibration
clf_sigmoid = CalibratedClassifierCV(clf, cv=5, method='sigmoid')
clf_sigmoid.fit(matrix_t, label)
print('RandomForestClassifier:')
#scores = cross_val_score(clf, matrix_test_t, label_test)#scores on Y
scores = cross_val_score(clf, matrix_t, label) #scores on X
print('clf:')
print(scores.mean())
#scores = cross_val_score(clf_isotonic, matrix_test_t, label_test)
scores = cross_val_score(clf_isotonic, matrix_t, label) #scores on X
print('clf_isotonic:')
print(scores.mean())
#scores = cross_val_score(clf_sigmoid, matrix_test_t, label_test)
scores = cross_val_score(clf_sigmoid, matrix_t, label) #scores on X
print('clf_sigmoid:')
print(scores.mean())

###below is code for regular CLF
print('predicted classes:')
results = clf.predict(matrix_test_t)
probabilities = clf.predict_proba(matrix_test_t)
print(probabilities)
f3 = open('predicted_RandomForest_class.txt','w')
f3_prob = open('predicted_RandomForest_probablities.txt','w')
for each in results:
    print(each, file = f3)
f3.close()
for each in probabilities:
    print(each, file = f3_prob)
f3_prob.close()

'''
###SVC#####
clf = SVC(kernel='rbf', probability=True) #initialize the classifier
imp.fit(matrix)#fit the imputer on training matrix
matrix_t = imp.transform(matrix)# handling missing values of training matrix
clf = clf.fit(matrix_t, label) # fit classifier on transformed matrix_t
matrix_test_t = imp.transform(matrix_test)#handling missing values of testing matrix
scores = cross_val_score(clf, matrix_test_t, label_test)
print('SVC:')
print(scores.mean())
print('predicted classes:')
print(clf.predict(matrix_test_t))#testing code to print out preditced methods

###LogisticRegression#####
clf = linear_model.LogisticRegression()  #initialize the classifier
imp.fit(matrix)#fit the imputer on training matrix
matrix_t = imp.transform(matrix)# handling missing values of training matrix
clf = clf.fit(matrix_t, label) # fit classifier on transformed matrix_t
matrix_test_t = imp.transform(matrix_test)#handling missing values of testing matrix
scores = cross_val_score(clf, matrix_test_t, label_test)
print('LogisticRegression:')
print(scores.mean())
print('predicted classes:')
print(clf.predict(matrix_test_t))#testing code to print out preditced methods
'''