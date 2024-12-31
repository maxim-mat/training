import abc
from math import radians, cos, sin

class AbsShapes(abc.ABC):
    def __init__(self):
        self.color = list([3,3,3])
        self.thickness = 4

    @abc.abstractmethod
    def draw(self , canvas ):
        pass

    @abc.abstractmethod
    def translate(self , points):
        pass

    @abc.abstractmethod
    def rotate(self , angle):
        pass

    def set_color(self, color):
        self.color = color

    def set_thickness(self , thickness):
        self.thickness = thickness

    @abc.abstractmethod
    def scale(self , scale_factor):
        pass

    @staticmethod
    def rotate_point(point, angle):
        center_point = (0, 0)
        angle_rad = radians(angle % 360)
        new_point = (point[0] - center_point[0], point[1] - center_point[1])
        new_point = (new_point[0] * cos(angle_rad) - new_point[1] * sin(angle_rad),
                     new_point[0] * sin(angle_rad) + new_point[1] * cos(angle_rad))
        new_point = (round(new_point[0] + center_point[0]), round(new_point[1] + center_point[1]))
        return new_point