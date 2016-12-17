from py_stringmatching import simfunctions, tokenizers
import numpy as np
import re

freq_unit = ['foot','volt','gigabyte','megabyte','watt','megahertz','gigahertz','inch','meter','terabyte','gram','ampere','hour','millimeter','minute','liter']
def UnitCheck(unitlist, indexlist):
    for each in unitlist:
        each.strip()
        each_tmp = each.split(' ')
        #print(each_tmp)
        each_quantity = each_tmp[0]
        each_unit = each_tmp[1]
        if each_unit not in freq_unit:
            index = unitlist.index(each)
            #print(index)
            unitlist[index] = ''
            indexlist[index] = ''
    while '' in unitlist:
        unitlist.remove('')
    while '' in indexlist:
        indexlist.remove('')
    #print(list)
    return unitlist, indexlist
#a = ['3 decisecond','128 megabyte','128 millibarn','240 picoinch']	
#UnitCheck(a)