'''
__author__ = 'George-Zhangzhiping'
__verion__ = 1.0

1. Arrary with [], str, len, iter and 
2. array: insert(index, value), delete(index)
3. resize Array  capacity

# Array instace initiation example
a = Array(10)
a = Array(10, fillvalue=9)
'''

class Array:
    def __init__(self, capacity, fillvalue=None):
        #self._items = [fillvalue for i in range(capacity)] 
        self._items = list()
        for i in range(capacity):
            self._items.append(fillvalue)

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __str__(self):
        return '<{}({})>'.format(self.__class__.__name__,
                                self.__len__())
    def __iter__(self):                               
        return iter(self._items)

    def insert(self, index, value):
        for i in range(len(self._items)-1, index, -1):
            self._items[i] = self._items[i-1] 
        self._items[index] = value

    def delete(self, index=None):
        for i in range(index, len(self._items)-1):
            self._items[i] = self._items[i+1] 
        self._items[-1] = None 

    def extend(self):
        pass

    def decrease(self):
        pass

'''
#Q1: how to keep Array capacity fixed after insert(), delete().
#Q2: where to execute resize operation. 
#A: use functions out of class, not attr mothods

# Test Demos:
a = Array(10, fillvalue=1)
print([i for i in a])

a.insert(2, 10)
print([i for i in a])

a.delete(2)
print([i for i in a])

a[1] = 3
a[2] = 6 
print([i for i in a])
'''
