# 2
def z5(n):
    r1 = '|'
    r2 = '0'
    for i in range(1, n+1):
        r1 += '....|'
        r2 += str(i).rjust(5, ' ')
    return f'{r1}\n{r2}'

def z6(a, b):
    r = '+---'*b + '+'
    for _ in range(a):
        r += '\n' + '|   '*b + '|\n' + '+---'*b + '+'
    return r

# 3
def factorial(n):
    return 1 if n<=1 else factorial(n-1)*n

for i in range(10):
    print(factorial(i), end=' ')
print()

# 4
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

for i in range(10):
    print(fibonacci(i), end=' ')
print()

# 5
def odwracanie_iter(L, left, right):
    while left <= right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

L=list(range(10))
odwracanie_iter(L, 2, 5)
print(L)
L=list(range(10))
odwracanie_iter(L, 4, 8)
print(L)

def odwracanie_rec(L, left, right):
    if left <= right:
        L[left], L[right] = L[right], L[left]
        odwracanie_rec(L, left+1, right-1)

L=list(range(10))
odwracanie_rec(L, 2, 5)
print(L)
L=list(range(10))
odwracanie_rec(L, 4, 8)
print(L)

# 6
def sum_seq(sequence):
    s = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            s += sum_seq(item)
        else:
            s += item
    return s

print(sum_seq([1,2,(3,4,[2,2,6],5),2,[1,4],1])) # 33

# 7
def flatten(sequence):
    s = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            s += flatten(item)
        else:
            s += [item]
    return s

sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(flatten(sequence)) # [1,2,3,4,5,6,7,8,9]
