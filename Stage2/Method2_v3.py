import re
from trie import Trie

# initialize a trie
trie = Trie()
with open('elec_brand_dic_revised_v2.txt', 'r') as f:
    lines = f.readlines()
    for each in lines:
        items = each.split(' \t ')
        #print(items[0])
        #print(items[1])
        tmp = ''
        for i in range(0, len(items)-1):
            tmp += items[i]
        tmp.strip()
        tmp = tmp.lower()
        value = items[len(items)-1]
        trie[tmp] = value


print('enermax')
kset = trie.keys('enermax')
print(kset)
print("enermax" in kset) 
# print its frequency
print(trie["enermax"])


# not sure for method2, do we need for one single word find all kset related and return the maximum freq or extend the search range to all related kset
# also consider the missing tuple and duplicate tuple issues, discuss with others.

train_result1 = []
train_result2 = []
train_result3 = []
found = 0
company_post = ['technology','tech','technologies','company','corp','corp.','llc','inc','inc.','co.','co','ltd','ltd.']
with open('one_word_training_data.txt', 'r') as z:
    lines = z.readlines()
    for line in lines:
        items = line.split(':')
        item_id = items[0]
        #print(items[1])
        item_tmp = items[1][items[1].find('[')+1 : items[1].find(']')]
        #print(item_tmp)
        item_main = item_tmp.split(',')
        #print(len(item_main))
        j = 0
        found_in_elif = False
        for each in item_main:
            #print(each)
            each = each.strip()
            each = each.lower()
            #if (each[len(each)-1] != "'"):
                #each += "'"
            #print(each, len(each))
            each = each[1:len(each)-1]
            #print(each)
            kset = trie.keys(each)
            found = False            
            if (each in kset):
                #print('rtrtr')
                #print(each)
                maximum = 0
                for i in range(0, len(kset)):
                    #print(kset[i], trie[kset[i]])
                    if (int(trie[kset[i]]) > maximum):
                        #print(int(trie[kset[i]]))
                        maximum = int(trie[kset[i]])
                        index = i
                train_result1.append(str(item_id) + ':'+ kset[index])
                found = True
                break				
            elif (each not in kset and found_in_elif == False):
                for item in company_post:
                    every = each				
                    every += ' '
                    every += item
                    #print(every)
                    if (every in kset):
                        #print('rtrtr')
                        #print(every)
                        maximum = 0
                        for i in range(0, len(kset)):
                        #print(kset[i], trie[kset[i]])
                            if (int(trie[kset[i]]) > maximum):
                                #print(int(trie[kset[i]]))
                                maximum = int(trie[kset[i]])
                                index = i
                        train_result1.append(str(item_id) + ':'+ kset[index])
                        found = True
                        found_in_elif = True
                        break					
            if (found == False):
                j += 1			                
        if (j == len(item_main)):
            train_result1.append(str(item_id) + ':' + 'Null')
#print(train_result1)				
z.close()

train_result2 = []
# trie is case sensitive, first make this part working as fine
# use tmp file for test, example 20
with open('two_word_training_data.txt', 'r') as z:
    lines = z.readlines()
    for line in lines:
        items = line.split(':')
        item_id = items[0]
        #print(items[1])
        item_tmp = items[1][items[1].find('[')+1 : items[1].find(']')]
        #print(item_tmp)
        item_main = item_tmp.split(',')
        #print(len(item_main))
        j = 0
        for each in item_main:
            each = each.lower()
            #print(each, len(each))
            each = each[1:len(each)-1]
            #print(each)
            kset = trie.keys(each)
            #print(kset)
            found_exact_match = False
            if (each in kset):
                #print('fssdf')
                for i in range(0, len(kset)):
                    if (each == kset[i]):
                        train_result2.append(str(item_id) + ':'+ kset[i])
                        found_exact_match = True
                        break						
                if (found_exact_match != True):
                    maximum = 0
                    for i in range(0, len(kset)):
                        #print(kset[i], trie[kset[i]])
                        if (int(trie[kset[i]]) > maximum):
                            #print(int(trie[kset[i]]))
                            maximum = int(trie[kset[i]])
                            index = i
                    train_result2.append(str(item_id) + ':'+ kset[index])
                    found += 1
                    break
            else:
                j += 1
        if (j == len(item_main)):
            train_result2.append(str(item_id) + ':' + 'Null')
#print(train_result2)				
z.close()

