from sklearn.svm import SVC
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

################
clf3 = SVC(kernel='rbf', probability=True)
clf3 = clf3.fit(matrix, label)
scores = cross_val_score(clf3, matrix, label)
print(scores.mean())

#0.410539215686




'''
lines = [line.rstrip('\n') for line in open('100Sampling_feature_vector.txt')]
label = [] #y
matrix = [] #x
for l in lines:
    l = l[1:-1]
    vector = l.split(', ')
    matrix.append(vector[:-1])
    print(vector)
    label.append(vector[8])
#print(label)
#print(matrix)

'''
