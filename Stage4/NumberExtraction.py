from py_stringmatching import simfunctions, tokenizers
import numpy as np
import re

def NumberExtraction(namelist):
    numberlist = []
    for each in namelist:
        number = re.findall(r'[\d|]+', each)
        if (len(number) == 2): # this is fractional number
            number = number[0]+'.'+number[1]
            if number == each:
                numberlist.append(number)
        elif (len(number) == 1):
            number = number[0]
            if number == each:
                numberlist.append(number)           
    #print(numberlist)
    return numberlist
#a = ['dock','128','10.2','dsve4342','x','14.5&quot','adjustable']
#b = ['Level', 'Mount', 'Universal', 'Wire', 'Management', 'Kit', '10', 'ELEW7-01']	
#NumberExtraction(a)