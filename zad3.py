# 1
"""
ZADANIE 3.1
Czy podany kod jest poprawny składniowo w Pythonie? Jeśli nie, to dlaczego?
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

for i in "axby": if ord(i) < 100: print (i)

for i in "axby": print (ord(i) if ord(i) < 100 else i)
"""
# brakuje indentacji przed if w przedostatniej linijce

# 2
"""
ZADANIE 3.2
Co jest złego w kodzie:

L = [3, 5, 4] ; L = L.sort()
.sort() sortuje w miejscu i zwraca None

x, y = 1, 2, 3
za dużo argumentów

X = 1, 2, 3 ; X[1] = 4
x to typ tuple, który jest niemodyfikowalny

X = [1, 2, 3] ; X[3] = 4
indeks poza zasięgiem

X = "abc" ; X.append("d")
typ string nie ma metody append

L = list(map(pow, range(8)))
funkcja pow przyjmuje 2 argumenty
"""

# 3
for i in range(30):
    if i%3!=0: print(i, end=' ')
print()

# 4
def z4():
    while True:
        t=input('input: ')
        if t=='stop': break
        try:
            x=float(t)
            print(x, x**3)
        except ValueError:
            print('error: not a number')
# z4()

# 5
def z5(n):
    r1 = '|'
    r2 = '0'
    for i in range(1, n+1):
        r1 += '....|'
        r2 += str(i).rjust(5, ' ')
    return f'{r1}\n{r2}'

print(z5(12))
assert z5(12) == """\
|....|....|....|....|....|....|....|....|....|....|....|....|
0    1    2    3    4    5    6    7    8    9   10   11   12"""

# 6
def z6(a, b):
    r = '+---'*b + '+'
    for _ in range(a):
        r += '\n' + '|   '*b + '|\n' + '+---'*b + '+'
    return r

print(z6(2, 4))
assert z6(2, 4) == """\
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+"""

# 8
def z8a(a, b):
    return set(a) & set(b)
def z8b(a, b):
    return set(a) | set(b)

print(z8a([1,2,3,5,7], [2,5,7,8])) # 2 5 7
print(z8b([1,2,3,5,7], [2,5,7,8])) # 1 2 3 5 7 8
print(z8a(['a','b','c'], ['a','c','d'])) # a c
print(z8b(['a','b','c'], ['a','c','d'])) # a b c d
assert z8a([1,2,3,5,7], [2,5,7,8]) == {2,5,7}
assert z8b([1,2,3,5,7], [2,5,7,8]) == {1,2,3,5,7,8}
assert z8a(['a','b','c'], ['a','c','d']) == {'a','c'}
assert z8b(['a','b','c'], ['a','c','d']) == {'a','b','c','d'}

# 9
def z9(x):
    return list(map(sum, x))

print(z9([[],[4],(1,2),[3,4],(5,6,7)]))
assert z9([[],[4],(1,2),[3,4],(5,6,7)]) == [0,4,3,7,18]

# 10
ROMAN = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
def roman2int(s):
    if not all(c in ROMAN.keys() for c in s):
        return None
    n = 0
    prev = s[0]
    for c in s[1:]:
        n += ROMAN[prev] if ROMAN[prev] >= ROMAN[c] else -ROMAN[prev]
        prev = c
    n += ROMAN[prev]
    return n

print(roman2int('XVI'))
print(roman2int('XLVII'))
print(roman2int('MCMLXX'))
assert roman2int('XVI') == 16
assert roman2int('XLVII') == 47
assert roman2int('MCMLXX') == 1970
