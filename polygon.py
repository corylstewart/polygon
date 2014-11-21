__author__ = 'cory'
from point import Point
from line import Line
from triangle import Triangle
import poly2tri


class Polygon:
    def __init__(self):
        self.points_list = []
        self.triangles = None

    def add_point(self, point_p):
        self.points_list.append(point_p)

    def add_point_by_coord(self, x, y):
        point_p = Point()
        point_p.set_coord(x, y)
        self.add_point(point_p)

    def add_points_by_point_list(self, points_list):
        for p in points_list:
            self.points_list.append(p)

    def polygon_is_closed(self):
        return self.points_list[0].points_are_equivalent(self.points_list[-1])

    def close_polygon(self):
        if not self.polygon_is_closed():
            point_p = Point()
            point_p.set_coord(self.points_list[0].get_x(),
                              self.points_list[0].get_y())
            self.points_list.append(point_p)

    def get_points(self):
        return self.points_list

    def is_valid_polygon(self):
        point_p = Point()
        if len(self.points_list) < 4:
            return False
        elif not self.points_list[0].points_are_equivalent(self.points_list[-1]):
            return False

    def make_triangles(self):
        polyline = []
        triangles = []
        for p in self.points_list:
            polyline.append(p.get_coord())
        this_polygon = None
        for i in range(5):
            try:
                this_polygon = poly2tri.Triangulator(polyline)
                break
            except:
                pass
        if not this_polygon:
            return None
        for triangle in this_polygon.polygons:
            point_a = Point()
            point_a.set_coord(triangle[0].x, triangle[0].y)
            point_b = Point()
            point_b.set_coord(triangle[1].x, triangle[1].y)
            point_c = Point()
            point_c.set_coord(triangle[2].x, triangle[2].y)
            this_triangle = Triangle()
            this_triangle.set_point_by_points(point_a,
                                              point_b,
                                              point_c)
            triangles.append(this_triangle)
        return triangles
p1 = Point()
p1.set_coord(0, 0)
p2 = Point()
p2.set_coord(1, 0)
p3 = Point()
p3.set_coord(1, 1)
p4 = Point()
p4.set_coord(0, 1)
p5 = Point()
p5.set_coord(0, 0)
points = [p1, p2, p3, p4]
poly = Polygon()
poly.add_points_by_point_list(points)
poly.close_polygon()
t = poly.make_triangles()
for b in t:
    for p in b.get_points():
        print p.get_coord()