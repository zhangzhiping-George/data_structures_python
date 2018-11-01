def swap(lst, a, b):
    tmp = lst[a] 
    lst[a] = lst[b]
    lst[b] = tmp

def selectSort(lst):
    i = 0
    while i < len(lst)-1: # n-1 searches
        minIdx = i 
        j = i+1
        while j < len(lst):
            if lst[j] < lst[minIdx]:
                minIdx = j
            j += 1
        if i != minIdx:
            swap(lst, i, minIdx)
        i += 1
    print(lst)

lst = [3,2,1,5,4]
selectSort(lst)
