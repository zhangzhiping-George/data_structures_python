import random

def mergesort(lyst):
    lystBuff = [None for i in range(len(lyst))]
    mergesortHelper(lyst, lystBuff, 0, len(lyst)-1) 

def mergesortHelper(lyst, lystBuff, low, high):
    if low < high:
        middle = (low + high)//2
        mergesortHelper(lyst, lystBuff, low, middle)
        mergesortHelper(lyst, lystBuff, middle+1, high)
        merge(lyst, lystBuff, low, middle, high)

def merge(lyst, lystBuff, low, middle, high):
    i1 = low
    i2 = middle + 1
    for i in range(low, high+1): # attention! boundary location
        if i1 > middle:
            lystBuff[i] = lyst[i2]
            i2 += 1
        elif i2 > high:
            lystBuff[i] = lyst[i1]
            i1 += 1 
        elif lyst[i1] < lyst[i2]:
            lystBuff[i] = lyst[i1]
            i1 += 1
        else: 
            lystBuff[i] = lyst[i2]
            i2 += 1
    for i in range(low, high+1):
        lyst[i] = lystBuff[i]
    del lystBuff
     

if __name__ == '__main__':
    lyst = [random.randint(1, 21) for i in range(20)]
    print(lyst)
    mergesort(lyst)
    print(lyst)
