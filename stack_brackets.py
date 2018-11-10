__author__ = 'George-Zhangzhiping'

'''
brackets pairs check with stack structure
'''

def brackets(pairstr):
    prechs = '{[('
    sufchs = ')]}'
    stack = list()
    for ch in pairstr:
        #print('str: {}'.format(ch))
        if ch in prechs: 
            stack.append(ch)
        else: 
            popch = stack.pop()
            if ch == ')' and popch != '(' \
                or ch == ']' and popch != '[' \
                or ch == '}' and popch != '{':
                return False
    if len(stack) == 0:
        return  True 
    else:
        return  False 
        

pairstr1 = '{[()]}{}[]()'
pairstr2 = '{[}()[]}{}[]()'

assert brackets(pairstr1) is True
print('===')
assert brackets(pairstr2) is False 
