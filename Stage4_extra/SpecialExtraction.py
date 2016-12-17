from py_stringmatching import simfunctions, tokenizers
import numpy as np
import re

def SpecialExtraction(namelist):
    for each in namelist:
        number = re.findall(r'\d+', each)
        if len(number) != 0:	# this is pure English word
            compare = ''.join(number)
            if compare != each:
                if len(number) == 2:
                    fraction = number[0]+'.'+number[1]
                    if fraction == each:					
                        index = namelist.index(each)
                        namelist[index] = ''
            else:
                index = namelist.index(each)
                namelist[index] = ''
            continue
        word = re.findall(r'[\D|]+', each)
        if len(word) != 0:	# this is pure number
            index = namelist.index(each)
            namelist[index] = ''
            continue

    while '' in namelist:
        namelist.remove('')
    #print(namelist)
    return namelist
#a = ['Level', 'Mounts', 'ELEW7-07', 'finally', 'gives', 'you']	
#SpecialExtraction(a)