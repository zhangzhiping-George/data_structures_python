def indexOfMin(lst):
    '''returns the index of the minmun item.'''
    idx = 0
    minItem = lst[idx]
    while idx < len(lst):
        if lst[idx] < minItem:
            minItem = lst[idx]
            minidx = idx
        idx += 1
    return minidx, minItem 

lst = [5, 4, 3, 1, 9, 2]

a, b = indexOfMin(lst)

print("idx: {}, minItem: {}".format(a, b))


