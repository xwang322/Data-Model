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
    label.append(vector[59])   #this depends on the number of the columns########
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
    label_test.append(vector_test[59])####################
a_test = np.array(label_test, dtype = '|S4')
b_test = a_test.astype(np.float)
label_test = b_test
###RandomForestClassifier#####

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

print("RandomForestClassifier")
#scores = cross_val_score(clf, matrix_test_t, label_test)#scores on Y
scores = cross_val_score(clf, matrix_t, label, cv = 5) #scores on X
print("clf_accuracy")
print(scores.mean())

scores = cross_val_score(clf, matrix_t, label, cv = 5, scoring= 'precision') #scores on X
print("clf_precision")
print(scores.mean())

scores = cross_val_score(clf, matrix_t, label, cv = 5, scoring= 'f1') #scores on X
print("clf_f1")
print(scores.mean())

scores = cross_val_score(clf, matrix_t, label, cv = 5, scoring= 'recall') #scores on X
print("clf_recall")
print(scores.mean())
#scores = cross_val_score(clf_isotonic, matrix_test_t, label_test)
scores = cross_val_score(clf_isotonic, matrix_t, label, cv = 5) #scores on X
print("clf_isotonic_accuracy")
print(scores.mean())

scores = cross_val_score(clf_isotonic, matrix_t, label, cv = 5, scoring= 'precision') #scores on X
print("clf_isotonic_precision")
print(scores.mean())

scores = cross_val_score(clf, matrix_t, label, cv = 5, scoring= 'f1') #scores on X
print("clf_isotonic_f1")
print(scores.mean())

scores = cross_val_score(clf, matrix_t, label, cv = 5, scoring= 'recall') #scores on X
print("clf_isotonic_recall")
print(scores.mean())

#scores = cross_val_score(clf_sigmoid, matrix_test_t, label_test)
scores = cross_val_score(clf_sigmoid, matrix_t, label, cv = 5) #scores on X
print("clf_sigmoid_accuracy")
print(scores.mean())

scores = cross_val_score(clf_sigmoid, matrix_t, label, cv = 5, scoring= 'precision') #scores on X
print("clf_sigmoid_precision")
print(scores.mean())

scores = cross_val_score(clf, matrix_t, label, cv = 5, scoring= 'f1') #scores on X
print("clf_sigmoid_f1")
print(scores.mean())

scores = cross_val_score(clf, matrix_t, label, cv = 5, scoring= 'recall') #scores on X
print("clf_sigmoid_recall")
print(scores.mean())

###below is code for regular CLF

###for training set########
print("predicted classes without unknowns, with unknowns, and probabilities for training set will be printed to three txt files:")
results = clf.predict(matrix_t) ###might need to use clf_sigmoid instead###
probabilities = clf.predict_proba(matrix_t)

f3 = open('sampling_predicted_RandomForest_class.txt','w')
f3_prob = open('sampling_predicted_RandomForest_probablities.txt','w')
f4 = open('sampling_predicted_RandomForest_labels_unknown added.txt','w')

###below is to manually? calculate the overall precision for training set########

for each in results:
    print(each, file = f3)
f3.close()

pos = 0
truepos = 0
equal = 0
i = 0
for each in probabilities:
    diff = each[1]-each[0]
    print(each, file = f3_prob)
    if diff == 0:
        equal = equal+1
        print(str(i+1)+':',"UNKNOWN", file = f4)
    if diff > 0:
        pos = pos +1
        if label[i] == 1:
            truepos = truepos +1
        print(str(i+1)+':',"MATCH", file = f4)
    if diff < 0:
        print(str(i+1)+':',"MISMATCH", file = f4)
    i = i+1
f3_prob.close()
f4.close

print("number of equal probability:")
print(equal)

print("precision:")
pre = truepos/pos
print(pre)

