#from fractions import gcd   # Py2
from math import gcd, isnan  # Py3

def simplify(frac):
    a, b = frac
    if b==0:
        return [float('nan'), float('nan')]
    g = gcd(a, b)
    a //= g
    b //= g
    if b<0:
        a*=-1
        b*=-1
    return [a, b]

def add_frac(frac1, frac2):         # frac1 + frac2
    a, b = frac1
    c, d = frac2
    return simplify([a*d+c*b, b*d])

def sub_frac(frac1, frac2):         # frac1 - frac2
    a, b = frac1
    c, d = frac2
    return simplify([a*d-c*b, b*d])

def mul_frac(frac1, frac2):         # frac1 * frac2
    a, b = frac1
    c, d = frac2
    return simplify([a*c, b*d])

def div_frac(frac1, frac2):         # frac1 / frac2
    a, b = frac1
    c, d = frac2
    if c==0:
        return [float('nan'), float('nan')]
    return simplify([a*d, b*c])

def is_positive(frac):              # bool, czy dodatni
    return simplify(frac)[0]>0

def is_zero(frac):                  # bool, typu [0, x]
    return frac[0]==0 and frac[1]!=0

def cmp_frac(frac1, frac2):         # -1 | 0 | +1
    cmp = sub_frac(frac1, frac2)[0]
    if cmp<0: return -1
    if cmp==0 or isnan(cmp): return 0
    return 1

def frac2float(frac):               # konwersja do float
    return float('nan') if frac[1]==0 else frac[0]/frac[1]

# f1 = [-1, 2]      # -1/2
# f2 = [1, -2]      # -1/2 (niejednoznaczność)
# f3 = [0, 1]       # zero
# f4 = [0, 2]       # zero (niejednoznaczność)
# f5 = [3, 1]       # 3
# f6 = [6, 2]       # 3 (niejednoznaczność)

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])

    def test_is_positive(self):
        self.assertEqual(is_positive([1, 2]), True)
        self.assertEqual(is_positive([-1, -2]), True)
        self.assertEqual(is_positive([-1, 2]), False)
        self.assertEqual(is_positive([1, -2]), False)

    def test_is_zero(self):
        self.assertEqual(is_zero([1, 2]), False)
        self.assertEqual(is_zero([0, 2]), True)
        self.assertEqual(is_zero([0, 0]), False)
        self.assertEqual(is_zero([2, 0]), False)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([1, 3], [1, 2]), -1)
        self.assertEqual(cmp_frac([1, 3], [2, 6]), 0)
        self.assertEqual(cmp_frac([-1, 3], [2, -6]), 0)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), .5)
        self.assertEqual(frac2float([-5, 4]), -1.25)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
