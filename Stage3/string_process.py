from py_stringmatching import simfunctions, tokenizers

def string_process(matrix_ele):
    product_name = tokenizers.whitespace(matrix_ele)
    for each in product_name:
        #get rid of ( at the front
        if('(' in each) and (each.index('(') == 0):
            each_new = each[1:]
            product_name[product_name.index(each)] = each_new
            break
        #get rid of ) at the back
        if(')' in each) and (each.index(')') == len(each)-1):
            each_new = each[:-1]
            product_name[product_name.index(each)] = each_new
            break
        # same to [ and ]
        if('[' in each) and (each.index('[') == 0):
            each_new = each[1:]
            product_name[product_name.index(each)] = each_new
            break			
        if(']' in each) and (each.index(']') == len(each)-1):
            each_new = each[:-1]
            product_name[product_name.index(each)] = each_new
            break
        # get rid of comma at the back
        if(',' in each) and (each.index(',') == len(each)-1):
            if('(' in each) and (each.index('(') == 0):
                each_new = each[1:-1]
                product_name[product_name.index(each)] = each_new
                break
            if('[' in each) and (each.index('(') == 0):
                each_new = each[1:-1]
                product_name[product_name.index(each)] = each_new
                break
            else:
                each_new = each[:-1]
                product_name[product_name.index(each)] = each_new
                break
        if(each == '-'):
            product_name.remove(each)
            break
        if(each == '/'):
            product_name.remove(each)
            break
    print(product_name)            
    return product_name;
a = 'hkc innoview i22lmh1 22 class widescreen led monitor, - 1920x1080 1000000:1 (dynamic contrast) [bla bla, bla] 16:9 aspect ratio - i'    
b = 'hipstreet 10 phoenix google tablet - android 4.4 kitkat, quad core 1.6ghz, 10 screen 1024 x 600 resolution, 8gb storag'
string_process(a)