import json
import operator
from decimal import*
import matplotlib.pyplot as plt
import numpy as np
import re
from collections import Counter  

# Please read the file and understand it first then choose which part you want to run

class One:	
    attrName = ''
    attrDetailsOne = []
		
    def __init__(self, attrName, attrDetail):
        self.attrName = attrName
        self.attrDetailsOne.append(attrDetail)

    def insert(self, attrDetail):
        self.attrDetailsOne.append(attrDetail)

class Two:	
    attrName = ''
    attrDetailsTwo = []
		
    def __init__(self, attrName, attrDetail):
        self.attrName = attrName
        self.attrDetailsTwo.append(attrDetail)

    def insert(self, attrDetail):
        self.attrDetailsTwo.append(attrDetail)

class Three:	
    attrName = ''
    attrDetailsThree = []
		
    def __init__(self, attrName, attrDetail):
        self.attrName = attrName
        self.attrDetailsThree.append(attrDetail)

    def insert(self, attrDetail):
        self.attrDetailsThree.append(attrDetail)

class Four:	
    attrName = ''
    attrDetailsFour = []
		
    def __init__(self, attrName, attrDetail):
        self.attrName = attrName
        self.attrDetailsFour.append(attrDetail)

    def insert(self, attrDetail):
        self.attrDetailsFour.append(attrDetail)

class Five:	
    attrName = ''
    attrDetailsFive = []
		
    def __init__(self, attrName, attrDetail):
        self.attrName = attrName
        self.attrDetailsFive.append(attrDetail)

    def insert(self, attrDetail):
        self.attrDetailsFive.append(attrDetail)

class Six:	
    attrName = ''
    attrDetailsSix = []
		
    def __init__(self, attrName, attrDetail):
        self.attrName = attrName
        self.attrDetailsSix.append(attrDetail)

    def insert(self, attrDetail):
        self.attrDetailsSix.append(attrDetail)

class Seven:	
    attrName = ''
    attrDetailsSeven = []
		
    def __init__(self, attrName, attrDetail):
        self.attrName = attrName
        self.attrDetailsSeven.append(attrDetail)

    def insert(self, attrDetail):
        self.attrDetailsSeven.append(attrDetail)

class Eight:	
    attrName = ''
    attrDetailsEight = []
		
    def __init__(self, attrName, attrDetail):
        self.attrName = attrName
        self.attrDetailsEight.append(attrDetail)

    def insert(self, attrDetail):
        self.attrDetailsEight.append(attrDetail)

class Nine:	
    attrName = ''
    attrDetailsNine = []
		
    def __init__(self, attrName, attrDetail):
        self.attrName = attrName
        self.attrDetailsNine.append(attrDetail)

    def insert(self, attrDetail):
        self.attrDetailsNine.append(attrDetail)

class Ten:	
    attrName = ''
    attrDetailsTen = []
		
    def __init__(self, attrName, attrDetail):
        self.attrName = attrName
        self.attrDetailsTen.append(attrDetail)

    def insert(self, attrDetail):
        self.attrDetailsTen.append(attrDetail)

attrdict = {} # this attrdict defines the dictionary which saves every json attribute name and its occurance
 
match_count = 0
id_list = []
id_distinct_list = [] 
with open('elec_pairs_stage1.txt', 'r') as f:
    for line in f:
        items = line.split('?')
        json_id1 = items[1]
        json_id2 = items[3]
        id1 = re.findall(r'[\d|]+', json_id1)
        id2 = re.findall(r'[\d|]+', json_id2)
        if (id1 == id2):
            match_count +=1
            id_list.append(id1)
        else:
            id_list.append(id1)
            id_list.append(id2)
    # print(id_list)
    for item in id_list:
        if (item  not in id_distinct_list):
            id_distinct_list.append(item)
            # print(item)
#print(len(id_distinct_list))            
#print(match_count)
f.close()

