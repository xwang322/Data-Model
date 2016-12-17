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

with open('X_missing_after_ID_extraction.txt', 'r') as f:
    for i, l in enumerate(f):
        pass
f.close()
print(i + 1)
matrix = [['null' for j in range(8)] for j in range (2*(i+1))]
result = ['null' for j in range(i+1)]
feature_attr = ['product type','product name','product segment','brand','category','product long description','product long description']
freq_word = ['is','you','the','be','to','of','and','a','in','that','have','as','it','for','on','with','do','at','this','by','from','or','an','one','all','over','will','would','so','up','out','if','about','get','who','which','go','can','just','into']
freq_unit = ['foot','volt','gigabyte','megabyte','watt','megahertz','gigahertz','inch','meter','terabyte','gram','ampere','hour','millimeter','minute','liter']

with open('X_missing_after_ID_extraction.txt','r') as f:
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
                if (aname.lower() == 'product name' or aname.lower() == 'product short description' or aname.lower() == 'product long description'):
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
                if (aname.lower() == 'product name' or aname.lower() == 'product short description' or aname.lower() == 'product long description'):
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
x = open('X_19.txt','w')

		    
f.close()
i = int(len(matrix)/2-1)
FVmatrix = [[0 for j in range(18)] for j in range(i+1)]    
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

    # this is for the names 
	
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
    #print(product_name1_lower, product_name2_lower, result[r])

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
    # take out special part, number+letter mix
    product_name1_lower = UnitExtraction.UnitExtraction(product_name1_lower, product_unit1_index_combination)
    product_name2_lower = UnitExtraction.UnitExtraction(product_name2_lower, product_unit2_index_combination)
    # take out the number part
    product_name1_number = NumberExtraction.NumberExtraction(product_name1_lower)
    product_name2_number = NumberExtraction.NumberExtraction(product_name2_lower)
	# in name, number is also included, but combination has been taken out
    print(product_name1_number, file = x)
    print(product_name2_number, file = x)
    #print(product_name1_lower, product_name2_lower)
    print(product_unit1_combination, file = x)
    print(product_unit2_combination, file = x)

	# this is for the long descriptions
	
    product_long1 = string_process4.string_process4(matrix[2*r][6])
    product_long1 = tokenizers.whitespace(product_long1)
    product_long1_lower = []
    for each in product_long1:
        product_long1_lower.append(each.lower())
    product_long1_upper = []
    for each in product_long1:
        product_long1_upper.append(each.upper())
		
    for each in product_long1_lower:
        if each in freq_word:
            index = product_long1_lower.index(each)
            product_long1_lower[index] = ''
            product_long1_upper[index] = ''
            product_long1[index] = ''
    while '' in product_long1_lower:
        product_long1_lower.remove('')
    while '' in product_long1:
        product_long1.remove('')
    while '' in product_long1_upper:
        product_long1_upper.remove('')
    product_long2 = string_process4.string_process4(matrix[2*r+1][6])
    product_long2 = tokenizers.whitespace(product_long2)
    product_long2_lower = []
    for each in product_long2:
        product_long2_lower.append(each.lower())
    product_long2_upper = []
    for each in product_long2:
        product_long2_upper.append(each.upper())
		
    for each in product_long2_lower:
        if each in freq_word:
            index = product_long2_lower.index(each)
            product_long2_lower[index] = ''
            product_long2_upper[index] = ''
            product_long2[index] = ''
    while '' in product_long2_lower:
        product_long2_lower.remove('')
    while '' in product_long2:
        product_long2.remove('')
    while '' in product_long2_upper:
        product_long2_upper.remove('')
    #print(product_long1, product_long2)

    # take out the number part
    product_long1_number = NumberExtraction.NumberExtraction(product_long1_lower)
    product_long2_number = NumberExtraction.NumberExtraction(product_long2_lower)
    print(product_long1_number, file = x)
    print(product_long2_number, file = x)

	# take out json format from long
    product_long1_json = matrix[2*r][6]
    product_long1_json_lower = product_long1_json.lower()
    product1_long_json = JsonLongDescription.JsonLongDescription(product_long1_json_lower)
    product_long2_json = matrix[2*r+1][6]
    product_long2_json_lower = product_long2_json.lower()
    product2_long_json = JsonLongDescription.JsonLongDescription(product_long2_json_lower)
    print(product1_long_json, file = x)
    print(product2_long_json, file = x)	
	
    # Parse out all number+unit
    product_unit1, product_unit1_index = ParseUnit.ParseUnit(product_long1)
    product_unit2, product_unit2_index = ParseUnit.ParseUnit(product_long2)
    product_unit1_lower, product_unit1_lower_index = ParseUnit.ParseUnit(product_long1_lower)
    product_unit2_lower, product_unit2_lower_index = ParseUnit.ParseUnit(product_long2_lower)
    product_unit1_upper, product_unit1_upper_index = ParseUnit.ParseUnit(product_long1_upper)
    product_unit2_upper, product_unit2_upper_index = ParseUnit.ParseUnit(product_long2_upper)
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
    # take out special part, number+letter mix
    product_long1_lower = UnitExtraction.UnitExtraction(product_long1_lower, product_unit1_index_combination)
    product_long2_lower = UnitExtraction.UnitExtraction(product_long2_lower, product_unit2_index_combination)
    print(product_unit1_combination, file = x)
    print(product_unit2_combination, file = x)
	
	
	# this is for the short descriptions
	
    product_short1 = string_process4.string_process4(matrix[2*r][7])
    product_short1 = tokenizers.whitespace(product_short1)
    product_short1_lower = []
    for each in product_short1:
        product_short1_lower.append(each.lower())
    product_short1_upper = []
    for each in product_short1:
        product_short1_upper.append(each.upper())
		
    for each in product_short1_lower:
        if each in freq_word:
            index = product_short1_lower.index(each)
            product_short1_lower[index] = ''
            product_short1_upper[index] = ''
            product_short1[index] = ''
    while '' in product_short1_lower:
        product_short1_lower.remove('')
    while '' in product_short1:
        product_short1.remove('')
    while '' in product_short1_upper:
        product_short1_upper.remove('')
    product_short2 = string_process4.string_process4(matrix[2*r+1][7])
    product_short2 = tokenizers.whitespace(product_short2)
    product_short2_lower = []
    for each in product_short2:
        product_short2_lower.append(each.lower())
    product_short2_upper = []
    for each in product_short2:
        product_short2_upper.append(each.upper())
		
    for each in product_short2_lower:
        if each in freq_word:
            index = product_short2_lower.index(each)
            product_short2_lower[index] = ''
            product_short2_upper[index] = ''
            product_short2[index] = ''
    while '' in product_short2_lower:
        product_short2_lower.remove('')
    while '' in product_short2:
        product_short2.remove('')
    while '' in product_short2_upper:
        product_short2_upper.remove('')
    #print(product_short1, product_short2)
	
    # take out the number part
    product_short1_number = NumberExtraction.NumberExtraction(product_short1_lower)
    product_short2_number = NumberExtraction.NumberExtraction(product_short2_lower)	
    print(product_short1_number, file = x)
    print(product_short2_number, file = x)

	# take out json format from long
    product_short1_json = matrix[2*r][7]
    product_short1_json_lower = product_short1_json.lower()
    product1_short_json = JsonLongDescription.JsonLongDescription(product_short1_json_lower)
    product_short2_json = matrix[2*r+1][7]
    product_short2_json_lower = product_short2_json.lower()
    product2_short_json = JsonLongDescription.JsonLongDescription(product_short2_json_lower)
    print(product1_short_json, file = x)
    print(product2_short_json, file = x)	
	
    # Parse out all number+unit
    product_unit1, product_unit1_index = ParseUnit.ParseUnit(product_short1)
    product_unit2, product_unit2_index = ParseUnit.ParseUnit(product_short2)
    product_unit1_lower, product_unit1_lower_index = ParseUnit.ParseUnit(product_short1_lower)
    product_unit2_lower, product_unit2_lower_index = ParseUnit.ParseUnit(product_short2_lower)
    product_unit1_upper, product_unit1_upper_index = ParseUnit.ParseUnit(product_short1_upper)
    product_unit2_upper, product_unit2_upper_index = ParseUnit.ParseUnit(product_short2_upper)
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
    # take out special part, number+letter mix
    product_short1_lower = UnitExtraction.UnitExtraction(product_short1_lower, product_unit1_index_combination)
    product_short2_lower = UnitExtraction.UnitExtraction(product_short2_lower, product_unit2_index_combination)
    print(product_unit1_combination, file = x)
    print(product_unit2_combination, file = x)
    print(result[r], file = x)	

x.close()







