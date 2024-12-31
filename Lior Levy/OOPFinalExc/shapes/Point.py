import cv2
from shapes.Shapes import AbsShapes

class Point(AbsShapes):
    def __init__(self , points):
        self.pointX = points["x"]
        self.pointY = points["y"]
        super().__init__()

    def scale(self , scale_factor):
        pass

    def rotate(self, angle):
        point = AbsShapes.rotate_point((self.pointX , self.pointY), angle)
        self.pointX = point[0]
        self.pointY = point[1]

    def translate(self, points):
        self.pointX = self.pointX + points[0]
        self.pointY = self.pointY + points[1]

    def draw(self , canvas):
        cv2.line(canvas, (self.pointX, self.pointY),
                 (self.pointX, self.pointY),
                 self.color, self.thickness)