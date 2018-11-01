def swap(lst, a, b):
    tmp = lst[a]
    lst[a] = lst[b]
    lst[b] = tmp

def bubbleSort(lst):
	n = len(lst)
	while n > 1:  
		i = 0
		while i < n-1:
			if lst[i+1] < lst[i]:
				swap(lst, i, i+1)
			i += 1
			print(lst) # debug
		n -= 1

lst = [5,4,2,1,3]

bubbleSort(lst)
