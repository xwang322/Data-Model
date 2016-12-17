import re

missing_X = []
with open('predictions_X.txt', 'r') as f:
    r = 1 
    j = 1
    a = open('X_missing_index.txt','w')
    for line in f:
        line = line.split(',')
        label = line[1].replace('\n','')
        label = label.strip()
        #print(label)
        if(label.lower() == 'unknown'):
            missing_X.append(line[0])
            print(str(j) + ':' + line[0], file = a)
            j += 1
        r += 1
    #print(missing_X)
    a.close()
f.close()

missing_Y = []
with open('predictions_Y.txt', 'r') as f:
    r = 1
    j = 1
    a = open('Y_missing_index.txt','w')
    for line in f:
        line = line.split(',')
        label = line[1].replace('\n','')
        label = label.strip()
        #print(label)
        if(label.lower() == 'unknown'):
            missing_Y.append(line[0])
            print(str(j) + ':' + line[0], file = a)
            j += 1
        r += 1
    #print(missing_Y)
    a.close()
f.close()

with open('X.txt', 'r') as f:
    r = 1
    a = open('X_missing.txt','w')
    for line in f:
        if(str(r) in missing_X):
            print(str(r) + ':' + line, end = '', file = a)
        r += 1
    a.close()
f.close()

with open('Y.txt', 'r') as f:
    r = 1
    a = open('Y_missing.txt','w')
    for line in f:
        if(str(r) in missing_Y):
            print(str(r) + ':' +line, end = '', file = a)
        r += 1
    a.close()
f.close()



