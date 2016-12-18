import re
import random
import json
from random import choice, sample, randint
from py_stringmatching import simfunctions, tokenizers
import string_process3
from sklearn.preprocessing import Imputer
import numpy as np
import Dict_lookup

feature_attr = ['id','product type','product name','product segment','brand','category','product long description']
#with open('Y.txt','r') as f:
with open('5000Test.txt','r') as f:
    for i,l in enumerate(f):
        pass
f.close()
#print(i)
matrix = [['null' for j in range(7)] for j in range (2*(i+1))]
result = ['null' for j in range(i+1)]
l = 0
#with open('Y.txt','r') as f: 
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
        matrix[r][6] = dict_tmp1.get('product long description')
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
        matrix[r+1][6] = dict_tmp2.get('product long description')
        result[m] = items[5]
        r += 2
        m += 1		
#print(matrix)
#print(result)		
f.close()

#x = open('Y_matrix.txt','w')
'''
x = open('5000Test_matrix.txt','w')
for each in matrix:
    print(each, file = x)
x.close()
#x = open('Y_matrix_class.txt','w')
x = open('5000Test_matrix_class.txt','w')
for each in result:
    print(each, file = x)
x.close()
'''
i = int(len(matrix)/2-1)
#print(i)
FVmatrix = [[0 for j in range(25)] for j in range(i+1)]    
r = 0
for r in range(i+1):
    product_type1 = string_process3.string_process3(matrix[2*r][1])
    product_type2 = string_process3.string_process3(matrix[2*r+1][1])
    # product type: jaro_winkler distance
    FVmatrix[r][0] = simfunctions.jaro_winkler(matrix[2*r][1], matrix[2*r+1][1])		       
    # product type: jaccard distance
    FVmatrix[r][1] = simfunctions.jaccard(set(product_type1), set(product_type2))
    # product type: soft_tfidf distance
    FVmatrix[r][2] = simfunctions.soft_tfidf(set(product_type1), set(product_type2))
    #product type: overlap_coefficient score	
    FVmatrix[r][3] = simfunctions.overlap_coefficient(set(product_type1), set(product_type2))
    #product type: cosine score	
    FVmatrix[r][4] = simfunctions.cosine(set(product_type1), set(product_type2))
	
    product_name1 = string_process3.string_process3(matrix[2*r][2])
    product_name2 = string_process3.string_process3(matrix[2*r+1][2])		
    # product name: jaro_winkler distance	
    FVmatrix[r][5] = simfunctions.jaro_winkler(matrix[2*r][2], matrix[2*r+1][2])
    #product name: jaccard score	
    FVmatrix[r][6] = simfunctions.jaccard(set(product_name1), set(product_name2)) 
    #product name: soft_tfidf score	
    FVmatrix[r][7] = simfunctions.soft_tfidf(set(product_name1), set(product_name2))
    #product name: overlap_coefficient score	
    FVmatrix[r][8] = simfunctions.overlap_coefficient(set(product_name1), set(product_name2))
    #product name: cosine score	
    FVmatrix[r][9] = simfunctions.cosine(set(product_name1), set(product_name2))
	
    product_seg1 = string_process3.string_process3(matrix[2*r][3])
    product_seg2 = string_process3.string_process3(matrix[2*r+1][3])	
	#product segment: jaro_winkler distance
    FVmatrix[r][10] = simfunctions.jaro_winkler(matrix[2*r][3], matrix[2*r+1][3]) 
	#product segment: jaccard distance
    FVmatrix[r][11] = simfunctions.jaccard(set(product_seg1), set(product_seg2)) 
	#product segment: soft_tfidf distance
    FVmatrix[r][12] = simfunctions.soft_tfidf(set(product_seg1), set(product_seg2)) 
    #product segment: overlap_coefficient score	
    FVmatrix[r][13] = simfunctions.overlap_coefficient(set(product_seg1), set(product_seg2))
    #product segment: cosine score	
    FVmatrix[r][14] = simfunctions.cosine(set(product_seg1), set(product_seg2)) 
 
    #brand: first tell whether it is missing, process then work
    if(matrix[2*r][4] == ''):
        matrix[2*r][4] = Dict_lookup.brand_extractor(matrix[2*r][2])
    if(matrix[2*r+1][4] == ''):
        matrix[2*r+1][4] = Dict_lookup.brand_extractor(matrix[2*r+1][2])
    #print(matrix[2*r][4], matrix[2*r+1][4])
    product_brand1 = string_process3.string_process3(matrix[2*r][4])
    product_brand2 = string_process3.string_process3(matrix[2*r+1][4])			
	#brand: soft_tfidf distance	
    FVmatrix[r][15] = simfunctions.soft_tfidf(set(product_brand1), set(product_brand2)) 		
	#brand: jaro_winkler distance	
    FVmatrix[r][16] = simfunctions.jaro_winkler(matrix[2*r][4], matrix[2*r+1][4]) 
	#brand: jaccard distance	
    FVmatrix[r][17] = simfunctions.jaccard(set(product_brand1), set(product_brand2)) 
	#brand: overlap_coefficient distance	
    FVmatrix[r][18] = simfunctions.overlap_coefficient(set(product_brand1), set(product_brand2))
	#brand: cosine distance	
    FVmatrix[r][19] = simfunctions.cosine(set(product_brand1), set(product_brand2))
	
    product_long1 = string_process3.string_process3(matrix[2*r][6])
    product_long2 = string_process3.string_process3(matrix[2*r+1][6])
    # long: jaccard distance
    FVmatrix[r][20] = simfunctions.jaccard(set(product_long1), set(product_long2))
    # long: overlap_coefficient distance
    FVmatrix[r][21] = simfunctions.overlap_coefficient(set(product_long1), set(product_long2))
    # long: cosine distance
    FVmatrix[r][22] = simfunctions.cosine(set(product_long1), set(product_long2))
    # long: soft_tfidf distance
    FVmatrix[r][23] = simfunctions.soft_tfidf(set(product_long1), set(product_long2))
		
    if(result[r] == 'MATCH\n'):
        FVmatrix[r][24] = 1
    else: 
        FVmatrix[r][24] = 0	
#print(FVmatrix)

#x = open('Y_feature_vector.txt','w')
x = open('5000Test29_string_processed_feature_vector.txt','w')
for each in FVmatrix:
    print(each, file = x)
x.close()






