import re
import random
import json
from py_stringmatching import simfunctions, tokenizers
import string_process4
from sklearn.preprocessing import Imputer
import numpy as np
import pint
import ParseUnit
import UnitCheck
import UnitExtraction
import SpecialExtraction
import NumberExtraction
import JsonLongDescription
import Compare
with open('Y_missing_after_ID_extraction.txt', 'r') as f:
#with open('100Sampling.txt', 'r') as f:
    for i, l in enumerate(f):
        pass
f.close()
print(i + 1)
matrix = [['null' for j in range(7)] for j in range (2*(i+1))]
result = ['null' for j in range(i+1)]
feature_attr = ['product name','product long description','product short description','assembled product width', 'assembled product height', 'assembled product length']
freq_word = ['is','you','the','be','to','of','and','a','in','that','have','as','it','for','on','with','do','at','this','by','from','or','an','one','all','over','will','would','so','up','out','if','about','get','who','which','go','can','just','into']
freq_unit = ['foot','volt','gigabyte','megabyte','watt','megahertz','gigahertz','inch','meter','terabyte','gram','ampere','hour','millimeter','minute','liter']
freq_color = ['white','silver','gray','black','red','maroon','yellow','olive','lime','green','aqua','teal','blue','navy','purple','multicolor','fuchsia']
id_list = []
with open('Y_missing_after_ID_extraction.txt','r') as f:
#with open('100Sampling.txt','r') as f:
    lines = f.readlines()
    r = 0
    m = 0
    for i in lines:
        dict_tmp1 = {}
        dict_tmp2 = {}
        items = i.split('?')
        id = items[0].split(':')
        id1 = id[0]
        #print(id1)
        id_list.append(id1)
        json_id1 = items[1]
        json_id2 = items[3]
        id1 = re.findall(r'[\d|]+', json_id1)
        id2 = re.findall(r'[\d|]+', json_id2)
        json_data1 = json.loads(items[2])
        for each in json_data1.keys():
            aname = each
            bname = json_data1.get(aname) 
            cname = ''.join(bname)
            if aname.lower() in feature_attr:
                attrPost = feature_attr.index(aname.lower())
                dict_tmp1.setdefault(aname.lower(), cname.lower())
        for each in feature_attr:
            if each not in dict_tmp1.keys():
                dict_tmp1.setdefault(each, '')			
        matrix[r][0] = id1
        matrix[r][1] = dict_tmp1.get('product name')
        matrix[r][2] = dict_tmp1.get('product long description')
        matrix[r][3] = dict_tmp1.get('product short description')
        matrix[r][4] = dict_tmp1.get('assembled product width')
        matrix[r][5] = dict_tmp1.get('assembled product height')
        matrix[r][6] = dict_tmp1.get('assembled product length')
        if matrix[r][2] == None:
            matrix[r][2] = 'null'
        if matrix[r][3] == None:
            matrix[r][3] = 'null'

		# for product 2
        json_data2 = json.loads(items[4])
        for each in json_data2.keys():
            aname = each
            bname = json_data2.get(aname) 
            cname = ''.join(bname)
            if aname.lower() in feature_attr:
                attrPost = feature_attr.index(aname.lower())
                dict_tmp2.setdefault(aname.lower(), cname.lower())
        for each in feature_attr:
            if each not in dict_tmp2.keys():
                dict_tmp2.setdefault(each, '')
        matrix[r+1][0] = id2
        matrix[r+1][1] = dict_tmp2.get('product name')
        matrix[r+1][2] = dict_tmp2.get('product long description')
        matrix[r+1][3] = dict_tmp2.get('product short description')
        matrix[r+1][4] = dict_tmp2.get('assembled product width')
        matrix[r+1][5] = dict_tmp2.get('assembled product height')
        matrix[r+1][6] = dict_tmp2.get('assembled product length')
        if matrix[r+1][2] == None:
            matrix[r+1][2] = 'null'       
        if matrix[r+1][3] == None:
            matrix[r+1][3] = 'null'           

        result[m] = items[5]
        r += 2
        m += 1		
#print(matrix[1])
#print(result)
f.close()

