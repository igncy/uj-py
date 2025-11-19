from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):          # "[(x1, y1), (x2, y2)]"
        return f'[{self.pt1}, {self.pt2}]'

    def __repr__(self):         # "Rectangle(x1, y1, x2, y2)"
        return f'Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})'

    def __norm(self):
        return Rectangle(min(self.pt1.x, self.pt2.x),
                         min(self.pt1.y, self.pt2.y),
                         max(self.pt1.x, self.pt2.x),
                         max(self.pt1.y, self.pt2.y))

    def __eq__(self, other):    # obsługa rect1 == rect2
        r1=self.__norm()
        r2=other.__norm()
        return r1.pt1 == r2.pt1 and r1.pt2 == r2.pt2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):           # zwraca środek prostokąta
        r = self.__norm()
        return Point(r.pt1.x+(r.pt2.x-r.pt1.x)/2, r.pt1.y+(r.pt2.y-r.pt1.y)/2)

    def area(self):             # pole powierzchni
        return abs(self.pt1.x-self.pt2.x)*abs(self.pt1.y-self.pt2.y)

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
        self.assertEqual(self.a!=self.b, True)
        self.assertEqual(self.a!=Rectangle(0,2,5,10), False)

    def test_center(self):
        self.assertEqual(self.a.center(),Point(2.5,6))
        self.assertEqual(self.b.center(),Point(2,4.5))

    def test_area(self):
        self.assertEqual(self.a.area(),40)
        self.assertEqual(self.b.area(),6)

    def test_move(self):
        self.a.move(1,1)
        self.assertEqual(self.a, Rectangle(1,3,6,11))

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()