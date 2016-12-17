from py_stringmatching import simfunctions, tokenizers
import re
def string_process4(line):
    line_new = re.sub(r'[],[()]', '', line)
    line_temp = re.sub(r'\<.*?\>', ' ', line_new)
    line_temp2 = line_temp.replace('&nbsp;', ' ')
    line_temp3 = re.sub(r'&#x\w\w\w\w;', ' ', line_temp2)
    line_tmp = tokenizers.whitespace(line_temp3)
    #print(line_tmp)
    for each in line_tmp:
        if(each == '-'):
            line_tmp.remove(each)
            continue
        if(each == '/'):
            line_tmp.remove(each)
            continue
        if(each == ':'):
            line_tmp.remove(each)
            continue
        if(each == '.'):
            line_tmp.remove(each)
            continue
        if(each == '&'):
            line_tmp.remove(each)
            continue
        if('*' in each):
            each_tmp = re.sub(r'\*+', '',each)
            each_tmp.strip();
            line_tmp[line_tmp.index(each)] = each_tmp
            continue
        if(each[len(each)-1] == ':'):
            line_tmp[line_tmp.index(each)] = each[:-1]
            continue
        if(each[len(each)-1] == '.'):
            line_tmp[line_tmp.index(each)] = each[:-1]
            continue
        if(each[len(each)-1] == '-'):
            line_tmp[line_tmp.index(each)] = each[:-1]
            continue
        '''
        if('-' in each and each[len(each)-1] != '-'):
            each_tmp = each.replace('-', ' ')
            each_tmp.strip();
            line_tmp[line_tmp.index(each)] = each_tmp
            continue
        '''
    line_final = ' '.join(line_tmp)
    line_final.strip()
    #print(line_final)
    return line_final;
#a = "Level Mount Universal Wire Management Kit 10, ELEW7-01"
#b = "Level Mount 10FT UNI WIRE MANAGEMENT LVMELEW707"
#c = "Lenmar AA 2700mAh Ni-MH Batteries, 8-Pack"
#d = "Lenmar PRO19 9V 200mAh Ni-MH Battery"
#string_process4(a)