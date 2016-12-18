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
lines = [line.rstrip('\n') for line in open('X_feature_vector.txt')]
label = []
matrix = []
for l in lines:
    l = l[1:-1]
    vector = l.split(', ')
    x = np.array(vector[:-1], dtype = '|S4')
    y = x.astype(np.float)
    matrix.append(y)
    label.append(vector[len(x)])   #this depends on the number of the columns########
a = np.array(label, dtype = '|S4')
b = a.astype(np.float)
label = b


############################

#####this part is to convert testing set file to proper format#####
lines_test = [line.rstrip('\n') for line in open('Y_feature_vector.txt')]

label_test = []
matrix_test = []
for l in lines_test:
    l = l[1:-1]
    vector_test = l.split(', ')
    x_test = np.array(vector_test[:-1], dtype = '|S4')
    y_test = x_test.astype(np.float)
    matrix_test.append(y_test)
    label_test.append(vector_test[len(x_test)])####################
##debugging code to be deleted##
'''
print("line 37\n")
print(matrix_test)
print(label_test)
'''
##debugging code to be deleted##
a_test = np.array(label_test, dtype = '|S4')
b_test = a_test.astype(np.float)
label_test = b_test
################################################


###RandomForestClassifier#####


#####  1st fold######

matrix_s1=matrix_test[0:8000]
matrix_t1=matrix_test[8000:]
label_s1=label_test[0:8000]
label_t1 = label_test[8000:]

clf = RandomForestClassifier(n_estimators = 10)
imp.fit(matrix_s1)#fit the imputer on training matrix######
matrix_t = imp.transform(matrix_s1)# handling missing values of training matrix
matrix_test_t = imp.transform(matrix_t1)#handling missing values of testing matrix

clf = clf.fit(matrix_t, label_s1) # fit classifier on transformed matrix_t

clf_isotonic = CalibratedClassifierCV(clf, cv=5, method='isotonic')
clf_isotonic.fit(matrix_t, label_s1)


# Gaussian Naive-Bayes with sigmoid calibration
clf_sigmoid = CalibratedClassifierCV(clf, cv=5, method='sigmoid')
clf_sigmoid.fit(matrix_t, label_s1)

'''
scores = cross_val_score(clf, imp.transform(matrix), label, cv = 5, scoring= 'precision') #scores on X
print("\nclf_precision\n")
print(scores)
'''

results = clf.predict(matrix_test_t)
probabilities = clf.predict_proba(matrix_test_t)

'''
results = clf_isotonic.predict(matrix_test_t)
probabilities = clf_isotonic.predict_proba(matrix_test_t)

results = clf_sigmoid.predict(matrix_test_t)
probabilities = clf_sigmoid.predict_proba(matrix_test_t)
'''
print(len(results))
print(len(probabilities))
print(probabilities)

pos = 0
truepos = 0
equal = 0
i = 0
threshold = 0.4
for each in probabilities:
    diff = abs(each[1]-each[0])
    if diff <= threshold:
        equal = equal+1
    elif (each[1]-each[0]) > threshold:
        pos = pos +1
        if label_t1[i] == 1:
            truepos = truepos +1
    i = i+1

actual_pos = 0
for each in results:
    if each == 1:
        actual_pos = actual_pos +1

print("\nnumber of equal probability:")
print(equal)
print("\nnumber of pos:")
print(pos)
print("\nnumber of truepos:")
print(truepos)
print("\nnumber of actual_pos:")
print(actual_pos)
print("\nprecision:")
pre1 = truepos/pos
print(pre1)
print("\nrecall:")
recall1 = truepos/actual_pos
print(recall1)
F1_1 = 2*(pre1*recall1)/(pre1 + recall1)
print("\nF1:\n\n")
print(F1_1)


####### 2nd fold##############################

matrix_s1=matrix_test[2000:]#1000-5000
matrix_t1=matrix_test[0:2000]
label_s1=label_test[2000:]
label_t1 = label_test[0:2000]

clf = RandomForestClassifier(n_estimators = 10)
imp.fit(matrix_s1)#fit the imputer on training matrix######
matrix_t = imp.transform(matrix_s1)# handling missing values of training matrix
matrix_test_t = imp.transform(matrix_t1)#handling missing values of testing matrix

clf = clf.fit(matrix_t, label_s1) # fit classifier on transformed matrix_t

clf_isotonic = CalibratedClassifierCV(clf, cv=5, method='isotonic')
clf_isotonic.fit(matrix_t, label_s1)