cnt = 0
with open('elec_pairs_stage1.txt','r') as f:
    r = 0;
    for line in f:
        r += 1
        items = line.split('?')
        json_data1 = json.loads(items[2])  
        json_data2 = json.loads(items[4])

        for x in json_data1:
            if (r == 1):
                attrdict.setdefault(x, 1)
            else:
                if (x not in attrdict):
                    attrdict.setdefault(x, 1)
                else:
                    attrdict[x] = attrdict.setdefault(x, 1) + 1
            cnt += 1

        for x in json_data2:
            if (x not in attrdict):
                attrdict.setdefault(x, 1)
            else:
                attrdict[x] = attrdict.setdefault(x, 1) + 1
            cnt += 1
print(cnt)
sorted_dict = sorted(attrdict.items(), key = operator.itemgetter(1), reverse = True)
missing_dict = sorted_dict[:]
missing_tmp = []


cnt = 0
go_cnt = 0
with open('elec_pairs_stage1.txt','r') as f:
    r = 0;
    for line in f:
        r += 1
        items = line.split('?')
        json_data1 = json.loads(items[2])  
        json_data2 = json.loads(items[4])
        json_id1 = items[1]
        json_id2 = items[3]
        id1 = re.findall(r'[\d|]+', json_id1)
        id2 = re.findall(r'[\d|]+', json_id2)
        if (id1 == id2):
            go_cnt += 1
        for x in json_data1:
            if (r == 1):
                attrdict.setdefault(x, 1)
            else:
                if (x not in attrdict):
                    attrdict.setdefault(x, 1)
                else:
                    attrdict[x] = attrdict.setdefault(x, 1) + 1
            cnt += 1

        for x in json_data2:
            if (id1 != id2):
                if (x not in attrdict):
                    attrdict.setdefault(x, 1)
                else:
                    attrdict[x] = attrdict.setdefault(x, 1) + 1
                cnt += 1
            else:
                pass
# print(go_cnt)
# print(cnt)
sorted_dict = sorted(attrdict.items(), key = operator.itemgetter(1), reverse = True)
missing_dict = sorted_dict[:]
missing_tmp = []

for item in missing_dict:
    a = list(item)
    missing_tmp.append(a)

for index in range(len(missing_tmp)):
    a = float((40000 - go_cnt - missing_tmp[index][1])) / float(40000 - go_cnt)
    a = ("%.5f" % a)
    missing_tmp[index][1] = a
missing_dict = tuple(missing_tmp)
print(missing_dict)	# this will print out the missing rate of each attribute 585 missing rate
f.closed

#print(missing_tmp)
z = open("attrAppearance.txt",'w')
for index in range(len(missing_tmp)):
    b = int((1 - float(missing_tmp[index][1])) * (40000 - go_cnt))
    #print(b)
    print(missing_dict[index][0] + ':' + str(b) + ',', end = '', file = z)
z.close()

# output the all attrnames in a file
f = open("attrnames.txt",'w')
for item in missing_dict:
    print(item[0] + ',', end = '', file = f)
f.close()

interest_attr = []
for x in range(10):
    interest_attr.append(missing_dict[x][0])
print(interest_attr)  # you can use this to print out the first ten attributes, most frequent

OneInst   = One(interest_attr[0], '')
TwoInst   = Two(interest_attr[1], '')
ThreeInst = Three(interest_attr[2], '')
FourInst  = Four(interest_attr[3], '')
FiveInst  = Five(interest_attr[4], '')
SixInst   = Six(interest_attr[5], '')
SevenInst = Seven(interest_attr[6], '')
EightInst = Eight(interest_attr[7], '')
NineInst  = Nine(interest_attr[8], '')
TenInst   = Ten(interest_attr[9], '')

Total = [OneInst, TwoInst, ThreeInst, FourInst, FiveInst, SixInst, SevenInst, EightInst, NineInst, TenInst]

with open('elec_pairs_stage1.txt','r') as s:
    for line in s:   
        items = line.split('?')
        json_data1 = json.loads(items[2])
        json_data2 = json.loads(items[4])
        attrPost = 0
        for each in json_data1.keys():
            aname = each
            bname = json_data1.get(aname) 
            cname = ''.join(bname)                    			
            if aname in interest_attr:
                attrPost = interest_attr.index(aname)
                Total[attrPost].insert(cname)

        for each in json_data2.keys():
            aname = each
            bname = json_data2.get(aname)
            cname = ''.join(bname)
            if aname in interest_attr:
                attrPost = interest_attr.index(aname)
                Total[attrPost].insert(cname)
