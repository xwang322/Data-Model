from sklearn.naive_bayes import GaussianNB
from sklearn.cross_validation import cross_val_score
import numpy as np


lines = [line.rstrip('\n') for line in open('100Sampling_feature_vector.txt')]
label = [] 
matrix = [] 
for l in lines:
    l = l[1:-1]
    vector = l.split(', ')
    x = np.array(vector[:-1], dtype = '|S4')
    y = x.astype(np.float)
    matrix.append(y)
    label.append(vector[8])
a = np.array(label, dtype = '|S4')
b = a.astype(np.float)
label = b

clf = GaussianNB()
clf = clf.fit(matrix, label)
scores = cross_val_score(clf, matrix, label)
print(scores.mean())