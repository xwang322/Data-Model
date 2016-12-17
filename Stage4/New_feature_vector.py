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

with open('X_missing.txt', 'r') as f:
    for i, l in enumerate(f):
        pass
f.close()
print(i + 1)
matrix = [['null' for j in range(8)] for j in range (2*(i+1))]
result = ['null' for j in range(i+1)]
feature_attr = ['product type','product name','product segment','brand','category','product long description','product long description']
freq_word = ['the','be','to','of','and','a','in','that','have','as','it','for','on','with','do','at','this','by','from','or','an','one','all','over','will','would','so','up','out','if','about','get','who','which','go','can','just','into']
freq_unit = ['foot','volt','gigabyte','megabyte','watt','megahertz','gigahertz','inch','meter','terabyte','gram','ampere','hour','millimeter','minute','liter']

with open('X_missing.txt','r') as f:
    lines = f.readlines()
    r = 0
    m = 0
    for i in lines:
        dict_tmp1 = {}
        dict_tmp2 = {}
        items = i.split('?')
        id = items[0].split(':')
        id1 = id[0]
        json_data1 = json.loads(items[2])
        for each in json_data1.keys():
            aname = each
            bname = json_data1.get(aname) 
            cname = ''.join(bname)
            if aname.lower() in feature_attr:
                if (aname.lower() == 'product name'):
                    attrPost = feature_attr.index(aname.lower())
                    dict_tmp1.setdefault(aname.lower(), cname)
                else:
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
        if matrix[r][6] == None:
            matrix[r][6] = ''
        matrix[r][7] = dict_tmp1.get('product short description')
        if matrix[r][7] == None:
            matrix[r][7] = ''
		# for product 2
        json_data2 = json.loads(items[4])
        for each in json_data2.keys():
            aname = each
            bname = json_data2.get(aname) 
            cname = ''.join(bname)
            if aname.lower() in feature_attr:
                if (aname.lower() == 'product name'):
                    attrPost = feature_attr.index(aname.lower())
                    dict_tmp2.setdefault(aname.lower(), cname)
                else:
                    attrPost = feature_attr.index(aname.lower())
                    dict_tmp2.setdefault(aname.lower(), cname.lower())
        for each in feature_attr:
            if each not in dict_tmp2.keys():
                dict_tmp2.setdefault(each, '')
        matrix[r+1][0] = id1
        matrix[r+1][1] = dict_tmp2.get('product type')
        matrix[r+1][2] = dict_tmp2.get('product name')
        matrix[r+1][3] = dict_tmp2.get('product segment')
        matrix[r+1][4] = dict_tmp2.get('brand')
        matrix[r+1][5] = dict_tmp2.get('category')
        matrix[r+1][6] = dict_tmp2.get('product long description')
        if matrix[r+1][6] == None:
            matrix[r+1][6] = ''
        matrix[r+1][7] = dict_tmp2.get('product short description')
        if matrix[r+1][7] == None:
            matrix[r+1][7] = ''
        result[m] = items[5]
        r += 2
        m += 1		
