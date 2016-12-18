import re

with open('elec_brand_dic.txt', 'r') as f:
    rev_list = []
    for line in f:
        line = line.strip()
        items = re.split(r'\s+', line)
        list_tmp = []
        for item in items:
            if (item.isdigit() != True):
                list_tmp.append(item)
        new_line = ' '.join(list_tmp)
        rev_list.append(new_line)
z = open('elec_brand_dic_null_freq.txt','w')
for each in rev_list:
    print(each, file = z)
z.close()		
f.close()

dict = {}
with open('elec_brand_dic.txt', 'r') as f:
    for line in f:
        line = line.strip()
        items = re.split(r'\s+', line)
        key = ''
        for index in range(0,len(items)-1):
            key += items[index]
            key += ' '
        key = key.strip()
        value = int(items[len(items)-1])
        dict.setdefault(key, value)      
f.close()

with open('elec_brand_dic_null_freq.txt','r') as f:
    r = 0
    for line in f:
        line = line.strip()
        items = re.split(r'\s+', line)
        if (len(items) > r):
            r = len(items)
    for i in range(1,r+1):
        locals()['list'+str(i)] = []
f.close()
 
with open('elec_brand_dic_null_freq.txt','r') as f:
    for line in f:
        line = line.strip()
        items = re.split(r'\s+', line)
        length = len(items)
        locals()['list'+str(length)].append(items)
f.close()    
'''
This part is to check whether spelling could introcude some same company in different positions
'''
list1_tmp = list1[:]
for each in list1:
    list1_tmp = list1[:]
    tmp = tuple(each)[0].lower()
    list1_tmp.remove(each)
    for every in list1_tmp:
        index = list1_tmp.index(every)
        if (tmp == tuple(list1_tmp[index])[0].lower()):
            a = dict.get(tuple(each)[0])
            b = dict.get(tuple(list1_tmp[index])[0])
            if (a >= b):
                dict.update({tuple(each)[0]: a+b})
                dict.pop(tuple(list1_tmp[index])[0])
                list1.remove(every)
            else:
                dict.update({tuple(list1_tmp[index]): a+b})
                dict.pop(tmp)
                list1.remove(each)
#print(list1)    
'''
This part is to delete brand name with 2 words and the second one is sth like "company" and match the first one.
In this case, they are exactly the same, so we should conbine their freq together
'''
#print(dict.keys())
company_post = ['technology','tech','technologies','company','corp','corp.','llc','inc','inc.','co.','co','ltd','ltd.']
for each in list1:
    for every in list2:
        if (str(each[0]).lower() == every[0].lower()):
            if (every[1].lower() in company_post):
                tmp = ''
                tmp += every[0]
                tmp += ' '
                tmp += every[1]
                a = dict.get(tuple(each)[0])
                b = dict.get(tmp)
                if (a >= b):
                    dict.update({tuple(each)[0]: a+b})
                    dict.pop(tmp)
                    list2.remove(every)
                else:
                    dict.update({tmp: a+b})
                    dict.pop(tuple(each)[0])
                    list1.remove(each)									
z = open('elec_brand_dic_revised_v2.txt','w')
for each in dict:
    print(each,'\t',dict.get(each), file = z)
z.close()          					
#print(dict)

			
        

