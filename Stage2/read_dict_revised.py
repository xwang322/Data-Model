from trie import Trie

# initialize a trie
trie = Trie()
with open('elec_brand_dic_revised.txt', 'r') as f:
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
        #print(items[0] +";" +items[1])
kset = trie.keys('sonnet')
print(kset)
print("sonnet" in kset) 
# print its frequency
print(trie["grace digital"])
print(trie["mario bros."])
f.close()
