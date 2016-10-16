import sys
def worddist(str1, str2, mapping):
    if not str1 or not str2 or not mapping or str1 not in mapping or str2 not in mapping:
        return -1
    
    l1 = mapping[str1]
    l2 = mapping[str2]
    
    idx1 = idx2 = 0
    ret = sys.maxint
    
    while idx1 < len(l1) and idx2 < len(l2):
        ret = min(ret, abs(l1[idx1] - l2[idx2]))
        if l1[idx1] < l2[idx2]:
            idx1 += 1
        else:
            idx2 += 1
        
    return ret
            
            
    
def preprocess(l, mapping):
    if not l:
        return
    
    for i in range(len(l)):
        if l[i] in mapping:
            mapping[l[i]].append(i)
        else:
            mapping[l[i]] = [i]
            
    return 

l = ["practice", "makes", "perfect", "coding", "makes"]
mapping = {}
preprocess(l, mapping)
print worddist('makes', 'coding', mapping)