#print(Total[0].attrDetailsOne) # when you print sth, you have to print [x] with attrDetails(x+1)

'''
a1 = {}
a2 = {}
count1 = [] # this is for counting the length of each key in a1
print(Total[0].attrName)
for item in Total[0].attrDetailsOne:
    count1.append(len(item))
    if (len(item) == 3):
        print(item)
for item in Total[0].attrDetailsOne:
    a1[item] = Total[0].attrDetailsOne.count(item)
#print(a1)
for item in count1:
    a2[item] = count1.count(item)
print(a2) # a2 will help to see the length of each key in a1 and return their counts
'''
'''
b1 = {}
b2 = {}
count2 = []
for item in Total[1].attrDetailsTwo:
    count2.append(len(item))
for item in Total[1].attrDetailsTwo:
    b1[item] = Total[1].attrDetailsTwo.count(item)
# print(b1) 
for item in count2:
    b2[item] = count2.count(item)
#print(b2)


c1 = {}
c2 = {}
count3 = []
for item in Total[2].attrDetailsThree:
    count3.append(len(item))
for item in Total[2].attrDetailsThree:
    c1[item] = Total[2].attrDetailsThree.count(item)
#print(c1) 
for item in count3:
    c2[item] = count3.count(item)
# print(c2)
'''
'''
d1 = {}
d2 = {}
count4 = []
print(Total[3].attrName)
for item in Total[3].attrDetailsFour:
    count4.append(len(item))
    if (len(item) == 1):
        print(item)
for item in Total[3].attrDetailsFour:
    d1[item] = Total[3].attrDetailsFour.count(item)
#print(d1) 
for item in count4:
    d2[item] = count4.count(item)
print(d2)
'''
'''
e1 = {}
e2 = {}
count5 = []
print(Total[4].attrName)
for item in Total[4].attrDetailsFive:    
    count5.append(len(item))
    if (len(item) == 1):
        print(item)
for item in Total[4].attrDetailsFive:
    e1[item] = Total[4].attrDetailsFive.count(item)
#print(e1) 
for item in count5:
    e2[item] = count5.count(item)
print(e2)
'''
'''
f1 = {}
f2 = {}
count6 = []
print(Total[5].attrName)
for item in Total[5].attrDetailsSix:
    count6.append(len(item))
    if (len(item) == 1):
        print(item)
for item in Total[5].attrDetailsSix:
    f1[item] = Total[5].attrDetailsSix.count(item)
#print(f1) 
for item in count6:
    f2[item] = count6.count(item)
print(f2)
'''
'''
g1 = {}
g2 = {}
count7 = []
print(Total[6].attrName)
for item in Total[6].attrDetailsSeven:
    count7.append(len(item))
    if (len(item) == 37):
        print(item)
for item in Total[6].attrDetailsSeven:
    g1[item] = Total[6].attrDetailsSeven.count(item)
# print(g1) 
for item in count7:
    g2[item] = count7.count(item)
print(g2)
'''
'''
h1 = {}
h2 = {}
count8 = []
print(Total[7].attrName)
for item in Total[7].attrDetailsEight:
    count8.append(len(item))
for item in Total[7].attrDetailsEight:
    h1[item] = Total[7].attrDetailsEight.count(item)
#print(h1) 
for item in count8:
    h2[item] = count8.count(item)
print(h2)
'''
'''
i1 = {}
i2 = {}
count9 = []
for item in Total[8].attrDetailsNine:
    count9.append(len(item))
for item in Total[8].attrDetailsNine:
    i1[item] = Total[8].attrDetailsNine.count(item)
#print(i1) 
for item in count9:
    i2[item] = count9.count(item)
# print(i2)
'''
'''
j1 = {}
j2 = {}
count10 = []
for item in Total[9].attrDetailsTen:
    count10.append(len(item))
for item in Total[9].attrDetailsTen:
    j1[item] = Total[9].attrDetailsTen.count(item)
print(j1) 
for item in count10:
    j2[item] = count10.count(item)
#print(j2)
'''
s.closed 
