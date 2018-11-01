import random

def swap(lst, a, b):
    tmp = lst[a]
    lst[a] = lst[b]
    lst[b] = tmp

def quicksort(lyst):
    quicksortHelper(lyst, 0, len(lyst)-1)

def quicksortHelper(lyst, left, right):
    if left < right:
        pivotLocation = partition(lyst, left, right) 
        quicksortHelper(lyst, left, pivotLocation-1) #left
        quicksortHelper(lyst, pivotLocation+1, right) #right

def partition(lyst, left, right):
    middle = (left + right)//2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    
    boundary = left

    for index in range(left, right):
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            boundary += 1

    swap(lyst, right, boundary)

    return boundary

def main(size=20, sort=quicksort):
    lyst = [random.randint(1, size+1) for i in range(size)]
    print(lyst)
    sort(lyst)
    print(lyst)

if __name__ == '__main__':
    main()
        
