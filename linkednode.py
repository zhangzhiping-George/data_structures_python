'''
singly linked node
'''
__author__ == 'George-Zhangzhiping'

class Node:
    def __init__(self, data, next_ = None):
        self.data = data 
        self.next_ = next_ 

a = Node('A', None)
b = Node('B', a)
c = Node('c', b) 
d = Node('D', c)
e = Node('E', d)

head = e 

'''
# linkednode with dummy header node
a._next = head 

probe = head
while index > 1 and probe._next != head
	probe = probe._next
	index -= 1

probe._next = Node(newItem, probe._next)
'''

'''
probe = head 
while probe != None:
    print(probe._data)
    probe = probe.next_
'''

def getData(tgt):
    probe = head 
    while probe != None and probe.data != tgt:
        probe = probe.next_

    if probe != None:
        print('got {}'.format(tgt) )
    else:
        print('{} is not in the linked structure'.format(tgt) )

getData('E')
getData('X')

def insert(index, newItem):
    if head is None or index < 1:
        head = Node(newItem, head)
    else:
        probe = head
		# probe(i-1).next_ = Node(newItem, probe(i-1).next_)
        while index > 1:# and probe.next_ is not None: 
            probe = probe.next_
            index -= 1
        probe.next_ = Node(newItem, probe.next_)
		# insert the tail
        if probe.next_ is None:
            probe.next_ = Node(newItem)
        else:
            probe.next_ = Node(newItem, probe.next_)

'''
def deleteHead():
    removedData = head.data
    head = head.next_
    return removedData

def deleteTail():
    #only one Node
    if head.next_ is None:
        head == None
    #two more Node
    else:
        probe = head
        while probe.next_.next_ != None: 
            probe = probe.next_
        removedData = probe.next_.data
        #the second from the bottom
        probe.next_ == None
        return removedData
'''

def delete(index):
	if index <= 0:
		removedData = head.data
		head = head.next_
		return removedData
	else:
		probe = head
		while index > 1: 
			probe = probe.next_
			index -= 1
		removedData = probe.next_ 
        if probe.next_.next_ is None:
            probe.next_ = None 
        else:
            probe.next_ = probe.next_.next_
		
		return removedData

# two way node
class twoWayNode(Node):
	def __init__(self, data, previous=None, next_=None):
		super().__init__(self, data, next)
		self._previous = previous

