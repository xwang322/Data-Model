from trie import Trie

# initialize a trie
trie = Trie()

with open('elec_brand_dic.txt', 'r') as f:
    lines = f.readlines()
    for each in lines:
        items = each.split("\t")
        # add item[0] as the key and [1] as the frequency in trie
        trie[items[0]] = items[1]
        #print items[0] +";" +items[1]

# search if PrintGreenToner.com is in trie
# kset contains all keys containing PrintGreenToner.com		
kset = trie.keys('griffin')
print(kset)
print("Griffin's" in kset) 
# print its frequency
print(trie["Griffin's"])
f.close()

