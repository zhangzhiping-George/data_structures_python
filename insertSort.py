def swap(lst, a, b):
    tmp = lst[a]
    lst[a] = lst[b]
    lst[b] = tmp

def insertionSort(lst):
    i = 1
    while i < len(lst): 
        insertionItem = lst[i]
        j = i - 1
        while j >= 0:
            if insertionItem < lst[j]:
                lst[j+1] = lst[j]
            else:
                break
            j -= 1
        lst[j+1] = insertionItem 
        print(lst)
        i += 1


lst = [2,5,1,4,3]
insertionSort(lst)
