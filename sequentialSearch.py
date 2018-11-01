def sequentialSearch(tgt, lst):
    '''returns the position of the target item if found'''
    idx = 0
    while idx < len(lst):
        if lst[idx] == tgt:
            return idx
        idx += 1
    return -1

lst = [5, 4, 3, 1, 9]
tgt = -3 

a = sequentialSearch(tgt, lst)

if a == -1:
    print('Oo')
else:
    print('idx: ', a)
