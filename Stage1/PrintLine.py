import re

with open('one_product_test_stage1.txt','r') as f:
    for line in f:
        print(line)
    items = line.split('?')
    for x in items:
        print(x)
    json1 = items[2].replace('{', '')
    json1 = json1.replace('}', '')
    details1 = json1.split(',')
    for y in details1:
        print(y) 
    json2 = items[4].replace('{', '')
    json2 = json2.replace('}', '')
    details2 = json2.split(',')
    for x in details2:
        print(x)    
f.closed 