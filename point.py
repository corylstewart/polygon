class Point:
    def __init__(self):
        self.x = None
        self.y = None

    def set_x(self, x_coord):
        self.x = float(x_coord)

    def set_y(self, y_coord):
        self.y = float(y_coord)

    def set_coord(self, x_coord, y_coord):
        self.set_x(x_coord)
        self.set_y(y_coord)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coord(self):
        return self.get_x(), self.get_y()

    def point_is_set(self):
        if self.get_x() is None or self.get_y() is None:
            return False
        else:
            return True