# Gaussian Naive-Bayes with sigmoid calibration
clf_sigmoid = CalibratedClassifierCV(clf, cv=5, method='sigmoid')
clf_sigmoid.fit(matrix_t, label_s1)
'''
scores = cross_val_score(clf, imp.transform(matrix), label, cv = 5, scoring= 'precision') #scores on X
print("\nclf_precision\n")
print(scores)
'''
results = clf.predict(matrix_test_t)
probabilities = clf.predict_proba(matrix_test_t)
print(len(results))
print(len(probabilities))

pos = 0
truepos = 0
equal = 0
i = 0
threshold = 0.4
for each in probabilities:
    diff = abs(each[1]-each[0])
    if diff <= threshold:
        equal = equal+1
    elif (each[1]-each[0]) > threshold:
        pos = pos +1
        if label_t1[i] == 1:
            truepos = truepos +1
    i = i+1

actual_pos = 0
for each in results:
    if each == 1:
        actual_pos = actual_pos +1

print("\nnumber of equal probability:")
print(equal)
print("\nnumber of pos:")
print(pos)
print("\nnumber of truepos:")
print(truepos)
print("\nnumber of actual_pos:")
print(actual_pos)
print("\nprecision:")
pre2 = truepos/pos
print(pre2)
print("\nrecall:")
recall2 = truepos/actual_pos
print(recall2)
F1_2 = 2*(pre2 * recall2)/(pre2 + recall2)
print("\nF1:\n\n")
print(F1_2)




####### 3rd fold##############################

matrix_s1=matrix_test[0:2000]#0-1000+2000-5000
for each in matrix_test[4000:]:
    matrix_s1.append(each)
print("length of matrix_s1:")
print(len(matrix_s1))

matrix_t1=matrix_test[2000:4000]

label_s1=np.concatenate((label_test[0:2000],label_test[4000:]), axis = 0)
print(label_s1)
print("length of label_s1:")
print(len(label_s1))

label_t1 = label_test[2000:4000]


clf = RandomForestClassifier(n_estimators = 10)
imp.fit(matrix_s1)#fit the imputer on training matrix######
matrix_t = imp.transform(matrix_s1)# handling missing values of training matrix
matrix_test_t = imp.transform(matrix_t1)#handling missing values of testing matrix

clf = clf.fit(matrix_t, label_s1) # fit classifier on transformed matrix_t

clf_isotonic = CalibratedClassifierCV(clf, cv=5, method='isotonic')
clf_isotonic.fit(matrix_t, label_s1)


# Gaussian Naive-Bayes with sigmoid calibration
clf_sigmoid = CalibratedClassifierCV(clf, cv=5, method='sigmoid')
clf_sigmoid.fit(matrix_t, label_s1)
'''
scores = cross_val_score(clf, imp.transform(matrix), label, cv = 5, scoring= 'precision') #scores on X
print("\nclf_precision\n")
print(scores)
'''
results = clf.predict(matrix_test_t)
probabilities = clf.predict_proba(matrix_test_t)
print(len(results))
print(len(probabilities))

pos = 0
truepos = 0
equal = 0
i = 0
threshold = 0.4
for each in probabilities:
    diff = abs(each[1]-each[0])
    if diff <= threshold:
        equal = equal+1
    elif (each[1]-each[0]) > threshold:
        pos = pos +1
        if label_t1[i] == 1:
            truepos = truepos +1
    i = i+1

actual_pos = 0
for each in results:
    if each == 1:
        actual_pos = actual_pos +1

print("\nnumber of equal probability:")
print(equal)
print("\nnumber of pos:")
print(pos)
print("\nnumber of truepos:")
print(truepos)
print("\nnumber of actual_pos:")
print(actual_pos)
print("\nprecision:")
pre3 = truepos/pos
print(pre3)
print("\nrecall:")
recall3 = truepos/actual_pos
print(recall3)
F1_3 = 2*(pre3 * recall3)/(pre3 + recall3)
print("\nF1:\n\n")
print(F1_3)


####### 4th fold##############################

matrix_s1=matrix_test[0:4000]#0-2000+3000-5000
for each in matrix_test[6000:]:
    matrix_s1.append(each)
print("length of matrix_s1:")
print(len(matrix_s1))

matrix_t1=matrix_test[4000:6000]

label_s1=np.concatenate((label_test[0:4000],label_test[6000:]), axis = 0)
print(label_s1)
print("length of label_s1:")
print(len(label_s1))

label_t1 = label_test[4000:6000]


clf = RandomForestClassifier(n_estimators = 10)
imp.fit(matrix_s1)#fit the imputer on training matrix######
matrix_t = imp.transform(matrix_s1)# handling missing values of training matrix
matrix_test_t = imp.transform(matrix_t1)#handling missing values of testing matrix

clf = clf.fit(matrix_t, label_s1) # fit classifier on transformed matrix_t

clf_isotonic = CalibratedClassifierCV(clf, cv=5, method='isotonic')
clf_isotonic.fit(matrix_t, label_s1)