i = int(len(matrix)/2-1)
FVmatrix = [[999 for j in range(2)] for j in range(i+1)]    
r = 0
missing1_all = 0
missing2_all = 0
nonempty = 0
label = 0
p = 0
q = 0
t1 = 0
t2 = 0
t3 = 0
dimen_list = ['height','width','length','depth']
for r in range(i+1):
	# this is for the long descriptions	
    product_long1 = string_process4.string_process4(matrix[2*r][2])
    product_long1 = tokenizers.whitespace(product_long1)	
    for each in product_long1:
        if each in freq_word:
            index = product_long1.index(each)
            product_long1[index] = ''
    while '' in product_long1:
        product_long1.remove('')

    product_long2 = string_process4.string_process4(matrix[2*r+1][2])
    product_long2 = tokenizers.whitespace(product_long2)		
    for each in product_long2:
        if each in freq_word:
            index = product_long2.index(each)
            product_long2[index] = ''
    while '' in product_long2:
        product_long2.remove('')
	# take out json format from long
    product_long1_json = matrix[2*r][2]
    product1_long_json = JsonLongDescription.JsonLongDescription(product_long1_json)
    product_long2_json = matrix[2*r+1][2]
    product2_long_json = JsonLongDescription.JsonLongDescription(product_long2_json)
    #print('Product 1 json in long :' + str(product1_long_json))
    #print('Product 2 json in long :' + str(product2_long_json))
    # take out height, length, width and depth in the json
    product1_long_json = str(product1_long_json)
    long1_json_token = product1_long_json.split(',')
    product2_long_json = str(product2_long_json)
    long2_json_token = product2_long_json.split(',')
    product1_json_token_result = []
    for each in long1_json_token:
        for every in dimen_list:
            if every in each:
                each_split = each.split(':')
                each_value = each_split[1]
                number = re.findall(r'[\d|]+', each_value)
                number = ''.join(number)
                product1_json_token_result.append(number)
    #print(product1_json_token_result)
    product2_json_token_result = []
    for each in long2_json_token:
        for every in dimen_list:
            if every in each:
                each_split = each.split(':')
                each_value = each_split[1]
                number = re.findall(r'[\d|]+', each_value)
                number = ''.join(number)
                product2_json_token_result.append(number)
    #print(product2_json_token_result)
    # take out the number part
    product_long1_number = NumberExtraction.NumberExtraction(product_long1)
    product_long1_number = list(set(product_long1_number))
    product_long2_number = NumberExtraction.NumberExtraction(product_long2)
    product_long2_number = list(set(product_long2_number))
    #print('Product 1 number in long description :' + str(product_long1_number))
    #print('Product 2 number in long description :' + str(product_long2_number))

    # take the dimension in the storage and put it here
    product1_width = matrix[2*r][4]
    product1_height = matrix[2*r][5]
    product1_length = matrix[2*r][6]
    product2_width = matrix[2*r+1][4]
    product2_height = matrix[2*r+1][5]
    product2_length = matrix[2*r+1][6]
    prod1_set = [product1_width, product1_height, product1_length]
    prod2_set = [product2_width, product2_height, product2_length]	
    # judge how many times none or three appears
    if product1_width == '' and product1_length == '' and product1_height == '':
        missing1_all += 1
    if product2_width == '' and product2_length == '' and product2_height == '':
        missing2_all += 1
    #print(prod1_set, prod2_set)
    if prod1_set != ['','',''] and prod2_set != ['','','']:
        nonempty += 1
        if set(prod1_set) == set(prod2_set): 
            label += 1
            FVmatrix[r][0] = 1			
            if result[r] == 'MATCH\n':
                p += 1
        else:
            FVmatrix[r][0] = 0
            if (result[r] == 'MISMATCH\n'):
                p += 1
    elif(prod1_set != ['','',''] and prod2_set == ['','','']): 
        if (set(prod1_set) - {''}) <= (set(product2_json_token_result) - {''}):
            FVmatrix[r][0] = 1
            q += 1
    elif(prod2_set != ['','',''] and prod1_set == ['','','']):
        if (set(prod2_set) - {''}) <= (set(product1_json_token_result) - {''}):
            FVmatrix[r][0] = 1
            q += 1			
    elif(len(set(product1_json_token_result) - {''}) != 0 and len(set(product2_json_token_result) - {''}) != 0):
        t1 += 1	
        tmp1 = set(product1_json_token_result) - {''}
        tmp2 = set(product2_json_token_result) - {''}
        #print(tmp1, tmp2)
        if tmp1 <= tmp2 or tmp2 <= tmp1:
            FVmatrix[r][0] = 1
            if (result[r] == 'MATCH\n'):
                t2 += 1
        else:
            FVmatrix[r][0] = 0
            if (result[r] == 'MISMATCH\n'):
                t3 += 1
    else:
        FVmatrix[r][0] = 999
z = 0
for each in FVmatrix:
    if each[0] != 999:
        z += 1
#print(z)		
#print(FVmatrix)
print(nonempty, p, q, t1, t2, t3)

with open('Y_missing_after_ID_extraction.txt', 'r') as f:
    r = 0
    a = open('Y_missing_after_dimension_extraction.txt','w')
    b = open('Y_obtained_after_dimension_extraction.txt','w')
    lines = f.readlines()
    for i in lines:
        if FVmatrix[r][0] != 999:
            if FVmatrix[r][0] == 1:
                print(id_list[r] + ', MATCH\n', end = '', file = b)
            if FVmatrix[r][0] == 0:
                print(id_list[r] + ', MISMATCH\n', end = '', file = b)
        else:
            print(i, end = '', file = a)
        r += 1
    a.close()
    b.close()	
f.close()
i = 0
with open('Y_missing_after_dimension_extraction.txt', 'r') as f:
    for i, l in enumerate(f):
        pass
f.close()
print(i + 1)
original = []
with open('predictions_Y_after_ID.txt', 'r') as f:
    lines_target = f.readlines()
    for each in lines_target:
        original.append(each)
    with open('Y_obtained_after_dimension_extraction.txt', 'r') as g:
        lines_origin = g.readlines()
        for i in lines_origin:
            items = i.split(',')
            number = items[0]
            value = items[1]
            target = number + ', MATCH\n'
            #print(i)
            original[int(number)-1] = i
    #print(original)	
f.close()	
with open('predictions_Y_after_dimension.txt', 'w') as f:
    for each in original:
        print(each, end = '', file = f)	
f.close()




