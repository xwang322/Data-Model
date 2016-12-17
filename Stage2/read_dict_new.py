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

#keysbyfrefix is feasible
print("Griffin example =========:)================") 
#say we want all the keys containing Griffin, we will do the following step
#kset contains all keys containing "Griffin",there are two of them in dict, Griffin Technology and Griffin's
kset = trie.keys("Griffin")
print (kset)
#both brands prefixed by Griffin can be found in kset
print ("Griffin Technology" in kset)
print ("Griffin's" in kset)

print ("\n Fractal example ========:)================")
kset = trie.keys("Fractal")
print (kset)
#only one brand contains Fractal is included in the dict, which is Fractal Design.
# Thus Fractal Design can be found in kset but not Fractal
print ("Fractal Design" in kset)
print ("Fractal" in kset)
# print its frequency
#print trie["Griffin"]

f.close()
