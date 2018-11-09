__author__ = 'George-Zhangzhiping'

'''
two-dimensinal array implementation 
'''

from pyarray import Array

class Grid:

    def  __init__(self, row, column, fillvalue=None):
        self._datas = Array(row) 
        for i in range(row):
            self._datas[i] = Array(column, fillvalue=fillvalue)

    def getLength(self):
        return len(self._datas)
            
    def getWidth(self):
        return len(self._datas[0])

    def __getitem__(self, index):
        return self._datas[index]

    def __setitem__(self, posX, posY, newItem):
        self._datas[posX][posY] = newItem

    def __str__(self):
        res = ''
        for i in range(self.getLength()):
            for j in range(self.getWidth()):
                res += str(self._datas[i][j]) + ' '
            res += '\n'

        return res

g = Grid(3,5)

print(g[0])
print(g[0][1])
print(g)
            
            
        
