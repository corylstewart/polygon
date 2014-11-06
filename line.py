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

    def does_line_overlap(self, other_line):
        pass


x = Line()
x.set_line_by_coord(0, 0, 1, 0)
y = Line()
y.set_line_by_coord(1, 0, 0, 0)
print x.lines_are_equivalent(y)