train_result3 = []
with open('three_word_training_data.txt', 'r') as z:
    lines = z.readlines()
    for line in lines:
        items = line.split(':')
        item_id = items[0]
        #print(items[1])
        item_tmp = items[1][items[1].find('[')+1 : items[1].find(']')]
        #print(item_tmp)
        item_main = item_tmp.split(',')
        #print(len(item_main))
        j = 0
        for each in item_main:
            each = each.lower()
            #print(each, len(each))
            each = each[1:len(each)-1]
            #print(each)
            kset = trie.keys(each)
            #print(kset)
            if (each in kset):
                #print(kset)
                maximum = 0
                for i in range(0, len(kset)):
                    #print(kset[i], trie[kset[i]])
                    if (int(trie[kset[i]]) > maximum):
                        #print(int(trie[kset[i]]))
                        maximum = int(trie[kset[i]])
                        index = i
                train_result3.append(str(item_id) + ':'+ kset[index])
                found += 1
                break
            else:
                j += 1
        if (j == len(item_main)):
            train_result3.append(str(item_id) + ':' + 'Null')
z.close()
#print(train_result3)

# summarizing the dict
dict = []
num = 240
num_list = []
with open('training_set.txt', 'r') as f:
    for line in f:  
        items = line.split(':')
        item_id = items[0]
        num_list.append(int(item_id))
#print(num_list)
f.close()

len1 = len(train_result1)
#print(len1)
len2 = len(train_result2)
len3 = len(train_result3)
num_cover_list = []
for each in train_result1:
    #print(each)
    items = each.split(':')
    item1_id = items[0]
    #print(item_id)
    item1_content = items[1]
    num_cover_list.append(int(item1_id))
    dict.append(each)
#print(dict)
#print(num_cover_list)

for each in train_result2:
    items = each.split(':')
    item2_id = items[0]
    item2_content = items[1]
    if (int(item2_id) in num_cover_list):
        index = num_cover_list.index(int(item2_id))
        comp1 = dict[index]
        comp1_item = comp1.split(':')
        length1 = len(comp1_item[1].split(' '))
        length2 = len(item2_content.split(' '))
        if (comp1_item[1] == 'Null' and item2_content != 'Null'):
            dict[index] = each
        if (comp1_item[1] != 'Null' and item2_content == 'Null'):
            pass
        if (comp1_item[1] != 'Null' and item2_content != 'Null'):
            #print(comp1_item[1], item2_content)
            #print(length1, length2)
            if (length1 == 1 and length2 == 1):
                pass
            if (length1 == 2 and length2 == 2):
                dict[index] = each
            if (length1 == 1 and length2 == 2):
                freq1 = trie[comp1_item[1]]
                freq2 = trie[item2_content]
                #print(freq1,freq2)
                if (freq1 >= freq2):
                    #print('sda')
                    pass
                if (freq1 < freq2):
                    #print('rtr')
                    dict[index] = each				
    if (int(item2_id) not in num_cover_list):
        num_cover_list.append(int(item2_id))
        dict.append(each)
#print(dict)
#print(num_cover_list)
    
for each in train_result3:
    items = each.split(':')
    item3_id = items[0]
    item3_content = items[1]
    if (int(item3_id) in num_cover_list):
        index = num_cover_list.index(int(item3_id))
        comp1 = dict[index]
        comp1_item = comp1.split(':')
        length1 = len(comp1_item[1].split(' '))
        length2 = len(item3_content.split(' '))
        if (comp1_item[1] == 'Null' and item3_content != 'Null'):
            dict[index] = each
        if (comp1_item[1] != 'Null' and item3_content == 'Null'):
            pass
        if (comp1_item[1] != 'Null' and item3_content != 'Null'):
            #print(comp1_item[1], item3_content)
            #print(length1, length2)
            if (length1 == length2 and length1 < 3):
                pass
            if (length1 == length2 and length1 >= 3):
                dict[index] = each
            if (length1 != length2):
                freq1 = trie[comp1_item[1]]
                freq2 = trie[item3_content]
                #print(freq1, freq2)
                if (freq1 >= freq2):
                    pass
                if (freq1 < freq2):
                    dict[index] = each				
    if (int(item3_id) not in num_cover_list):
        num_cover_list.append(int(item3_id))
        dict.append(each)
#print(dict)
#print(num_cover_list)  
 
num_null_list = list(set(num_list) - set(num_cover_list)) 
#print(num_null_list)
for each in num_null_list:
    item = str(each) + ':' + 'Null'
    dict.append(item)
    num_cover_list.append(each)
num_null_list = list(set(num_list) - set(num_cover_list)) 

#print(dict)
#print(num_null_list)
#print(num_cover_list)
dict_final = []
for i in num_list:
    for each in dict:
        each_id = each.split(':')[0]
        if (int(each_id) == i):
            dict_final.append(each)
#print(dict_final)    

m = open('Method2_result_v3_training_result.txt','w')
for each in dict_final:
    print(each, file = m)
m.close()

f.close()
