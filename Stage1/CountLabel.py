import fileinput
match_count = 0
mismatch_count = 0
missing_label  = 0
with open('elec_pairs_stage1.txt','r') as f:
    for line in f:
        items = line.split('?')
        ###print(items[5])
        if items[5] == 'MATCH\n':
            match_count += 1;
            ###print("Capture one match")
        elif items[5] == 'MISMATCH\n':
            mismatch_count += 1
            ###print("Capture one mismatch")
        else:
            missing_label += 1
f.closed 
print ("There are %d MATCHED products"%(match_count))
print ("There are %d MISMATCHED products"%(mismatch_count))
print ("There are %d UNLABELED products"%(missing_label))