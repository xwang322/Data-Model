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
with open('5000Sampling.txt','r') as f:
    for i,l in enumerate(f):
        pass
f.close()
#print(i)
matrix = [['null' for j in range(7)] for j in range (2*(i+1))]
result = ['null' for j in range(i+1)]
l = 0
#with open('Y.txt','r') as f: 
with open('5000Sampling.txt','r') as f:
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
x = open('5000Sampling_matrix.txt','w')
for each in matrix:
    print(each, file = x)
x.close()
#x = open('Y_matrix_class.txt','w')
x = open('5000Sampling_matrix_class.txt','w')
for each in result:
    print(each, file = x)
x.close()
'''
i = int(len(matrix)/2-1)
#print(i)
FVmatrix = [[0 for j in range(21)] for j in range(i+1)]    
r = 0
for r in range(i+1):

    # product type: levenshtein distance
    if(matrix[2*r][1] == '' and matrix[2*r+1][1] == ''):
        FVmatrix[r][0] = 999
    else:
        FVmatrix[r][0] = simfunctions.levenshtein(matrix[2*r][1], matrix[2*r+1][1])			       
    # product type: needleman_wunsch distance
    if(matrix[2*r][1] == '' and matrix[2*r+1][1] == ''):
        FVmatrix[r][1] = 999
    else:
        FVmatrix[r][1] = simfunctions.needleman_wunsch(matrix[2*r][1], matrix[2*r+1][1])	
    # product type: smith_waterman distance
    if(matrix[2*r][1] == '' and matrix[2*r+1][1] == ''):
        FVmatrix[r][2] = 999
    else:
        FVmatrix[r][2] = simfunctions.smith_waterman(matrix[2*r][1], matrix[2*r+1][1])	
    # product type: affine distance
    if(matrix[2*r][1] == '' and matrix[2*r+1][1] == ''):
        FVmatrix[r][3] = 999
    else:
        FVmatrix[r][3] = simfunctions.affine(matrix[2*r][1], matrix[2*r+1][1])	

	
    # product name: levenshtein distance
    if(matrix[2*r][2] == '' and matrix[2*r+1][2] == ''):
        FVmatrix[r][4] = 999
    else:
        FVmatrix[r][4] = simfunctions.levenshtein(matrix[2*r][2], matrix[2*r+1][2])			       
    # product name: needleman_wunsch distance
    if(matrix[2*r][2] == '' and matrix[2*r+1][2] == ''):
        FVmatrix[r][5] = 999
    else:
        FVmatrix[r][5] = simfunctions.needleman_wunsch(matrix[2*r][2], matrix[2*r+1][2])	
    # product name: smith_waterman distance
    if(matrix[2*r][2] == '' and matrix[2*r+1][2] == ''):
        FVmatrix[r][6] = 999
    else:
        FVmatrix[r][6] = simfunctions.smith_waterman(matrix[2*r][2], matrix[2*r+1][2])	
    # product name: affine distance
    if(matrix[2*r][2] == '' and matrix[2*r+1][2] == ''):
        FVmatrix[r][7] = 999
    else:
        FVmatrix[r][7] = simfunctions.affine(matrix[2*r][2], matrix[2*r+1][2])	
	
	
    # product seg: levenshtein distance
    if(matrix[2*r][3] == '' and matrix[2*r+1][3] == ''):
        FVmatrix[r][8] = 999
    else:
        FVmatrix[r][8] = simfunctions.levenshtein(matrix[2*r][3], matrix[2*r+1][3])			       
    # product seg: needleman_wunsch distance
    if(matrix[2*r][3] == '' and matrix[2*r+1][3] == ''):
        FVmatrix[r][9] = 999
    else:
        FVmatrix[r][9] = simfunctions.needleman_wunsch(matrix[2*r][3], matrix[2*r+1][3])	
    # product seg: smith_waterman distance
    if(matrix[2*r][3] == '' and matrix[2*r+1][3] == ''):
        FVmatrix[r][10] = 999
    else:
        FVmatrix[r][10] = simfunctions.smith_waterman(matrix[2*r][3], matrix[2*r+1][3])	
    # product seg: affine distance
    if(matrix[2*r][3] == '' and matrix[2*r+1][3] == ''):
        FVmatrix[r][11] = 999
    else:
        FVmatrix[r][11] = simfunctions.affine(matrix[2*r][3], matrix[2*r+1][3])	

 
    #brand: first tell whether it is missing, process then work
    if(matrix[2*r][4] == ''):
        matrix[2*r][4] = Dict_lookup.brand_extractor(matrix[2*r][2])
    if(matrix[2*r+1][4] == ''):
        matrix[2*r+1][4] = Dict_lookup.brand_extractor(matrix[2*r+1][2])
    # product brand: levenshtein distance
    if(matrix[2*r][4] == '' and matrix[2*r+1][4] == ''):
        FVmatrix[r][12] = 999
    else:
        FVmatrix[r][12] = simfunctions.levenshtein(matrix[2*r][4], matrix[2*r+1][4])			       
    # product brand: needleman_wunsch distance
    if(matrix[2*r][4] == '' and matrix[2*r+1][4] == ''):
        FVmatrix[r][13] = 999
    else:
        FVmatrix[r][13] = simfunctions.needleman_wunsch(matrix[2*r][4], matrix[2*r+1][4])	
    # product brand: smith_waterman distance
    if(matrix[2*r][4] == '' and matrix[2*r+1][4] == ''):
        FVmatrix[r][14] = 999
    else:
        FVmatrix[r][14] = simfunctions.smith_waterman(matrix[2*r][4], matrix[2*r+1][4])	
    # product brand: affine distance
    if(matrix[2*r][4] == '' and matrix[2*r+1][4] == ''):
        FVmatrix[r][15] = 999
    else:
        FVmatrix[r][15] = simfunctions.affine(matrix[2*r][4], matrix[2*r+1][4])	

    product_long1 = string_process3.string_process3(matrix[2*r][6])
    product_long2 = string_process3.string_process3(matrix[2*r+1][6])
    # long: jaccard distance
    FVmatrix[r][16] = simfunctions.jaccard(set(product_long1), set(product_long2))
    # long: overlap_coefficient distance
    FVmatrix[r][17] = simfunctions.overlap_coefficient(set(product_long1), set(product_long2))
    # long: cosine distance
    FVmatrix[r][18] = simfunctions.cosine(set(product_long1), set(product_long2))
    # long: soft_tfidf distance
    FVmatrix[r][19] = simfunctions.soft_tfidf(set(product_long1), set(product_long2))

		
    if(result[r] == 'MATCH\n'):
        FVmatrix[r][20] = 1
    else: 
        FVmatrix[r][20] = 0	
#print(FVmatrix)

#x = open('Y_feature_vector.txt','w')
x = open('5000Sampling30_string_processed_feature_vector.txt','w')
for each in FVmatrix:
    print(each, file = x)
x.close()






