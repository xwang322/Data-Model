from py_stringmatching import simfunctions, tokenizers
import numpy as np
import re

freq_punctuation = ['?','/','.',',','|','-','——','+','=',';',':','%','$','@','&','!','^']
def Compare(prod1, prod2):
# preprocessing the item first
    label = 0
    sim = 0
    if prod1 == [] or prod2 == [] or (prod1 == [] and prod2 == []):
        sim = 999
        return sim
    for each in prod1:
        index1 = prod1.index(each)
        each = list(each)
        for every in freq_punctuation:
            if every in each:
                index = each.index(every)
                each[index] = ''
        while '' in each:
            each.remove('')
        each = ''.join(each)
        prod1[index1] = each
    for each in prod2:
        index1 = prod2.index(each)
        each = list(each)
        for every in freq_punctuation:
            if every in each:
                index = each.index(every)
                each[index] = ''
        while '' in each:
            each.remove('')
        each = ''.join(each)
        prod2[index1] = each
    #print(prod1, prod2)
    length1 = len(prod1)
    length2 = len(prod2)

    if (length1 == length2):
        for each in prod1:
            if each in prod2:
                label += 1
                continue
        sim = float(label / length1)				
    elif(length1 < length2):
        for each in prod1:
            if each in prod2:
                label += 1
                continue
        sim = float(label / length1)
    else:
        for each in prod2:
            if each in prod1:
                label += 1
                continue
        sim = float(label / length2)
		
    #print(sim)
    return sim
#a = ['ddc2b','hd15','st122proa','35mm','15-pin','ddcddc2','60hz']
#b = ['hd15','st122proa','ddc2b']	
#Compare(a,b)