__author__ = 'cory'

from point import Point


class Line:
    def __init__(self):
        self.point_a = None
        self.point_b = None

    def set_line_by_point(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def set_line_by_coord(self, point_a_x, point_a_y, point_b_x, point_b_y):
        point_a = Point()
        point_a.set_coord(point_a_x, point_a_y)
        point_b = Point()
        point_b.set_coord(point_b_x, point_b_y)
        self.set_line_by_point(point_a, point_b)

    def get_line(self):
        return self.point_a.get_coord(), self.point_b.get_coord()

    def line_is_set(self):
        return self.point_a.point_is_set() and self.point_b.point_is_set()

    def x_diff(self):
        return self.point_b.get_x() - self.point_a.get_x()

    def y_diff(self):
        return self.point_b.get_y() - self.point_a.get_y()

    def slope(self):
        x_diff = self.x_diff()
        if x_diff == 0:
            return float('inf')
        else:
            y_diff = self.y_diff()
            return y_diff/x_diff

    def length(self):
        return (self.x_diff()**2 + self.y_diff()**2)**0.5

    def do_lines_intersect(self, other_line):
        if self.lines_are_equivalent(other_line):
            return True
        if self.do_lines_share_point(other_line):
            pass
        else:
            pass

    def lines_are_equivalent(self, other_line):
        return (self.point_a.points_are_equivalent(other_line.point_a) and
                self.point_b.points_are_equivalent(other_line.point_b)) or \
               (self.point_a.points_are_equivalent(other_line.point_b) and
                self.point_b.points_are_equivalent(other_line.point_a))

    def do_lines_share_point(self, other_line):
        return self.point_a.points_are_equivalent(other_line.point_a) or \
            self.point_a.points_are_equivalent(other_line.point_b) or \
            self.point_b.points_are_equivalent(other_line.point_a) or \
            self.point_b.points_are_equivalent(other_line.point_a)

    def do_lines_have_same_slope(self, other_line):
        return self.slope() == other_line.slop()

    def is_point_on_line(self, point, epsilon=.005):
        if self.point_a.points_are_equivalent(point) or self.point_b.points_are_equivalent(point):
            return False
        if abs(self.cross_product(point)) > epsilon:
            return False
        dot_product = self.dot_product(point)
        if dot_product < 0:
            return False
        if dot_product > self.squared_length():
            return False
        return True

    def cross_product(self, point):
        return (point.get_y() - self.point_a.get_y()) * (self.point_b.get_x() - self.point_a.get_x()) - \
               (point.get_x() - self.point_a.get_x()) * (self.point_b.get_y() - self.point_a.get_y())

    def dot_product(self, point):
        return (point.get_x() - self.point_a.get_x()) * (self.point_b.get_x() - self.point_a.get_x()) + \
               (point.get_y() - self.point_a.get_y())*(self.point_b.get_y() - self.point_a.get_y())

    def squared_length(self):
        return (self.point_b.get_x() - self.point_a.get_x())**2 + \
               (self.point_b.get_y() - self.point_a.get_y())**2

    def does_line_overlap(self, other_line):
        if not self.do_lines_share_point(other_line):
            return False
        if self.length() < other_line.length():
            pass


x = Line()
x.set_line_by_coord(0, 0, 1, 1)
y = Line()
y.set_line_by_coord(1, 1, 2, 2)
print x.do_lines_intersect(y)