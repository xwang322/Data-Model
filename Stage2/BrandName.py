import json
import re
import random
#from collections import Counter  
from random import choice, sample, randint

class BrandName:	
    attrName = ''
    attrDetails = []
		
    def __init__(self, attrName, attrDetail):
        self.attrName = attrName
        self.attrDetails.append(attrDetail)

    def insert(self, attrDetail):
        self.attrDetails.append(attrDetail)

Name_coll = {} # this attrdict defines the dictionary which saves every json attribute brand name and its occurance
match_count = 0
id_list = []
id_distinct_list = [] 

with open('one_pair_test_stage2.txt', 'r') as f:
    for line in f:
        items = line.split('?')
        json_id1 = items[1]
        json_id2 = items[3]
        id1 = re.findall(r'[\d|]+', json_id1)
        id2 = re.findall(r'[\d|]+', json_id2)
        if (id1 == id2):
            match_count += 1
            id_list.append(id1)
        else:
            id_list.append(id1)
            id_list.append(id2)
    #print(id_list)
    for item in id_list:
        if (item  not in id_distinct_list):
            id_distinct_list.append(item)
#print(len(id_distinct_list))            
#print(match_count)
f.close()

cnt = 0
with open('one_pair_test_stage2.txt','r') as f:
    r = 0;
    for line in f:
        r += 1
        items = line.split('?')
        json_data1 = json.loads(items[2])  
        json_data2 = json.loads(items[4])
        for x in json_data1:
            if (x == 'Product Name'):
                if (r == 1):
                    Name_coll.setdefault(x, 1)
                else:
                    if (x not in Name_coll):
                        Name_coll.setdefault(x, 1)
                    else:
                        Name_coll[x] = Name_coll.setdefault(x, 1) + 1
                cnt += 1
        for x in json_data2:
            if (x == 'Product Name'):
                if (x not in Name_coll):
                    Name_coll.setdefault(x, 1)
                else:
                    Name_coll[x] = Name_coll.setdefault(x, 1) + 1
                cnt += 1
#print(cnt)
#print(Name_coll)
f.close()

BrandList = BrandName('Product Name', '')
random_line_num = random.sample(range(1, 10001), 360)
random_line_num.sort()
#print(random_line_num)
with open('elec_pairs_stage2.txt','r',encoding='UTF-8') as f:
    lines = f.readlines()
    for i in random_line_num:
        x = lines[i-1]    
        #print(x)        
        items = x.split('?')
        json_data1 = json.loads(items[2])
        #json_data2 = json.loads(items[4])
        for each in json_data1.keys():
            aname = each
            bname = json_data1.get(aname) 
            cname = ''.join(bname)            
            if (aname == 'Product Name'):
                BrandList.insert(cname)
        '''
        for each in json_data2.keys():
            aname = each
            bname = json_data2.get(aname)
            cname = ''.join(bname)
            if (aname == 'Product Name'):
                BrandList.insert(cname)
        '''
#print(BrandList.attrDetails)

z = open("BrandName_for_all.txt",'w')
for index in range(len(BrandList.attrDetails) - 1):
    print(str(index + 1) + ':' + BrandList.attrDetails[index+1], file = z)
z.close()
f.close()
