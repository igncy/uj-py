from zad6_points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):          # "[(x1, y1), (x2, y2)]"
        return f'[{self.pt1}, {self.pt2}]'

    def __repr__(self):         # "Rectangle(x1, y1, x2, y2)"
        return f'Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})'

    def __eq__(self, other):    # obsługa rect1 == rect2
        return

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):           # zwraca środek prostokąta
        return

    def area(self):             # pole powierzchni
        return

    def move(self, x, y):       # przesunięcie o (x, y)
        p=Point(x,y)
        self.pt1+=p
        self.pt2+=p

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.a=Rectangle(0,2,5,10)
        self.b=Rectangle(3,3,1,6)

    def test_str(self):
        self.assertEqual(str(self.a), '[(0, 2), (5, 10)]')
        self.assertEqual(str(self.b), '[(3, 3), (1, 6)]')

    def test_repr(self):
        self.assertEqual(repr(self.a), 'Rectangle(0, 2, 5, 10)')
        self.assertEqual(repr(self.b), 'Rectangle(3, 3, 1, 6)')

    def test_eq(self):
        self.assertEqual(self.a==self.b, False)
        self.assertEqual(self.a==Rectangle(0,2,5,10), True)

    def test_ne(self):
        self.assertEqual(self.a==self.b, True)
        self.assertEqual(self.a==Rectangle(0,2,5,10), False)

    def test_center(self):
        self.assertEqual()

    def test_area(self):
        self.assertEqual()

    def test_move(self):
        self.assertEqual()

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()