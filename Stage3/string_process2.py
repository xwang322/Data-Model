from py_stringmatching import simfunctions, tokenizers
import re
def string_process2(line):
    line_new = re.sub(r'[],[()]', '', line)
    line_tmp = tokenizers.whitespace(line_new)
    for each in line_tmp:
        if(each == '-'):
            line_tmp.remove(each)
            break
        if(each == '/'):
            line_tmp.remove(each)
            break
    #print(line_tmp)        
    return line_tmp;
a = 'sophia global compatible ink cartridge, replacement [for] canon bci-6 (1 magenta)(refurbished)'    
b = 'hipstreet 10 phoenix google tablet - android 4.4 kitkat, quad core 1.6ghz, 10 screen 1024 x 600 resolution, 8gb storag'
string_process2(b)