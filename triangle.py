__author__ = 'cory'
from point import Point


class Triangle:
    def __init__(self):
        self.point_a = None
        self.point_b = None
        self.point_c = None

    def set_point_by_coord(self, point_a_x, point_a_y, point_b_x,
                           point_b_y, point_c_x, point_c_y):
        point_a = Point()
        point_a.set_coord(point_a_x, point_a_y)
        point_b = Point()
        point_b.set_coord(point_b_x, point_b_y)
        point_c = Point()
        point_c.set_coord(point_c_x,point_c_y)
        self.set_point_by_points(point_a, point_b, point_c)

    def set_point_by_points(self, point_a, point_b, point_c):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c

    def get_points(self):
        return [self.point_a, self.point_b, self.point_c]

    @staticmethod
    def area_of_a_triangle_by_points(point_a, point_b, point_c):
        return abs(point_a.get_x()*(point_b.get_y()-point_c.get_y()) +
                point_b.get_x()*(point_c.get_y()-point_a.get_y()) +
                point_c.get_x()*(point_a.get_y()-point_b.get_y()))/2.

    def area_of_this_triangle(self):
        return self.area_of_a_triangle_by_points(self.point_a, self.point_b, self.point_c)