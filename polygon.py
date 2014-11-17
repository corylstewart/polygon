__author__ = 'cory'
from point import Point
from line import Line
from triangle import Triangle


class Polygon:
    def __init__(self):
        self.points_list = []
        self.triangles = None

    def add_point(self, point):
        self.points_list.append(point)

    def add_point_by_coord(self, x, y):
        point = Point()
        point.set_coord(x,y)
        self.add_point(point)

    def get_points(self):
        return self.points_list

    def is_valid_polygon(self):
        point = Point()
        if len(self.points_list) < 4:
            return False
        elif not self.points_list[0].points_are_equivalent(self.points_list[-1]):
            return False