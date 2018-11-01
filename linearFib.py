def fib(n):
    sum = 1
    first = 1
    second = 1
    count = 3
    while count <= n:
        sum = first + second
        first = second
        second = sum
        count += 1

    return sum

print('fib(10): ', fib(10))
        
