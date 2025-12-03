import pytest

from zad6.points import Point
from zad8.rectangles import Rectangle

class TestRectangle():
    @pytest.fixture(scope='class')
    def a(self):
        return Rectangle(0, 2, 5, 10)

    @pytest.fixture(scope='class')
    def b(self):
        return Rectangle(1, 3, 3, 6)

    @pytest.fixture(scope='class')
    def c(self):
        return Rectangle(1,1,3,3)

    @pytest.fixture(scope='class')
    def d(self):
        return Rectangle(2,0,4,4)

    def test_init(self):
        with pytest.raises(ValueError):
            Rectangle(0,0,0,0)
        with pytest.raises(ValueError):
            Rectangle(5,6,1,3)

    def test_from_points(self, a, b):
        pt1=Point(0,2)
        pt2=Point(5,10)
        assert Rectangle.from_points((pt1, pt2)) == a
        assert Rectangle.from_points((pt1, pt2)) != b

    def test_str(self, a, b):
        assert str(a) == '[(0, 2), (5, 10)]'
        assert str(b) == '[(1, 3), (3, 6)]'

    def test_repr(self, a, b):
        assert repr(a) == 'Rectangle(0, 2, 5, 10)'
        assert repr(b) == 'Rectangle(1, 3, 3, 6)'

    def test_eq(self, a, b):
        assert not a == b
        assert a == Rectangle(0, 2, 5, 10)

    def test_ne(self, a, b):
        assert a != b
        assert not a != Rectangle(0, 2, 5, 10)

    def test_center(self, a, b):
        assert a.center() == Point(2.5, 6)
        assert b.center() == Point(2, 4.5)

    def test_area(self, a, b):
        assert a.area() == 40
        assert b.area() == 6

    def test_move(self, a):
        a.move(1, 1)
        assert a == Rectangle(1, 3, 6, 11)
        a.move(-1, -1)
        assert a == Rectangle(0, 2, 5, 10)

    def test_intersection(self, a, b, c, d):
        assert a.intersection(b) == b
        assert c.intersection(d) == Rectangle(2,1,3,3)
        with pytest.raises(ValueError):
            Rectangle(0, 0, 1, 1).intersection(Rectangle(2,2,3,3))

    def test_cover(self, a, b, c, d):
        assert a.cover(b) == a
        assert c.cover(d) == Rectangle(1,0,4,4)

    def test_make4(self, a, b):
        assert a.make4() == (
            Rectangle(0,2,2.5,6),
            Rectangle(0,6,2.5,10),
            Rectangle(2.5,6,5,10),
            Rectangle(2.5,2,5,6)
        )
        assert b.make4() == (
            Rectangle(1,3,2,4.5),
            Rectangle(1,4.5,2,6),
            Rectangle(2,4.5,3,6),
            Rectangle(2,3,3,4.5)
        )

if __name__ == '__main__':
    pytest.main()