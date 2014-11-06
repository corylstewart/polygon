__author__ = 'cory'

from point import Point


class Line:
    def __init__(self):
        self.point_a = None
        self.point_b = None

    def set_line_by_point(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def set_line_by_coord(self, point_a_x, point_a_y,
                           point_b_x, point_b_y):
        point_a = Point()
        point_a.set_coord(point_a_x, point_a_y)
        point_b = Point()
        point_b.set_coord(point_b_x, point_b_y)
        self.set_line_by_point(point_a, point_b)

    def get_line(self):
        return self.point_a.get_coord(), self.point_b.get_coord()

    def line_is_set(self):
        return self.point_a.point_is_set() and self.point_b.point_is_set()

    def slope(self):
        y_diff = self.point_b.get_y() - self.point_a.get_y()
        if y_diff == 0:
            return float('inf')
        x_diff = self.point_b.get_x() - self.point_a.get_x()
        return x_diff/y_diff

    def _does_line_overlap(self, other_line):
        pass