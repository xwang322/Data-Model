from sklearn import linear_model
from sklearn.cross_validation import cross_val_score
import numpy as np


lines = [line.rstrip('\n') for line in open('100Sampling_feature_vector.txt')]
label = [] #y
matrix = [] #x
for l in lines:
    l = l[1:-1]
    vector = l.split(', ')
    x = np.array(vector[:-1], dtype = '|S4')
    y = x.astype(np.float)
    matrix.append(y)
    #print(y)
    label.append(vector[8])
a = np.array(label, dtype = '|S4')
b = a.astype(np.float)
label = b
#print(label)
#print(matrix)

################
clf2 = linear_model.LogisticRegression() #????????????#
clf2 = clf2.fit(matrix, label)
scores = cross_val_score(clf2, matrix, label)
print(scores.mean())

#0.780024509804
