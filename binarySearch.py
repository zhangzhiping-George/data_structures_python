def binarySearch(tgt, sortedLst):
    '''
        midIdx = len(sortedLst)//2
        for i in range(len(sortedLst)):
            if tgt == sortedLst[midIdx]:
                return midIdx
            elif tgt < sortedLst[midIdx]:
                midIdx = midIdx//2
            else:
                midIdx = (midIdx+len(sortedLst))//2
        return -1
    '''
    left = 0
    right = len(sortedLst) - 1
    while left <= right:
        idx = (left  + right)//2
        if tgt == sortedLst[idx]:
            return idx
        elif tgt < sortedLst[idx]:
            right = idx - 1 
        else:
            left = idx + 1 
    return -1

lst = [1,2,3,4,5,6,7, 8, 9, 10, 11, 12,13]

a = binarySearch(3, lst)
if a != -1:
    print(lst[a])
else:
    print('a is -1')
