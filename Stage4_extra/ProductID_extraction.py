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

with open('predictions_missing.txt', 'r') as f:
    for i, l in enumerate(f):
        pass
f.close()
#print(i + 1)
matrix = [['null' for j in range(4)] for j in range (2*(i+1))]
#result = ['null' for j in range(i+1)]
feature_attr = ['manufacturer part number','product name','product long description','product long description']
freq_word = ['the','be','to','of','and','a','in','that','have','as','it','for','on','with','do','at','this','by','from','or','an','one','all','over','will','would','so','up','out','if','about','get','who','which','go','can','just','into']
id_list = []
with open('predictions_missing.txt','r') as f:
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
        matrix[r][0] = dict_tmp1.get('manufacturer part number')
        matrix[r][1] = dict_tmp1.get('product name')
        matrix[r][2] = dict_tmp1.get('product long description')
        if matrix[r][2] == None:
            matrix[r][2] = ''
        matrix[r][3] = dict_tmp1.get('product short description')
        if matrix[r][3] == None:
            matrix[r][3] = ''
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
        matrix[r+1][0] = dict_tmp2.get('manufacturer part number')
        matrix[r+1][1] = dict_tmp2.get('product name')
        matrix[r+1][2] = dict_tmp2.get('product long description')
        if matrix[r+1][2] == None:
            matrix[r+1][2] = ''
        matrix[r+1][3] = dict_tmp2.get('product short description')
        if matrix[r+1][3] == None:
            matrix[r+1][3] = ''
        #result[m] = items[5]
        r += 2
        m += 1		
#print(matrix[18])
#print(result)
#print(id_list)    
f.close()
i = int(len(matrix)/2-1)
print(i+1)
FVmatrix = [[0 for j in range(2)] for j in range(i+1)]    
r = 0
contain = 0
real = 0
for r in range(i+1):
    manufacturer1 = (matrix[2*r][0])
    manufacturer2 = (matrix[2*r+1][0])
    name1 = (matrix[2*r][1])
    name2 = (matrix[2*r+1][1])
    long1 = (matrix[2*r][2])
    long2 = (matrix[2*r+1][2])
    short1 = (matrix[2*r][3])
    short2 = (matrix[2*r+1][3])
    if (manufacturer1 == '' and manufacturer2 == ''):
        FVmatrix[r][0] = 0	
    if (manufacturer1 != '' and manufacturer2 != ''):
        if (manufacturer1 == manufacturer2):
            FVmatrix[r][0] = 1
        else:
            FVmatrix[r][0] = 0		
    if (manufacturer1 != '' and manufacturer2 == ''):
        target = manufacturer1
        boolean = (target in name2) or (target in long2) or (target in short2)
        if boolean is True:
            FVmatrix[r][0] = 1
            #print(manufacturer1)
        else:
            FVmatrix[r][0] = 0
    if (manufacturer1 == '' and manufacturer2 != ''):
        target = manufacturer2
        boolean = (target in name1) or (target in long1) or (target in short1)
        if boolean is True:
            FVmatrix[r][0] = 1
        else:
            FVmatrix[r][0] = 0

    if FVmatrix[r][0] == 1:
        contain += 1
    '''	
    if(result[r] == 'MATCH\n'):
        FVmatrix[r][1] = 1
    else: 
        FVmatrix[r][1] = 0
    if FVmatrix[r][0] == 1:
        if FVmatrix[r][1] == 1:
            real += 1
    '''
#print(FVmatrix)
#print(contain, real, float(real/contain))
with open('predictions_missing.txt', 'r') as f:
    r = 0
    a = open('predictions_missing_after_ID_extraction.txt','w')
    b = open('predictions_obtained_after_ID_extraction.txt','w')
    lines = f.readlines()
    for i in lines:
        if FVmatrix[r][0] == 1:
            print(id_list[r] + ', MATCH\n', end = '', file = b)
        else:
            print(i, end = '', file = a)
        r += 1
    a.close()
    b.close()	
f.close()
i = 0
with open('predictions_missing_after_ID_extraction.txt', 'r') as f:
    for i, l in enumerate(f):
        pass
f.close()
print(i + 1)
original = []
with open('predictions_22_raw.txt', 'r') as f:
    lines_target = f.readlines()
    for each in lines_target:
        original.append(each)
    with open('predictions_obtained_after_ID_extraction.txt', 'r') as g:
        lines_origin = g.readlines()
        for i in lines_origin:
            items = i.split(',')
            number = items[0]
            value = items[1]
            #print(lines_target[int(number)-1])
            target = number + ', MATCH\n'
            #print(target)
            original[int(number)-1] = target
    #print(original)	
f.close()	
with open('predictions_after_ID.txt', 'w') as f:
    for each in original:
        print(each, end = '', file = f)	
f.close()





