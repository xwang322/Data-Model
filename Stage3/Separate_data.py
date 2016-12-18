import re
import random
import json
from random import choice, sample, randint

line_num = list(range(1,20001))
training_line_num = random.sample(range(1, 20001), 10000)
training_line_num.sort()
training_line_num_tmp = set(training_line_num)
line_num_tmp = set(line_num)
test_line_num = list(line_num_tmp.difference(training_line_num_tmp))
with open('elec_pairs_stage1.txt', 'r') as f:
    lines = f.readlines()
    a = open('X.txt','w')
    for each in training_line_num:
        print(lines[each-1], end = '', file = a)
    a.close()
    b = open('Y.txt','w')
    for each in test_line_num:
        print(lines[each-1], end = '', file = b)
    b.close()
f.close()

