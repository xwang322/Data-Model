from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn import linear_model
from sklearn.cross_validation import cross_val_score
from sklearn.calibration import CalibratedClassifierCV
import numpy as np
from sklearn.preprocessing import Imputer 
imp = Imputer(missing_values= 999, strategy='mean', axis=0)


lines = [line.rstrip('\n') for line in open('X_feature_vector_second_round.txt')]
label = []
matrix = []
for l in lines:
    l = l[1:-1]
    vector = l.split(', ')
    x = np.array(vector[:-1], dtype = '|S4')
    y = x.astype(np.float)
    matrix.append(y)
    label.append(vector[len(x)])   
a = np.array(label, dtype = '|S4')
b = a.astype(np.float)
label = b

lines_test = [line.rstrip('\n') for line in open('Y_feature_vector_second_round.txt')]
label_test = []
matrix_test = []
for l in lines_test:
    l = l[1:-1]
    vector_test = l.split(', ')
    x_test = np.array(vector_test[:-1], dtype = '|S4')
    y_test = x_test.astype(np.float)
    matrix_test.append(y_test)

clf = RandomForestClassifier(n_estimators = 10)
imp.fit(matrix)#fit the imputer on training matrix
matrix_t = imp.transform(matrix)# handling missing values of training matrix
clf = clf.fit(matrix_t, label) # fit classifier on transformed matrix_t
matrix_test_t = imp.transform(matrix_test)#handling missing values of testing matrix

'''
print("\n\n###RandomForestClassifier######:\n")
#scores = cross_val_score(clf, matrix_test_t, label_test)#scores on Y
scores = cross_val_score(clf, matrix_t, label, cv = 5) #scores on X
print("\nclf_accuracy\n")
print(scores.mean())

scores = cross_val_score(clf, matrix_t, label, cv = 5, scoring= 'precision') #scores on X
print("\nclf_precision\n")
print(scores.mean())

scores = cross_val_score(clf, matrix_t, label, cv = 5, scoring= 'f1') #scores on X
print("\nclf_f1\n")
print(scores.mean())

scores = cross_val_score(clf, matrix_t, label, cv = 5, scoring= 'recall') #scores on X
print("\nclf_recall\n")
print(scores.mean())
'''

results = clf.predict(matrix_test_t)
probabilities = clf.predict_proba(matrix_test_t)

print(probabilities)
f3_prob = open('sampling_predicted_RandomForest_probablities.txt','w')
f4 = open('predictions_22.txt','w')

for each in probabilities:
    print(each, file = f3_prob)
f3_prob.close()

equal = 0
i = 1
threshold = 0.4   #threshold can be changed here
for each in probabilities:
    diff = abs(each[1]-each[0])
    if diff <= threshold:
        equal = equal+1
        print(str(i)+", UNKNOWN", file = f4)
    elif (each[1]-each[0]) > threshold:
        print(str(i)+", MATCH", file = f4)
    else:
        print(str(i)+", MISMATCH", file = f4)
    i = i+1
f4.close

print("number of equal probability:")
print(equal)

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
        if label_test[i] == 1:
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

