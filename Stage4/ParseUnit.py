from pint import UnitRegistry
from py_stringmatching import simfunctions, tokenizers
import numpy as np
import re

def ParseUnit(list):
    ureg = UnitRegistry()
    output = []
    output_index = []
    for each in list:
        try:
            ureg.parse_expression(each)
            try:		
                x = ureg.parse_expression(each).magnitude
                y = ureg.parse_expression(each).units
                number = re.findall(r'[\d|]+', each)  # pure unit would generate error      number = re.findall(r'(\d+)\.(\d*)', each)
                #print(number[0],len(number)) #if pure unit, number should be null, then cannot get into the condition below
                #print(x, y)
                if (len(number) == 1): # there would be only one number, so number[0] for integer
                    if (str(x) == number[0]): 
                        combine = str(x) + ' ' + str(y)
                        output.append(combine)
                        output_index.append(list.index(each))
                if (len(number) == 2): # this is fractional number
                    number = number[0]+'.'+number[1]
                    #print(number)
                    if (str(x) == number): 
                        combine = str(x) + ' ' + str(y)
                        output.append(combine)
                        output_index.append(list.index(each))
            except:
                if(len(number) == 0):
                    unit_index = list.index(each)
                    #print(unit_index)
                    if list[unit_index - 1].isdigit():
                        combine = list[unit_index - 1] + ' ' + str(y)
                        output.append(combine)
                        output_index.append(list.index(each))
                continue
        except:
            continue
    #print(output)
    #print(output_index)
    return output, output_index
#a = ['cyberpower','2','38','MB','56kg','120V','400mah','10ft','240mAh','360','PC','4.7GB'] # not perfect for 400mah
#list1, list2 = ParseUnit(a)
#print(list1)