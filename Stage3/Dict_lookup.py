import re
from trie import Trie
def brand_extractor(line):
# initialize a trie
    trie = Trie()
    with open('elec_brand_dic_revised.txt', 'r') as f:
        lines = f.readlines()
        for each in lines:
            items = each.split(' \t ')
            tmp = ''
            for i in range(0, len(items)-1):
                tmp += items[i]
            tmp.strip()
            tmp = tmp.lower()
            value = items[len(items)-1]
            trie[tmp] = value
		
    item_main = re.split(r'\s+', line.strip())
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

    train_result1 = []
    found = 0
    company_post = ['technology','tech','technologies','company','corp','corp.','llc','inc','inc.','co.','co','ltd','ltd.']
    j = 0
    found_in_elif = False
    for each in set(item_one):
        #print(each)
        each = each.strip()
        each = each.lower()
        #print(each)
        kset = trie.keys(each)
        found = False            
        if (each in kset):
            maximum = 0
            for i in range(0, len(kset)):
                if (int(trie[kset[i]]) > maximum):
                    maximum = int(trie[kset[i]])
                    index = i
            train_result1.append(kset[index])
            found = True
            break				
        elif (each not in kset and found_in_elif == False):
            for item in company_post:
                every = each				
                every += ' '
                every += item
                if (every in kset):
                    maximum = 0
                    for i in range(0, len(kset)):
                        if (int(trie[kset[i]]) > maximum):
                            maximum = int(trie[kset[i]])
                            index = i
                    train_result1.append(kset[index])
                    found = True
                    found_in_elif = True
                    break					
        if (found == False):
            j += 1			                
    if (j == len(item_main)):
        train_result1.append('Null')
    #print(train_result1)
	
    train_result2 = []
    j = 0
    for each in set(item_two):
        each = each.lower()
        found_exact_match = False
        if (each in kset):
            for i in range(0, len(kset)):
                if (each == kset[i]):
                    train_result2.append(kset[i])
                    found_exact_match = True
                    break						
            if (found_exact_match != True):
                maximum = 0
                for i in range(0, len(kset)):
                    if (int(trie[kset[i]]) > maximum):
                        maximum = int(trie[kset[i]])
                        index = i
                train_result2.append(kset[index])
                found += 1
                break
        else:
            j += 1
    if (j == len(set(item_two))):
        train_result2.append('Null')
    #print(train_result2)				

    train_result3 = []
    j = 0
    for each in set(item_three):
        each = each.lower()
        kset = trie.keys(each)
        if (each in kset):
            maximum = 0
            for i in range(0, len(kset)):
                if (int(trie[kset[i]]) > maximum):
                    maximum = int(trie[kset[i]])
                    index = i
            train_result3.append(kset[index])
            found += 1
            break
        else:
            j += 1
    if (j == len(set(item_three))):
        train_result3.append('Null')
    #print(train_result3)

    max = 0
    return_str = ''
    for each in train_result1:
        if(each != 'Null'):
            tmp = trie[each]
            #print(tmp)
            if(int(tmp) > max):
                max = int(tmp)
                return_str = each
    for each in train_result2:
        if(each != 'Null'):
            tmp = trie[each]
            #print(tmp)
            if(int(tmp) > max):
                max = int(tmp)
                return_str = each
    for each in train_result3:
        if(each != 'Null'):
            tmp = trie[each]
            #print(tmp)
            if(int(tmp) > max):
                max = int(tmp)            
                return_str = each
    #print(return_str)
    return(return_str)	
a = 'Bello SW7408-8M Subwoofer Cable</li><li>'
b = "Enermax EMK5402 - Storage mobile rack - 5.25 to 4 x 2.5"
c = "Enermax EMK5201U3 - Storage mobile rack - 5.25 to 3.5 / 2.5"
d = 'Enermax'
e = 'NORTH BY HONEYWELL 40HE PAPR Cartridge, Magenta, PK 3'
f = "NORTH BY HONEYWELL 4003HE PAPR Cartridge Yellow/Magenta PK 3"
g = "HUBBELL WIRING DEVICE-KELLEMS 074093404 Strain Relief,Used with NPT 1 In"
h = "HUBBELL WIRING DEVICE-KELLEMS SHC2024CR Cable Connector 1/2 In Straight Black"
i = "ROMEX 63946823 Nonmetallic Cable 14/3 AWG White 100ft"
brand_extractor(i)