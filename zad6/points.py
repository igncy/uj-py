from math import sqrt

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):          # zwraca string "(x, y)"
        return f'({self.x}, {self.y})'

    def __repr__(self):         # zwraca string "Point(x, y)"
        return f'Point({self.x}, {self.y})'

    def __eq__(self, other):    # obsługa point1 == point2
        return self.x==other.x and self.y==other.y

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):   # v1 + v2
        return Point(self.x+other.x, self.y+other.y)

    def __sub__(self, other):   # v1 - v2
        return Point(self.x-other.x, self.y-other.y)

    def __mul__(self, other):   # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x*other.x + self.y*other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):           # długość wektora
        return sqrt(self.x*self.x + self.y*self.y)

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase):
    def setUp(self):
        self.p=Point(1,2)
        self.q=Point(4,3)

    def test_str(self):
        self.assertEqual(str(self.p), '(1, 2)')
        self.assertEqual(str(self.q), '(4, 3)')

    def test_repr(self):
        self.assertEqual(repr(self.p), 'Point(1, 2)')
        self.assertEqual(repr(self.q), 'Point(4, 3)')

    def test_eq(self):
        self.assertEqual(self.p==self.q, False)
        self.assertEqual(self.p==Point(1,2), True)

    def test_ne(self):
        self.assertEqual(self.p!=self.q, True)
        self.assertEqual(self.p!=Point(1, 2), False)

    def test_add(self):
        self.assertEqual(self.p+self.q, Point(5,5))

    def test_sub(self):
        self.assertEqual(self.p-self.q, Point(-3,-1))

    def test_mul(self):
        self.assertEqual(self.p*self.q, 10)

    def test_cross(self):
        self.assertEqual(self.p.cross(self.q), -5)

    def test_length(self):
        self.assertEqual(self.p.length(), sqrt(5))
        self.assertEqual(self.q.length(), 5)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()
