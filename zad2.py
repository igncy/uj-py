line = """ZADANIE 2.10 GvR
Mamy dany string wielowierszowy line.
Podać sposób obliczenia liczby wyrazów w stringu."""
word = 'word'
L = [5, 2, 1, 8, 10, 12, 20, 30, 100, 222, 349]
n = 20845805685468500

# 10
print('2.10:', len(line.split()))

# 11
print('2.11:', '_'.join(list(word)))

# 12
print('2.12:', ''.join(x[0] for x in line.split()))
print('2.12:', ''.join(x[-1] for x in line.split()))

# 13
print('2.13:', sum(map(len, line.split())))

# 14
print('2.14:', max([(x, len(x)) for x in line.split()], key=lambda x: x[1]))

# 15
print('2.15:', ''.join(str(x) for x in L))

# 16
print('2.16:', line.replace('GvR', 'Guido van Rossum'))

# 17
print('2.17:', sorted(line.split()))
print('2.17:', sorted(line.split(), key=len))

# 18
print('2.18:', str(n).count('0'))

# 19
print('2.19:', ''.join(str(x).zfill(3) for x in L))
