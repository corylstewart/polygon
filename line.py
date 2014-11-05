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

