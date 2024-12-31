import cv2
from shapes.Shapes import AbsShapes

class Circle(AbsShapes):
    def __init__(self , points):
        self.firstPoint = (points[0]["x"] , points[0]["y"])
        self.radius = points[0]["radius"]
        super().__init__()

    def scale(self, scale_factor):
        self.radius = round(self.radius * scale_factor)

    def rotate(self, angle):
        self.firstPoint = AbsShapes.rotate_point(self.firstPoint , angle)

    def translate(self, points):
        self.firstPoint = (self.firstPoint[0] + points[0],self.firstPoint[1] + points[1])

    def draw(self , canvas ):
        cv2.circle(canvas, self.firstPoint ,
                 self.radius,
                 self.color, self.thickness)