import re
import random
import json
from random import choice, sample, randint

Test = []
with open('elec_pairs_stage4.txt', 'r') as f:
    lines = f.readlines()
    sampling_number = random.sample(lines, 1000)
    #print(sampling_number)
    for i in sampling_number:     
        items = i.split('?')
        json_id1 = items[1]
        json_id2 = items[3]
        id1 = re.findall(r'[\d|]+', json_id1)
        id2 = re.findall(r'[\d|]+', json_id2)
        json_data1 = json.loads(items[2])  
        json_data2 = json.loads(items[4])
        Test.append(i)

x = open('1000Sampling.txt','w')
for each in Test:
    print(each, end = '', file = x)
x.close()
f.close()
