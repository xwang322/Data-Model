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

with open('X_missing_after_dimension_extraction.txt', 'r') as f:
    for i, l in enumerate(f):
        pass
f.close()
print(i + 1)
matrix = [['null' for j in range(8)] for j in range (2*(i+1))]
result = ['null' for j in range(i+1)]
feature_attr = ['product type','product name','product segment','brand','category','product long description','product short description']
freq_word = ['is','you','the','be','to','of','and','a','in','that','have','as','it','for','on','with','do','at','this','by','from','or','an','one','all','over','will','would','so','up','out','if','about','get','who','which','go','can','just','into']
freq_unit = ['foot','volt','gigabyte','megabyte','watt','megahertz','gigahertz','inch','meter','terabyte','gram','ampere','hour','millimeter','minute','liter']
freq_color = ['white','silver','gray','black','red','maroon','yellow','olive','lime','green','aqua','teal','blue','navy','purple','multicolor','fuchsia']
id_list = []

with open('X_missing_after_dimension_extraction.txt','r') as f:
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
#print(color)
f.close()


i = int(len(matrix)/2-1)
FVmatrix = [[0 for j in range(3)] for j in range(i+1)]
label = [999 for j in range(i+1)]    
r = 0
p = 0
q = 0
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

    # take out the number part
    product_name1_number = NumberExtraction.NumberExtraction(product_name1_lower)
    product_name1_number = list(set(product_name1_number))
    product_name2_number = NumberExtraction.NumberExtraction(product_name2_lower)
    product_name2_number = list(set(product_name2_number))
    product_name_number_compare = Compare.Compare(product_name1_number, product_name2_number)

	# in name, number is also included, but combination has been taken out
    #print('Product 1 number in name :' + str(product_name1_number))
    #print('Product 2 number in name :' + str(product_name2_number))
    #print('Product number in name compare :' + str(product_name_number_compare))	
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
    product_name_unit1_combination = product_unit1_combination
    product_unit2_combination = list(set(product_unit2_combination))
    product_name_unit2_combination = product_unit2_combination
    product_unit1_index_combination = list(set(product_unit1_index_combination))
    product_unit2_index_combination = list(set(product_unit2_index_combination))
    product_unit_combination_compare = Compare.Compare(product_unit1_combination, product_unit2_combination)
    #print('Product 1 number+unit in name :' + str(product_unit1_combination))
    #print('Product 2 number+unit in name :' + str(product_unit2_combination))
    #print('Product combination in name compare :' + str(product_unit_combination_compare))	
    # take out special part, number+letter mix
    product_name1_lower = UnitExtraction.UnitExtraction(product_name1_lower, product_unit1_index_combination)
    product_name2_lower = UnitExtraction.UnitExtraction(product_name2_lower, product_unit2_index_combination)
    #print(product_name1_lower, product_name2_lower)

    #extract special characterstics
    product_name1_special = SpecialExtraction.SpecialExtraction(product_name1_lower)
    product_name1_special = list(set(product_name1_special))
    product_name2_special = SpecialExtraction.SpecialExtraction(product_name2_lower)
    product_name2_special = list(set(product_name2_special))
    product_name_special_compare = Compare.Compare(product_name1_special, product_name2_special)
    #print('Product 1 special in name :' + str(product_name1_special))
    #print('Product 2 special in name :' + str(product_name2_special))
    #print('Product special in name compare :' + str(product_name_special_compare))		
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
    product_long1_number = list(set(product_long1_number))
    product_long2_number = NumberExtraction.NumberExtraction(product_long2_lower)
    product_long2_number = list(set(product_long2_number))
    product_long_number_compare = Compare.Compare(product_long1_number, product_long2_number)
    #print('Product 1 number in long description :' + str(product_long1_number))
    #print('Product 2 number in long description :' + str(product_long2_number))
    #print('Product number in long compare :' + str(product_long_number_compare))	

	# take out json format from long
    product_long1_json = matrix[2*r][6]
    product_long1_json_lower = product_long1_json.lower()
    product1_long_json = JsonLongDescription.JsonLongDescription(product_long1_json_lower)
    product_long2_json = matrix[2*r+1][6]
    product_long2_json_lower = product_long2_json.lower()
    product2_long_json = JsonLongDescription.JsonLongDescription(product_long2_json_lower)
    #print('Product 1 json in long :' + str(product1_long_json))
    #print('Product 2 json in long :' + str(product2_long_json))	
	
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
    product_long_unit1_combination = product_unit1_combination	
    product_unit2_combination = list(set(product_unit2_combination))
    product_long_unit2_combination = product_unit2_combination
    product_unit1_index_combination = list(set(product_unit1_index_combination))
    product_unit2_index_combination = list(set(product_unit2_index_combination))
    product_unit_combination_compare = Compare.Compare(product_unit1_combination, product_unit2_combination)
    #print('Product 1 number+unit in long :' + str(product_unit1_combination))
    #print('Product 2 number+unit in long :' + str(product_unit2_combination))
    #print('Product combination in long compare :' + str(product_unit_combination_compare))	
    # take out special part, number+letter mix
    product_long1_lower = UnitExtraction.UnitExtraction(product_long1_lower, product_unit1_index_combination)
    product_long2_lower = UnitExtraction.UnitExtraction(product_long2_lower, product_unit2_index_combination)

    #extract special characterstics
    product_long1_special = SpecialExtraction.SpecialExtraction(product_long1_lower)
    product_long1_special = list(set(product_long1_special))
    product_long2_special = SpecialExtraction.SpecialExtraction(product_long2_lower)
    product_long2_special = list(set(product_long2_special))
    product_long_special_compare = Compare.Compare(product_long1_special, product_long2_special)
    #print('Product 1 special in long :' + str(product_long1_special))
    #print('Product 2 special in long :' + str(product_long2_special))	
    #print('Product special in long compare :' + str(product_long_special_compare))		
	
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
    product_short1_number = list(set(product_short1_number))
    product_short2_number = NumberExtraction.NumberExtraction(product_short2_lower)
    product_short2_number = list(set(product_short2_number))
    product_short_number_compare = Compare.Compare(product_short1_number, product_short2_number)
    #print('Product 1 number in short :' + str(product_short1_number))
    #print('Product 2 number in short :' + str(product_short2_number))
    #print('Product number in short compare :' + str(product_short_number_compare))	

	# take out json format from long
    product_short1_json = matrix[2*r][7]
    product_short1_json_lower = product_short1_json.lower()
    product1_short_json = JsonLongDescription.JsonLongDescription(product_short1_json_lower)
    product_short2_json = matrix[2*r+1][7]
    product_short2_json_lower = product_short2_json.lower()
    product2_short_json = JsonLongDescription.JsonLongDescription(product_short2_json_lower)
    #print('Product 1 json in short :' + str(product1_short_json))
    #print('Product 2 json in short :' + str(product2_short_json))	

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
    product_short_unit1_combination = product_unit1_combination
    product_unit2_combination = list(set(product_unit2_combination))
    product_short_unit2_combination = product_unit2_combination
    product_unit1_index_combination = list(set(product_unit1_index_combination))
    product_unit2_index_combination = list(set(product_unit2_index_combination))
    product_unit_combination_compare = Compare.Compare(product_unit1_combination, product_unit2_combination)
    #print('Product 1 number+unit in short :' + str(product_unit1_combination))
    #print('Product 2 number+unit in short :' + str(product_unit2_combination))
    #print('Product combination in short compare :' + str(product_unit_combination_compare))	
    # take out special part, number+letter mix
    product_short1_lower = UnitExtraction.UnitExtraction(product_short1_lower, product_unit1_index_combination)
    product_short2_lower = UnitExtraction.UnitExtraction(product_short2_lower, product_unit2_index_combination)

    #extract special characterstics
    product_short1_special = SpecialExtraction.SpecialExtraction(product_short1_lower)
    product_short1_special = list(set(product_short1_special))
    product_short2_special = SpecialExtraction.SpecialExtraction(product_short2_lower)
    product_short2_special = list(set(product_short2_special))
    product_short_special_compare = Compare.Compare(product_short1_special, product_short2_special)
    #print('Product 1 special in short :' + str(product_short1_special))
    #print('Product 2 special in short :' + str(product_short2_special))
    #print('Product special in short compare :' + str(product_short_special_compare))		

    number1_combo = product_short1_number + product_long1_number + product_name1_number
    number2_combo = product_short2_number + product_long2_number + product_name2_number
    unit1_combo = product_short_unit1_combination + product_long_unit1_combination + product_name_unit1_combination
    unit2_combo = product_short_unit2_combination + product_long_unit2_combination + product_name_unit2_combination
    special1_combo = product_short1_special + product_long1_special + product_name1_special
    special2_combo = product_short2_special + product_long2_special + product_name2_special
    
    number1_combo = list(set(number1_combo))	
    number2_combo = list(set(number2_combo))
    unit1_combo = list(set(unit1_combo))
    unit2_combo = list(set(unit2_combo))
    special1_combo = list(set(special1_combo))
    special2_combo = list(set(special2_combo))
    
    product_number_compare = Compare.Compare(number1_combo, number2_combo) 
    product_unit_compare = Compare.Compare(unit1_combo, unit2_combo)
    product_special_compare = Compare.Compare(special1_combo, special2_combo)
    #print('Product number compare :' + str(product_number_compare))
    #print('Product unit compare :' + str(product_unit_compare))
    #print('Product special compare :' + str(product_special_compare))	
    '''
    FVmatrix[r][0] = product_name_number_compare
    FVmatrix[r][1] = product_unit_combination_compare
    FVmatrix[r][2] = product_name_special_compare
    FVmatrix[r][3] = product_long_number_compare
    FVmatrix[r][4] = product_unit_combination_compare
    FVmatrix[r][5] = product_long_special_compare
    FVmatrix[r][6] = product_short_number_compare
    FVmatrix[r][7] = product_unit_combination_compare
    FVmatrix[r][8] = product_short_special_compare
    '''
    FVmatrix[r][0] = product_number_compare
    FVmatrix[r][1] = product_unit_compare
    FVmatrix[r][2] = product_special_compare
    if 0.0 in FVmatrix[r] and 999 in FVmatrix[r]:
        if FVmatrix[r].count(0.0) + FVmatrix[r].count(999) == 3:
            label[r] = 0
            p += 1
    if(label[r] == 0 and result[r] == 'MISMATCH\n'):
        q += 1		
	# print the result	
    #print(result[r])
print(p,q)
with open('X_missing_after_dimension_extraction.txt', 'r') as f:
    r = 0
    a = open('X_missing_after_special_extraction.txt','w')
    b = open('X_obtained_after_special_extraction.txt','w')
    lines = f.readlines()
    for i in lines:
        if label[r] != 999:
            print(id_list[r] + ', MISMATCH\n', end = '', file = b)
        else:
            print(i, end = '', file = a)
        r += 1
    a.close()
    b.close()	
f.close()
i = 0
with open('X_missing_after_special_extraction.txt', 'r') as f:
    for i, l in enumerate(f):
        pass
f.close()
print(i + 1)
original = []
with open('predictions_X_after_dimension.txt', 'r') as f:
    lines_target = f.readlines()
    for each in lines_target:
        original.append(each)
    with open('X_obtained_after_special_extraction.txt', 'r') as g:
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
with open('predictions_X_after_special.txt', 'w') as f:
    for each in original:
        print(each, end = '', file = f)	
f.close()



