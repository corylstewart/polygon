__author__ = 'cory'

from point import Point

print 'testing point'
p = Point()

print 'testing points is None...'
assert not p.point_is_set()

print 'testing setting points to positive numbers...'
p.set_x(1)
p.set_y(2)
assert p.get_coord() == (1, 2)
assert p.point_is_set()

print 'testing get_x get_y...'
assert p.get_x() == 1 and p.get_y() == 2

print 'testing negative, zero and set_coord...'
p.set_coord(-1, 0)
assert p.get_coord() == (-1, 0)

print 'testing decimals...'
p.set_coord(123.456789, -0.0)
assert p.get_coord() == (123.456789, -0.0)

print 'testing points are equivalent...'
p2 = Point()
p2.set_coord(123.456789, -0.0)
assert p.points_are_equivalent(p2)
p2.set_coord(123, -0.0)
assert not p.points_are_equivalent(p2)

print 'done'