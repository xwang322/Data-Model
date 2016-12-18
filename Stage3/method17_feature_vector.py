import re
import random
import json
from random import choice, sample, randint
from py_stringmatching import simfunctions, tokenizers
import string_process2
from sklearn.preprocessing import Imputer
import numpy as np

feature_attr = ['id','product type','product name','product segment','brand','category']
#with open('X.txt','r') as f:
with open('5000Test.txt','r') as f:
    for i,l in enumerate(f):
        pass
f.close()
#print(i)
matrix = [['null' for j in range(6)] for j in range (2*(i+1))]
result = ['null' for j in range(i+1)]
#with open('X.txt','r') as f: 
l = 0
with open('5000Test.txt','r') as f:
    lines = f.readlines()
    r = 0
    m = 0
    for i in lines:
        dict_tmp1 = {}
        dict_tmp2 = {}
        items = i.split('?')
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
        matrix[r][1] = dict_tmp1.get('product type')
        matrix[r][2] = dict_tmp1.get('product name')
        matrix[r][3] = dict_tmp1.get('product segment')
        matrix[r][4] = dict_tmp1.get('brand')
        matrix[r][5] = dict_tmp1.get('category')
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
        matrix[r+1][1] = dict_tmp2.get('product type')
        matrix[r+1][2] = dict_tmp2.get('product name')
        matrix[r+1][3] = dict_tmp2.get('product segment')
        matrix[r+1][4] = dict_tmp2.get('brand')
        matrix[r+1][5] = dict_tmp2.get('category')
        result[m] = items[5]
        r += 2
        m += 1		
#print(len(matrix))
#print(result)		
f.close()

#x = open('X_matrix.txt','w')
x = open('5000Test_matrix.txt','w')
for each in matrix:
    print(each, file = x)
x.close()
#x = open('X_matrix_class.txt','w')
x = open('5000Test_matrix_class.txt','w')
for each in result:
    print(each, file = x)
x.close()

i = int(len(matrix)/2-1)
#print(i)
FVmatrix = [[0 for j in range(10)] for j in range(i+1)]    
r = 0
for r in range(i+1):
    product_type1 = string_process2.string_process2(matrix[2*r][1])
    product_type2 = string_process2.string_process2(matrix[2*r+1][1])
    # product type: jaro_winkler distance
    if(matrix[2*r][1] == '' and matrix[2*r+1][1] == ''):
        FVmatrix[r][0] = 999
    else:
        FVmatrix[r][0] = simfunctions.jaro_winkler(matrix[2*r][1], matrix[2*r+1][1])		       
    # product type: jaccard distance
    if(matrix[2*r][1] == '' and matrix[2*r+1][1] == ''):
        FVmatrix[r][1] = 999
    else:
        FVmatrix[r][1] = simfunctions.jaccard(set(product_type1), set(product_type2))
    # product type: third one is uncertain
    if(len(matrix[2*r][1]) == len(matrix[2*r+1][1])):
        FVmatrix[r][2] = simfunctions.hamming_distance(matrix[2*r][1], matrix[2*r+1][1])
    else:
        FVmatrix[r][2] = simfunctions.cosine(set(product_type1), set(product_type2))

    product_name1 = string_process2.string_process2(matrix[2*r][2])
    product_name2 = string_process2.string_process2(matrix[2*r+1][2])		
    # product name: jaro_winkler distance	
    if(matrix[2*r][2] == '' and matrix[2*r+1][2] == ''):
        FVmatrix[r][3] = 999
    else:
        FVmatrix[r][3] = simfunctions.jaro_winkler(matrix[2*r][2], matrix[2*r+1][2])
    #product name: jaccard score	
    FVmatrix[r][4] = simfunctions.jaccard(set(product_name1), set(product_name2)) 
    # product name: third one is uncertain
    if(len(matrix[2*r][2]) == len(matrix[2*r+1][2])):
        FVmatrix[r][5] = simfunctions.hamming_distance(matrix[2*r][2], matrix[2*r+1][2])
    else:
        FVmatrix[r][5] = simfunctions.cosine(set(product_name1), set(product_name2))
	
	#product segment: jaro_winkler distance
    if(matrix[2*r][3] == '' and matrix[2*r+1][3] == ''):
	    FVmatrix[r][6] = 999
    else:
	    FVmatrix[r][6] = simfunctions.jaro_winkler(matrix[2*r][3], matrix[2*r+1][3]) 
	#product segment: jaccard distance
    product_seg1 = string_process2.string_process2(matrix[2*r][3])
    product_seg2 = string_process2.string_process2(matrix[2*r+1][3])
    if(matrix[2*r][3] == '' and matrix[2*r+1][3] == ''):
	    FVmatrix[r][7] = 999
    else:
        FVmatrix[r][7] = simfunctions.jaccard(set(product_seg1), set(product_seg2)) 
    # product segment: third one is uncertain
    if(len(matrix[2*r][3]) == len(matrix[2*r+1][3])):
        FVmatrix[r][8] = simfunctions.hamming_distance(matrix[2*r][3], matrix[2*r+1][3])
    else:
        FVmatrix[r][8] = simfunctions.cosine(set(product_seg1), set(product_seg2))		
		
    if(result[r] == 'MATCH\n'):
        FVmatrix[r][9] = 1
    else: 
        FVmatrix[r][9] = 0	
#print(FVmatrix)

#x = open('X_feature_vector.txt','w')
x = open('5000Test17_string_processed_feature_vector.txt','w')
for each in FVmatrix:
    print(each, file = x)
x.close()






