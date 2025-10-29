def add_poly(poly1, poly2):         # poly1(x) + poly2(x)
    n = max(len(poly1), len(poly2))
    poly = [0]*n
    i = 0
    while i < n:
        try:
            poly[i] += poly1[i]
        except IndexError:
            pass
        try:
            poly[i] += poly2[i]
        except IndexError:
            pass
        i += 1
    return poly

def sub_poly(poly1, poly2):         # poly1(x) - poly2(x)
    poly = add_poly(poly1, -poly2)
    return poly

def mul_poly(poly1, poly2): pass        # poly1(x) * poly2(x)

def is_zero(poly): pass                 # bool, [0], [0,0], itp.

def eq_poly(poly1, poly2):         # bool, porównywanie poly1(x) == poly2(x)
    if len(poly1) != len(poly2):
        return False
    for i in range(len(poly1)):
        if poly1[i] != poly2[i]:
            return False
    return True

def eval_poly(poly, x0): pass           # poly(x0), algorytm Hornera

def combine_poly(poly1, poly2): pass    # poly1(poly2(x)), trudne!

def pow_poly(poly, n): pass             # poly(x) ** n

def diff_poly(poly):                # pochodna wielomianu
    diff = poly[:]
    for i in range(len(poly)-2, -1, -1):
        diff[i] += i+1
        diff[i+1] = 0
    return diff

# p1 = [2, 1]                   # W(x) = 2 + x
# p2 = [2, 1, 0]                # jw  (niejednoznaczność)
# p3 = [-3, 0, 1]               # W(x) = -3 + x^2
# p4 = [3]                      # W(x) = 3, wielomian zerowego stopnia
# p5 = [0]                      # zero
# p6 = [0, 0, 0]                # zero (niejednoznaczność)

import unittest

class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [0, 1]      # W(x) = x
        self.p2 = [0, 0, 1]   # W(x) = x^2

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p2), [0, 1, 1])

    def test_sub_poly(self): pass

    def test_mul_poly(self): pass

    def test_is_zero(self): pass

    def test_eq_poly(self):
        self.assertEqual(eq_poly(self.p1, [0, 1]), True)
        self.assertEqual(eq_poly(self.p2, [0, 0, 1]), True)

    def test_eval_poly(self): pass

    def test_combine_poly(self): pass

    def test_pow_poly(self): pass

    def test_diff_poly(self):
        self.assertEqual(diff_poly(self.p1), [1, 0])
        self.assertEqual(diff_poly(self.p2), [0, 2, 0])


    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
