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

with open('X_missing_after_ID_extraction.txt', 'r') as f:
    for i, l in enumerate(f):
        pass
f.close()
#print(i + 1)
missing_collection = [['null' for j in range(4)] for j in range(i+1)]
low_threshold_mismatch_count = 0
low_threshold_match_count = 0
high_threshold_mismatch_count = 0
high_threshold_match_count = 0
with open('X_missing_after_ID_extraction.txt','r') as f:
    lines = f.readlines()
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
            dict_tmp1.setdefault(aname.lower(), cname.lower())
		# for product 2
        json_data2 = json.loads(items[4])
        for each in json_data2.keys():
            aname = each
            bname = json_data2.get(aname) 
            cname = ''.join(bname)
            dict_tmp2.setdefault(aname.lower(), cname.lower()) 
		# start the comparison
        dict_tmp1_list = []
        dict_tmp2_list = []
        for each in dict_tmp1.keys():
            dict_tmp1_list.append(each)
        for each in dict_tmp2.keys():
            dict_tmp2_list.append(each)
        difference = list(set(dict_tmp1_list) - set(dict_tmp2_list))

        for each in difference:
            if 'gtin' in difference:
                index1 = difference.index('gtin')
                difference[index1] = ''
            if 'upc' in difference:
                index2 = difference.index('upc')
                difference[index2] = ''
            if 'category' in difference:
                index3 = difference.index('category')
                difference[index3] = ''
            if 'manufacturer part number' in difference:
                index4 = difference.index('manufacturer part number')
                difference[index4] = ''
            if 'country of origin: components' in difference:
                index5 = difference.index('country of origin: components')
                difference[index5] = ''
        while '' in difference:
            difference.remove('')
        #print(difference) 
        diff_sum = len(difference)
        found_num = 0
        for each in difference:
            value = dict_tmp1.get(each)
            flag = False			
            for every in dict_tmp2.values():
                if flag == False:
                    if value in every:
                        found_num += 1
                        flag = True						
                        break
        missing_collection[m][0] = diff_sum
        missing_collection[m][1] = found_num
        if (diff_sum == 0):
            missing_collection[m][2] = 999
        else:
            missing_collection[m][2] = float(found_num / diff_sum)
        missing_collection[m][3] = items[5]
        if missing_collection[m][2] == 0 and missing_collection[m][3] == 'MISMATCH\n':
            low_threshold_mismatch_count += 1
        if missing_collection[m][2] == 0 and missing_collection[m][3] == 'MATCH\n':
            low_threshold_match_count += 1
        if missing_collection[m][2] >= 0.6 and missing_collection[m][3] == 'MATCH\n':
            high_threshold_match_count += 1
        if missing_collection[m][2] >= 0.6 and missing_collection[m][3] == 'MISMATCH\n':
            high_threshold_mismatch_count += 1			
        m += 1
print(high_threshold_match_count, high_threshold_mismatch_count)
print(low_threshold_match_count, low_threshold_mismatch_count)









