from points import Point

'''
W pliku rectangles.py zdefiniować klasę Rectangle wraz z potrzebnymi metodami. Wykorzystać wyjątek ValueError do obsługi błędów. Napisać kod testujący moduł rectangles. 
'''

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        # Chcemy, aby x1 < x2, y1 < y2.
        self.pt1 = Point(min(x1, x2), min(y1, y2))
        self.pt2 = Point(max(x1, x2), max(y1, y2))

    def __str__(self):          # "[(x1, y1), (x2, y2)]"
        return f'[{self.pt1}, {self.pt2}]'

    def __repr__(self):         # "Rectangle(x1, y1, x2, y2)"
        return f'Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})'

    def __eq__(self, other):    # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):           # zwraca środek prostokąta
        return Point(self.pt1.x+(self.pt2.x-self.pt1.x)/2, self.pt1.y+(self.pt2.y-self.pt1.y)/2)

    def area(self):             # pole powierzchni
        return abs(self.pt1.x-self.pt2.x)*abs(self.pt1.y-self.pt2.y)

    def move(self, x, y):       # przesunięcie o (x, y)
        p=Point(x,y)
        self.pt1+=p
        self.pt2+=p

    def intersection(self, other):  # część wspólna prostokątów
        raise ValueError

    def cover(self, other):     # prostąkąt nakrywający oba
        return Rectangle(
            min(self.pt1.x, other.pt1.x),
            min(self.pt1.y, other.pt1.y),
            max(self.pt2.x, other.pt2.x),
            max(self.pt2.y, other.pt2.y)
        )

    def make4(self):            # zwraca krotkę czterech mniejszych
        lx=self.pt2.x-self.pt1.x
        ly=self.pt2.y-self.pt1.y
        dx=lx/2
        dy=ly/2
        # 2 3
        # 1 4
        return (
            Rectangle(self.pt1.x, self.pt1.y, self.pt1.x+dx, self.pt1.y+dy),
            Rectangle(self.pt1.x, self.pt1.y+dy, self.pt1.x+dx, self.pt1.y+2*dy),
            Rectangle(self.pt2.x-dx, self.pt2.y-dy, self.pt2.x, self.pt2.y),
            Rectangle(self.pt2.x-dx, self.pt2.y-2*dy, self.pt2.x, self.pt2.y-dy),
        )
# A-------B   po podziale  A---+---B
# |       |                |   |   |
# |       |                +---+---+
# |       |                |   |   |
# D-------C                D---+---C

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.a = Rectangle(0, 2, 5, 10)
        self.b = Rectangle(3, 3, 1, 6)
        self.c = Rectangle(1,1,3,3)
        self.d = Rectangle(2,0,4,4)

    def test_str(self):
        self.assertEqual(str(self.a), '[(0, 2), (5, 10)]')
        self.assertEqual(str(self.b), '[(1, 3), (3, 6)]')

    def test_repr(self):
        self.assertEqual(repr(self.a), 'Rectangle(0, 2, 5, 10)')
        self.assertEqual(repr(self.b), 'Rectangle(1, 3, 3, 6)')

    def test_eq(self):
        self.assertEqual(self.a == self.b, False)
        self.assertEqual(self.a == Rectangle(0, 2, 5, 10), True)

    def test_ne(self):
        self.assertEqual(self.a != self.b, True)
        self.assertEqual(self.a != Rectangle(0, 2, 5, 10), False)

    def test_center(self):
        self.assertEqual(self.a.center(), Point(2.5, 6))
        self.assertEqual(self.b.center(), Point(2, 4.5))

    def test_area(self):
        self.assertEqual(self.a.area(), 40)
        self.assertEqual(self.b.area(), 6)

    def test_move(self):
        self.a.move(1, 1)
        self.assertEqual(self.a, Rectangle(1, 3, 6, 11))

    def test_intersection(self):
        self.assertEqual(self.a.intersection(self.b), self.b)
        self.assertEqual(self.c.intersection(self.d), Rectangle(2,1,3,3))
        self.assertRaises(ValueError, Rectangle(0,0,1,1).intersection, Rectangle(2,2,3,3))

    def test_cover(self):
        self.assertEqual(self.a.cover(self.b), self.a)
        self.assertEqual(self.c.cover(self.d), Rectangle(1,0,4,4))

    def test_make4(self):
        self.assertEqual(self.a.make4(), (
            Rectangle(0,2,2.5,6),
            Rectangle(0,6,2.5,10),
            Rectangle(2.5,6,5,10),
            Rectangle(2.5,2,5,6)
        ))
        self.assertEqual(self.b.make4(), (
            Rectangle(1,3,2,4.5),
            Rectangle(1,4.5,2,6),
            Rectangle(2,4.5,3,6),
            Rectangle(2,3,3,4.5)
        ))

if __name__ == '__main__':
    unittest.main()
