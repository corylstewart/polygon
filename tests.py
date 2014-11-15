__author__ = 'cory'
from line import Line
from point import Point
from triangle import Triangle

t = Triangle()
t.set_point_by_coord(0,0,0,1,1,0)
for point in t.get_points():
    print point.get_coord()
print t.area_of_a_triangle_by_points(t.point_a,t.point_b, t.point_c) == t.area_of_this_triangle()
point = Point()
point.set_coord(.1,.1)
print t.is_point_within_triangle(point)
point.set_coord(0,0)
print t.is_point_within_triangle(point)
point.set_coord(-.1,-.1)
print t.is_point_within_triangle(point)