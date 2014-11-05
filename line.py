__author__ = 'cory'

from point import Point


class Line:
    def __init__(self):
        self.pointA = None
        self.pointB = None

    def set_line_by_point(self, pointA, pointB):
        self.pointA = pointA
        self.pointB = pointB

    def set_line_by_coord(self, pointA_x, pointA_y,
                           pointB_x, pointB_y):
        pointA = Point()
        pointA.set_coord(pointA_x, pointA_y)
        pointB = Point()
        pointB.set_coord(pointB_x, pointB_y)
        self.set_line_by_point(pointA, pointB)

    def get_line(self):
        return self.pointA.get_coord(), self.pointB.get_coord()

    def line_is_set(self):
        return self.pointA.point_is_set() and self.pointB.point_is_set()

    def slope(self):
        y_diff = self.pointB.get_y() - self.pointA.get_y()
        if y_diff == 0:
            return float('inf')
        x_diff = self.pointB.get_x() - self.pointA.get_x()
        return x_diff/y_diff

    def _does_line_overlap(self, other_line):
        pass