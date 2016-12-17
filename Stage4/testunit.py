from pint import UnitRegistry
from py_stringmatching import simfunctions, tokenizers
import numpy as np
import re
ureg = UnitRegistry()
#a = '2kg'
#print(a)
a = 'this sentence is to test whether it can test our 2 MB or 2kg or something else'
b = "2kg 3 MB"
b = b.split(' ')
print(b)
list = []
for each in b:
    try:
        print(each)
        ureg.parse_expression(each)
        try:		
            x = ureg.parse_expression(each).magnitude
            y = ureg.parse_expression(each).units
            number = re.findall(r'[\d|]+', each)  # FILTER OUT PURE UNIT
            print(type(number[0]))
            print(x, y)
            if (str(x) == number[0]):
                print(x, y, number)
                list.append(str(x)+' ' +str(y))
        except:
            if(len(number) == 0):
                unit_index = b.index(each)
                print(unit_index)
                if b[unit_index - 1].isdigit():
                    print('sadadad')
                    combine = b[unit_index - 1]+' '+str(y)
                    list.append(combine)
            continue
    except:
        continue
print(list)
#print(a_token)
#print(ureg.parse_expression(a))
#print(ureg.parse_expression(a).magnitude)
#print(ureg.parse_expression(a).units)
#print(ureg.parse_expression(a).dimensionality)