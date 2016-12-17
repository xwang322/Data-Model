import re
from trie import Trie

# initialize a trie
trie = Trie()
with open('elec_brand_dic_revised.txt', 'r') as f:
    lines = f.readlines()
    for each in lines:
        items = each.split(' ')
        tmp = ''
        for i in range(0, len(items)-1):
            tmp += items[i]
        tmp.strip()
        tmp = tmp.lower()
        value = items[len(items)-1]
        #print(tmp, value)
		# add item[0] as the key and [1] as the frequency in trie
        trie[tmp] = value
        #print(items[0] +";" +items[1])
train_result = []
found = 0

# not sure for method2, do we need for one single word find all kset related and return the maximum freq or extend the search range to all related kset
# also consider the missing tuple and duplicate tuple issues, discuss with others.
with open('one_word_training_data.txt', 'r') as z:
    lines = z.readlines()
    for line in lines:
        items = line.split(':')
        item_id = items[0]
        #print(items[1])
        pattern = re.compile("'(.*?)'")
        item_main = pattern.findall(items[1])
        for each in item_main:
            each = each.lower()
            kset = trie.keys(each)
            #print(kset)
            #print(each)
            if (each in kset):
                #print(kset)
                maximum = 0
                for i in range(0, len(kset)):
                    #print(kset[i], trie[kset[i]])
                    if (int(trie[kset[i]]) > maximum):
                        #print(int(trie[kset[i]]))
                        maximum = int(trie[kset[i]])
                        index = i
                train_result.append(str(item_id) + ':'+ kset[index])
                found += 1
                break
            else:
                i += 1
        if (i == len(item_main)):
            train_result.append(str(item_id) + ':' + 'Null')
#print(train_result)				
z.close()

m = open('Method2_result_one_revised.txt','w')
for each in train_result:
    print(each, file = m)
m.close()

with open('two_word_training_data.txt', 'r') as z:
    lines = z.readlines()
    for line in lines:
        items = line.split(':')
        item_id = items[0]
        #print(items[1])
        pattern = re.compile("'(.*?)'")
        item_main = pattern.findall(items[1])
        for each in item_main:
            each = each.lower()
            kset = trie.keys(each)
            #print(kset)
            #print(each)
            if (each in kset):
                #print(kset)
                maximum = 0
                for i in range(0, len(kset)):
                    #print(kset[i], trie[kset[i]])
                    if (int(trie[kset[i]]) > maximum):
                        #print(int(trie[kset[i]]))
                        maximum = int(trie[kset[i]])
                        index = i
                train_result.append(str(item_id) + ':'+ kset[index])
                found += 1
                break
            else:
                i += 1
        if (i == len(item_main)):
            train_result.append(str(item_id) + ':' + 'Null')
#print(train_result)				
z.close()

m = open('Method2_result_two_revised.txt','w')
for each in train_result:
    print(each, file = m)
m.close()

with open('three_word_training_data.txt', 'r') as z:
    lines = z.readlines()
    for line in lines:
        items = line.split(':')
        item_id = items[0]
        #print(items[1])
        pattern = re.compile("'(.*?)'")
        item_main = pattern.findall(items[1])
        for each in item_main:
            each = each.lower()
            kset = trie.keys(each)
            #print(kset)
            #print(each)
            if (each in kset):
                #print(kset)
                maximum = 0
                for i in range(0, len(kset)):
                    #print(kset[i], trie[kset[i]])
                    if (int(trie[kset[i]]) > maximum):
                        #print(int(trie[kset[i]]))
                        maximum = int(trie[kset[i]])
                        index = i
                train_result.append(str(item_id) + ':'+ kset[index])
                found += 1
                break
            else:
                i += 1
        if (i == len(item_main)):
            train_result.append(str(item_id) + ':' + 'Null')
z.close()
#print(train_result)
				
m = open('Method2_result_three_revised.txt','w')
for each in train_result:
    print(each, file = m)
m.close()

f.close()