#print(matrix[0])
#print(result)    
f.close()
i = int(len(matrix)/2-1)
FVmatrix = [[0 for j in range(26)] for j in range(i+1)]    
r = 0
for r in range(i+1):
    # merge the type, segment, brand, category part
    # product type: levenshtein distance
    product1_comb = []
    product1_comb.append(matrix[2*r][1])
    product1_comb.append(matrix[2*r][3])
    product1_comb.append(matrix[2*r][4])
    product1_comb.append(matrix[2*r][5])		       

    product2_comb = []
    product2_comb.append(matrix[2*r+1][1])
    product2_comb.append(matrix[2*r+1][3])
    product2_comb.append(matrix[2*r+1][4])
    product2_comb.append(matrix[2*r+1][5])
    product_comb = []
    product_comb.append(product1_comb)
    product_comb.append(product2_comb)
    #print(product_comb)
    product1_comb_str = ' '.join(product_comb[0])
    product1_comb_str.strip()
    product1_comb_str = string_process4.string_process4(product1_comb_str)	
    product2_comb_str = ' '.join(product_comb[1])
    product2_comb_str.strip()
    product2_comb_str = string_process4.string_process4(product2_comb_str)
    product1_comb_list = tokenizers.whitespace(product1_comb_str)
    product2_comb_list = tokenizers.whitespace(product2_comb_str)	
    #print(product1_comb_list, product2_comb_list)

    # process the product name, take similar words from name by combination	
    # first is within each combination
    flag1 = 0
    product_name1 = string_process4.string_process4(matrix[2*r][2])
    product_name1 = tokenizers.whitespace(product_name1)
    product_name1_lower = []
    for each in product_name1:
        product_name1_lower.append(each.lower())
    product_name1_upper = []
    for each in product_name1:
        product_name1_upper.append(each.upper())
    for each in product_name1_lower:
        if each in product1_comb_list:
            flag1 = 1
            index = product_name1_lower.index(each)
            product_name1_lower[index] = ''
            product_name1[index] = ''
            product_name1_upper[index] = ''
    while '' in product_name1_lower:
        product_name1_lower.remove('')
    while '' in product_name1:
        product_name1.remove('')
    while '' in product_name1_upper:
        product_name1_upper.remove('')

    flag2 = 0		
    product_name2 = string_process4.string_process4(matrix[2*r+1][2])
    product_name2 = tokenizers.whitespace(product_name2)
    product_name2_lower = []
    for each in product_name2:
        product_name2_lower.append(each.lower())
    product_name2_upper = []
    for each in product_name2:
        product_name2_upper.append(each.upper())
    for each in product_name2_lower:
        if each in product2_comb_list:
            flag2 = 1
            index = product_name2_lower.index(each)
            product_name2_lower[index] = ''
            product_name2[index] = ''
            product_name2_upper[index] = ''
    while '' in product_name2_lower:
        product_name2_lower.remove('')
    while '' in product_name2:
        product_name2.remove('')
    while '' in product_name2_upper:
        product_name2_upper.remove('')

    # then cross list with the other combination
    flag3 = 0
    for each in product_name1_lower:
        if each in product2_comb_list:
            flag3 += 1
            index = product_name1_lower.index(each)
            product_name1_lower[index] = ''
            product_name1[index] = ''
            product_name1_upper[index] = ''
    while '' in product_name1_lower:
        product_name1_lower.remove('')
    while '' in product_name1:
        product_name1.remove('')
    while '' in product_name1_upper:
        product_name1_upper.remove('')

    flag4 = 0		
    for each in product_name2_lower:
        if each in product1_comb_list:
            flag4 += 1
            index = product_name2_lower.index(each)
            product_name2_lower[index] = ''
            product_name2[index] = ''
            product_name2_upper[index] = ''
    while '' in product_name2_lower:
        product_name2_lower.remove('')
    while '' in product_name2:
        product_name2.remove('')	
    while '' in product_name2_upper:
        product_name2_upper.remove('')	
		
    FVmatrix[r][0] = flag1
    FVmatrix[r][1] = flag2
    FVmatrix[r][2] = flag3
    FVmatrix[r][3] = flag4
    # clean the product name by frequency words
    for each in product_name1_lower:
        if each in freq_word:
            index = product_name1_lower.index(each)
            product_name1_lower[index] = ''
            product_name1[index] = ''
            product_name1_upper[index] = ''
    while '' in product_name1_lower:
        product_name1_lower.remove('')
    while '' in product_name1:
        product_name1.remove('')
    while '' in product_name1_upper:
        product_name1_upper.remove('')
		
    for each in product_name2_lower:
        if each in freq_word:
            index = product_name2_lower.index(each)
            product_name2_lower[index] = ''
            product_name2[index] = ''
            product_name2_upper[index] = ''
    while '' in product_name2_lower:
        product_name2_lower.remove('')
    while '' in product_name2:
        product_name2.remove('')
    while '' in product_name2_upper:
        product_name2_upper.remove('')
	
	# still for product name, just notify whether there is word from the other product long description
    # still not decided whether need to take away from there
    product_long1 = string_process4.string_process4(matrix[2*r][6])
    product_long2 = string_process4.string_process4(matrix[2*r+1][6])
    flag5 = 0
    for each in product_name1_lower:
        if each in product_long2:
            flag5 += 1
    flag6 = 0
    for each in product_name2_lower:
        if each in product_long1:
            flag6 += 1
    FVmatrix[r][4] = flag5
    FVmatrix[r][5] = flag6

	# still for product name, just notify whether there is word from the other product short description
	# still not decided whether need to take away from there
    product_short1 = string_process4.string_process4(matrix[2*r][7])
    product_short2 = string_process4.string_process4(matrix[2*r+1][7])
    flag7 = 0
    for each in product_name1_lower:
        if each in product_short2:
            flag7 += 1
    flag8 = 0
    for each in product_name2_lower:
        if each in product_short1:
            flag8 += 1
    FVmatrix[r][6] = flag7
    FVmatrix[r][7] = flag8

    # Parse out all number+unit
    product_unit1, product_unit1_index = ParseUnit.ParseUnit(product_name1)
    product_unit2, product_unit2_index = ParseUnit.ParseUnit(product_name2)
    product_unit1_lower, product_unit1_lower_index = ParseUnit.ParseUnit(product_name1_lower)
    product_unit2_lower, product_unit2_lower_index = ParseUnit.ParseUnit(product_name2_lower)
    product_unit1_upper, product_unit1_upper_index = ParseUnit.ParseUnit(product_name1_upper)
    product_unit2_upper, product_unit2_upper_index = ParseUnit.ParseUnit(product_name2_upper)
    # check if this is a good extraction, judge if it is within freq list
    product_unit1, product_unit1_index = UnitCheck.UnitCheck(product_unit1, product_unit1_index)
    product_unit2, product_unit2_index = UnitCheck.UnitCheck(product_unit2, product_unit2_index)
    product_unit1_lower, product_unit1_lower_index = UnitCheck.UnitCheck(product_unit1_lower, product_unit1_lower_index)
    product_unit2_lower, product_unit2_lower_index = UnitCheck.UnitCheck(product_unit2_lower, product_unit2_lower_index)
    product_unit1_upper, product_unit1_upper_index = UnitCheck.UnitCheck(product_unit1_upper, product_unit1_upper_index)
    product_unit2_upper, product_unit2_upper_index = UnitCheck.UnitCheck(product_unit2_upper, product_unit2_upper_index)
    # better to combine two list together to increase accuracy	
    product_unit1_combination = product_unit1 + product_unit1_lower + product_unit1_upper
    product_unit2_combination = product_unit2 + product_unit2_lower + product_unit2_upper
    product_unit1_index_combination = product_unit1_index + product_unit1_lower_index + product_unit1_upper_index
    product_unit2_index_combination = product_unit2_index + product_unit2_lower_index + product_unit2_upper_index
    # get rid of same elements	
    product_unit1_combination = list(set(product_unit1_combination))
    product_unit2_combination = list(set(product_unit2_combination))
    product_unit1_index_combination = list(set(product_unit1_index_combination))
    product_unit2_index_combination = list(set(product_unit2_index_combination))
    product_name1_lower = UnitExtraction.UnitExtraction(product_name1_lower, product_unit1_index_combination)
    product_name2_lower = UnitExtraction.UnitExtraction(product_name2_lower, product_unit2_index_combination)
	# still some problems with unit

    #extract special characterstics
    #print(product_name1_lower, product_name2_lower)
    product_name1_special = SpecialExtraction.SpecialExtraction(product_name1_lower)
    product_name2_special = SpecialExtraction.SpecialExtraction(product_name2_lower)
    #print(product_name1_special, product_name2_special)

    # test if special is in another description	
    flag9 = 0
    for each in product_name1_special:
        if each in product_long2:
            flag9 += 1
    flag10 = 0
    for each in product_name2_special:
        if each in product_long1:
            flag10 += 1
    FVmatrix[r][8] = flag9
    FVmatrix[r][9] = flag10

    flag11 = 0
    for each in product_name1_special:
        if each in product_short2:
            flag11 += 1
    flag12 = 0
    for each in product_name2_special:
        if each in product_short1:
            flag12 += 1
    FVmatrix[r][10] = flag11
    FVmatrix[r][11] = flag12
	
    # some minor rule: refurbished
    flag13 = 0
    if 'refurbished' in product_name1_lower:
        if ('refurbished' not in product_name2_lower):
            flag13 = 1
    if 'refurbished' in product_name2_lower:
        if ('refurbished' not in product_name1_lower):
            flag13 = 1
    FVmatrix[r][12] = flag9
	
	# working on 4 sets based method for product name
    #jaccard distance
    FVmatrix[r][13] = simfunctions.jaccard(set(product_name1_lower), set(product_name2_lower))
    #overlap_coefficient distance
    FVmatrix[r][14] = simfunctions.overlap_coefficient(set(product_name1_lower), set(product_name2_lower))
    #cosine distance
    FVmatrix[r][15] = simfunctions.cosine(set(product_name1_lower), set(product_name2_lower))
    #soft_tfidf distance
    FVmatrix[r][16] = simfunctions.soft_tfidf(set(product_name1_lower), set(product_name2_lower))

	# working on 4 sets based method for product special
    #jaccard distance
    FVmatrix[r][17] = simfunctions.jaccard(set(product_name1_special), set(product_name2_special))
    #overlap_coefficient distance
    FVmatrix[r][18] = simfunctions.overlap_coefficient(set(product_name1_special), set(product_name2_special))
    #cosine distance
    FVmatrix[r][19] = simfunctions.cosine(set(product_name1_special), set(product_name2_special))
    #soft_tfidf distance
    FVmatrix[r][20] = simfunctions.soft_tfidf(set(product_name1_special), set(product_name2_special))
	
    # working on 4 sets based method for product unit
    #jaccard distance
    FVmatrix[r][21] = simfunctions.jaccard(set(product_unit1_combination), set(product_unit2_combination))
    #overlap_coefficient distance
    FVmatrix[r][22] = simfunctions.overlap_coefficient(set(product_unit1_combination), set(product_unit2_combination))
    #cosine distance
    FVmatrix[r][23] = simfunctions.cosine(set(product_unit1_combination), set(product_unit2_combination))
    #soft_tfidf distance
    FVmatrix[r][24] = simfunctions.soft_tfidf(set(product_unit1_combination), set(product_unit2_combination))
	
    if(result[r] == 'MATCH\n'):
        FVmatrix[r][25] = 1
    else: 
        FVmatrix[r][25] = 0
    print(product_name1_special, product_name2_special, FVmatrix[r][25])
#print(FVmatrix)
'''
x = open('X_feature_vector_second_round.txt','w')
for each in FVmatrix:
    print(each, file = x)
x.close()		
'''









