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

with open('Y_missing_after_dimension_extraction.txt', 'r') as f:
    for i, l in enumerate(f):
        pass
f.close()
print(i + 1)
matrix = [['null' for j in range(8)] for j in range (2*(i+1))]
result = ['null' for j in range(i+1)]
color = ['null' for j in range(2*(i+1))]
feature_attr = ['product type','product name','product segment','brand','category','product long description','product short description']
freq_word = ['is','you','the','be','to','of','and','a','in','that','have','as','it','for','on','with','do','at','this','by','from','or','an','one','all','over','will','would','so','up','out','if','about','get','who','which','go','can','just','into']
freq_unit = ['foot','volt','gigabyte','megabyte','watt','megahertz','gigahertz','inch','meter','terabyte','gram','ampere','hour','millimeter','minute','liter']
freq_color = ['pink','white','silver','gray','black','red','maroon','yellow','olive','lime','green','aqua','teal','blue','navy','purple','multicolor','fuchsia']
id_list = []
with open('Y_missing_after_dimension_extraction.txt','r') as f:
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
            elif (aname.lower() == 'actual color'):
                color[r] = cname
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
        	
        if color[r] == 'null':
            for each in freq_color:
                if each in matrix[r][6]:
                    color[r] = each
                elif each in matrix[r][2]:
                    color[r] = each
                elif each in matrix[r][7]:
                    color[r] = each
		
		# for product 2
        json_data2 = json.loads(items[4])
        for each in json_data2.keys():
            aname = each
            bname = json_data2.get(aname) 
            cname = ''.join(bname)
            if aname.lower() in feature_attr:
                attrPost = feature_attr.index(aname.lower())
                dict_tmp2.setdefault(aname.lower(), cname.lower())
            elif (aname.lower() == 'actual color'):
                color[r+1] = cname
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
        if matrix[r+1][6] == None:
            matrix[r+1][6] = ''
        matrix[r+1][7] = dict_tmp2.get('product short description')
        if matrix[r+1][7] == None:
            matrix[r+1][7] = ''
        #print(color[r+1])
        		
        if color[r+1] == 'null':
            for each in freq_color:
                if each in matrix[r+1][6]:
                    color[r+1] = each
                elif each in matrix[r+1][2]:
                    color[r+1] = each
                elif each in matrix[r+1][7]:
                    color[r+1] = each
	    		
        result[m] = items[5]
        r += 2
        m += 1		
#print(matrix[0])
#print(result)
#print(color)
z = 0
for each in color:
    if each == 'null':
        z += 1
print(z)
f.close()

i = int(len(matrix)/2-1)
FVmatrix = [[0 for j in range(2)] for j in range(i+1)]    
r = 0
color_total = 0
color_diff = 0
color_same = 0
for r in range(i+1):
    # take the color in the storage and put it here
    product1_color = color[2*r]
    product2_color = color[2*r+1]
    #print('Product 1 color :' + product1_color)	
    #print('Product 2 color :' + product2_color)
    if product1_color == 'null' and product2_color == 'null':
        FVmatrix[r][0] = 999
    if product1_color != 'null' and product2_color != 'null':
        if product1_color == product2_color:
            FVmatrix[r][0] = 1
        else:
            FVmatrix[r][0] = 0
            #color_same += 1			
    if (product1_color == 'null' and product2_color != 'null') or (product2_color == 'null' and product1_color != 'null'):		
        FVmatrix[r][0] = 0	
	
    if(result[r] == 'MATCH\n'):
        FVmatrix[r][1] = 1
    else: 
        FVmatrix[r][1] = 0	
	
    if FVmatrix[r][0] == 0 or FVmatrix[r][0] == 1:
        color_total += 1
    if (FVmatrix[r][0] == 0 and FVmatrix[r][1] == 0) or (FVmatrix[r][0] == 1 and FVmatrix[r][1] == 1):
        color_same += 1
    if (FVmatrix[r][0] == 1 and FVmatrix[r][1] == 0) or (FVmatrix[r][0] == 0 and FVmatrix[r][1] == 1):
        color_diff += 1 		
#print(FVmatrix)
print(color_total, color_same, color_diff)
'''
with open('Y_missing_after_dimension_extraction.txt', 'r') as f:
    r = 0
    a = open('Y_missing_after_color_extraction.txt','w')
    b = open('Y_obtained_after_color_extraction.txt','w')
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
with open('Y_missing_after_color_extraction.txt', 'r') as f:
    for i, l in enumerate(f):
        pass
f.close()
print(i + 1)
original = []
with open('predictions_Y_after_dimension.txt', 'r') as f:
    lines_target = f.readlines()
    for each in lines_target:
        original.append(each)
    with open('Y_obtained_after_color_extraction.txt', 'r') as g:
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
with open('predictions_Y_after_color.txt', 'w') as f:
    for each in original:
        print(each, end = '', file = f)	
f.close()

'''


