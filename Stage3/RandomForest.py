from sklearn.ensemble import RandomForestClassifier
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
clf1 = RandomForestClassifier(n_estimators = 10)
clf1 = clf1.fit(matrix, label)
scores = cross_val_score(clf1, matrix, label)
print(scores.mean())

#0.799632352941



'''
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end = ",")
    print('\n')
'''
