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
with open('training_set.txt', 'r') as z:
    lines = z.readlines()
    for line in lines:
        items = line.split(':')
        item_id = items[0]
        items[1] = items[1].lower()
        item_main = re.split(r'\s+', items[1].strip())
        for each in item_main:
            #print(each)
            kset = trie.keys(each)
            #print(each in kset)
            if (kset):
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
#print(found)

m = open('Method1.result_revised.txt','w')
for each in train_result:
    print(each, file = m)
m.close()

f.close()