from zad6.points import Point

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        # Chcemy, aby x1 < x2, y1 < y2.
        if x1 >= x2 or y1 >= y2:
            raise ValueError('error: x1 >= x2 or y1 >= y2')
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    @classmethod
    def from_points(cls, points):
        pt1, pt2 = points
        return cls(pt1.x, pt1.y, pt2.x, pt2.y)

    @property
    def top(self):
        return self.pt2.y

    @property
    def left(self):
        return self.pt1.x

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def right(self):
        return self.pt2.x

    @property
    def width(self):
        return self.pt2.x-self.pt1.x

    @property
    def height(self):
        return self.pt2.y-self.pt1.y

    @property
    def topleft(self):
        return Point(self.pt1.x, self.pt2.y)

    @property
    def bottomleft(self):
        return self.pt1

    @property
    def topright(self):
        return self.pt2

    @property
    def bottomright(self):
        return Point(self.pt2.x, self.pt1.y)

    def __str__(self):          # "[(x1, y1), (x2, y2)]"
        return f'[{self.pt1}, {self.pt2}]'

    def __repr__(self):         # "Rectangle(x1, y1, x2, y2)"
        return f'Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})'

    def __eq__(self, other):    # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    @property
    def center(self):           # zwraca środek prostokąta
        return Point((self.pt1.x+self.pt2.x)/2, (self.pt1.y+self.pt2.y)/2)

    def area(self):             # pole powierzchni
        return abs(self.pt1.x-self.pt2.x)*abs(self.pt1.y-self.pt2.y)

    def move(self, x, y):       # przesunięcie o (x, y)
        p=Point(x,y)
        self.pt1+=p
        self.pt2+=p

    def intersection(self, other):  # część wspólna prostokątów
        x1, y1, x2, y2 = (
            max(self.pt1.x, other.pt1.x),
            max(self.pt1.y, other.pt1.y),
            min(self.pt2.x, other.pt2.x),
            min(self.pt2.y, other.pt2.y)
        )
        if x1>=x2 or y1>=y2:
            raise ValueError('error: rectangles do not intersect')
        return Rectangle(x1,y1,x2,y2)

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
