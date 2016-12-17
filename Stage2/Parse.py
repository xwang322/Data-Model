import re
import random
from random import choice, sample, randint

line_num = list(range(1,361))
training_line_num = random.sample(range(1, 361), 240)
training_line_num.sort()
training_line_num_tmp = set(training_line_num)
line_num_tmp = set(line_num)
test_line_num = list(line_num_tmp.difference(training_line_num_tmp))
with open('BrandName_for_all.txt', 'r') as f:
    lines = f.readlines()
    a = open('training_set.txt','w')
    for each in training_line_num:
        print(lines[each-1], end = '', file = a)
    a.close()
    b = open('test_set.txt','w')
    for each in test_line_num:
        print(lines[each-1], end = '', file = b)
    b.close()
f.close()

One_word_data = []
Two_word_data = []
Three_word_data = []
with open('BrandName_for_all.txt', 'r') as f:
    lines = f.readlines()
    for i in training_line_num:
        x = lines[i-1]    
        items = x.split(':')
        item_id = items[0]
        item_main = re.split(r'\s+', items[1].strip())
        item_one = []
        item_two = []
        item_three = []
        for each in range(len(item_main)):
            if ((item_main[each]).isdigit() != True and item_main[each] != '-'): # get rid of all single number and '-' because they cannot be single brand name
                item_one.append(item_main[each])
        for each in range(len(item_main)-1):
            item_two.append(item_main[each] + ' ' + item_main[each+1])
        for each in range(len(item_main)-2):
            item_three.append(item_main[each] + ' ' + item_main[each+1] + ' ' + item_main[each+2])
        One_word_data.append(str(item_id) + ':' + str(item_one))
        Two_word_data.append(str(item_id) + ':' + str(item_two))
        Three_word_data.append(str(item_id) + ':' + str(item_three))

x = open('one_word_training_data.txt','w')
for each in One_word_data:
    print(each, file = x)
x.close()
y = open('two_word_training_data.txt','w')
for each in Two_word_data:
    print(each, file = y)
y.close()
z = open('three_word_training_data.txt','w')
for each in Three_word_data:
    print(each, file = z)
z.close()
f.close()