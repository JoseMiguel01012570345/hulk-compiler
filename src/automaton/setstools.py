def PowerSet(elements):
    result = []
    for i in range(len(elements) + 1):
        result += combination_n_k(list(elements),i)
        pass
    return result

def combination_n_k(elements,k):
    return _combination_n_k(elements,[False for e in elements],0,k)

def _combination_n_k(elements,matched,takens=0,count=0,current_set=[]):
    if takens == count:
        for i in range(1,len(current_set)):
            idx0 = elements.index(current_set[i - 1])
            idx1 = elements.index(current_set[i])
            if idx0 > idx1:
                return []
            pass
        return [[] + current_set]
    
    result = []
    for i in range(len(elements)):
        if not matched[i]:
            matched[i] = True
            current_set.append(elements[i])
            result += _combination_n_k(elements,matched,takens + 1,count,current_set)
            current_set.pop()
            matched[i] = False
            pass
        pass
    return result