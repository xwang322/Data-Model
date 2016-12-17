from py_stringmatching import simfunctions, tokenizers
import numpy as np
import re

def UnitExtraction(namelist, indexlist):
    for each in indexlist:
        each = int(each)
        namelist[each] = ''
    while '' in namelist:
        namelist.remove('')
    #print(namelist)
    return namelist
#a = ['3 decisecond','128 megabyte','128 millibarn','240 picoinch']	
#UnitExtraction(a)