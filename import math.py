
class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_perimeter(self):
        perimeter = 6 * self.side_length
        return perimeter

    def calculate_area(self):
        area = (3 * Hexagon.sqrt(3) * (self.side_length ** 2)) / 2
        return area

    def calculate_angles(self):
        angle = 720 / 6
        return angle

        