# Gaussian Naive-Bayes with sigmoid calibration
clf_sigmoid = CalibratedClassifierCV(clf, cv=5, method='sigmoid')
clf_sigmoid.fit(matrix_t, label_s1)
'''
scores = cross_val_score(clf, imp.transform(matrix), label, cv = 5, scoring= 'precision') #scores on X
print("\nclf_precision\n")
print(scores)
'''
results = clf.predict(matrix_test_t)
probabilities = clf.predict_proba(matrix_test_t)
print(len(results))
print(len(probabilities))

pos = 0
truepos = 0
equal = 0
i = 0
threshold = 0.4
for each in probabilities:
    diff = abs(each[1]-each[0])
    if diff <= threshold:
        equal = equal+1
    elif (each[1]-each[0]) > threshold:
        pos = pos +1
        if label_t1[i] == 1:
            truepos = truepos +1
    i = i+1


actual_pos = 0
for each in results:
    if each == 1:
        actual_pos = actual_pos +1

print("\nnumber of equal probability:")
print(equal)
print("\nnumber of pos:")
print(pos)
print("\nnumber of truepos:")
print(truepos)
print("\nnumber of actual_pos:")
print(actual_pos)
print("\nprecision:")
pre4 = truepos/pos
print(pre4)
print("\nrecall:")
recall4 = truepos/actual_pos
print(recall4)
F1_4 = 2*(pre4 * recall4)/(pre4 + recall4)
print("\nF1:\n\n")
print(F1_4)


####### 5th fold##############################

matrix_s1=matrix_test[0:6000]#0-3000+4000-5000
for each in matrix_test[8000:]:
    matrix_s1.append(each)
print("length of matrix_s1:")
print(len(matrix_s1))

matrix_t1=matrix_test[6000:8000]

label_s1=np.concatenate((label_test[0:6000],label_test[8000:]), axis = 0)
print(label_s1)
print("length of label_s1:")
print(len(label_s1))

label_t1 = label_test[6000:8000]


clf = RandomForestClassifier(n_estimators = 10)
imp.fit(matrix_s1)#fit the imputer on training matrix######
matrix_t = imp.transform(matrix_s1)# handling missing values of training matrix
matrix_test_t = imp.transform(matrix_t1)#handling missing values of testing matrix

clf = clf.fit(matrix_t, label_s1) # fit classifier on transformed matrix_t

clf_isotonic = CalibratedClassifierCV(clf, cv=5, method='isotonic')
clf_isotonic.fit(matrix_t, label_s1)


# Gaussian Naive-Bayes with sigmoid calibration
clf_sigmoid = CalibratedClassifierCV(clf, cv=5, method='sigmoid')
clf_sigmoid.fit(matrix_t, label_s1)
'''
scores = cross_val_score(clf, imp.transform(matrix), label, cv = 5, scoring= 'precision') #scores on X
print("\nclf_precision\n")
print(scores)
'''
results = clf.predict(matrix_test_t)
probabilities = clf.predict_proba(matrix_test_t)
print(len(results))
print(len(probabilities))

pos = 0
truepos = 0
equal = 0
i = 0
threshold = 0.4
for each in probabilities:
    diff = abs(each[1]-each[0])
    if diff <= threshold:
        equal = equal+1
    elif (each[1]-each[0]) > threshold:
        pos = pos +1
        if label_t1[i] == 1:
            truepos = truepos +1
    i = i+1



actual_pos = 0
for each in results:
    if each == 1:
        actual_pos = actual_pos +1

print("\nnumber of equal probability:")
print(equal)
print("\nnumber of pos:")
print(pos)
print("\nnumber of truepos:")
print(truepos)
print("\nnumber of actual_pos:")
print(actual_pos)
print("\nprecision:")
pre5 = truepos/pos
print(pre5)
print("\nrecall:")
recall5 = truepos/actual_pos
print(recall5)
F1_5 = 2*(pre5 * recall5)/(pre5 + recall5)
print("\nF1:\n\n")
print(F1_5)


print("FINAL RESULTS on Y:")
print("\nprecision:")
print(pre1)
print(pre2)
print(pre3)
print(pre4)
print(pre5)
print("\nrecall:")
print(recall1)
print(recall2)
print(recall3)
print(recall4)
print(recall5)
print("\nF1:")
print(F1_1)
print(F1_2)
print(F1_3)
print(F1_4)
print(F1_5)
print("\n\n average precision:")
print((pre1+pre2+pre3+pre4+pre5)/5)
print("\n\n average recall:")
print((recall1+recall2+recall3+recall4+recall5)/5)
print("\n\n average F1:")
print((F1_1+F1_2+F1_3+F1_4+F1_5)/5)
