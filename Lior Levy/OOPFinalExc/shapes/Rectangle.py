import cv2
from shapes.Shapes import AbsShapes

class Rectangle(AbsShapes):
    def __init__(self , points):
        self.firstPoint = (points[0]["x"] , points[0]["y"])
        self.secondPoint = (points[1]["x"] , points[1]["y"])
        super().__init__()

    def scale(self , scale_factor):
        center_point = ((self.firstPoint[0] + self.secondPoint[0]) / 2, (self.firstPoint[1] + self.secondPoint[1]) / 2)
        self.firstPoint = (round(center_point[0] + (self.firstPoint[0] - center_point[0]) * scale_factor),
                           round(center_point[1] + (self.firstPoint[1] - center_point[1]) * scale_factor))

        self.secondPoint = (round(center_point[0] + (self.secondPoint[0] - center_point[0]) * scale_factor),
                            round(center_point[1] + (self.secondPoint[1] - center_point[1]) * scale_factor))

    def rotate(self, angle):
        self.firstPoint = AbsShapes.rotate_point(self.firstPoint , angle)
        self.secondPoint = AbsShapes.rotate_point(self.secondPoint, angle)

    def translate(self, points):
        self.firstPoint = (points[0] + self.firstPoint[0] ,
                           points[1] + self.firstPoint[1])

        self.secondPoint = (points[0] + self.secondPoint[0],
                            points[1] + self.secondPoint[1])

    def draw(self , canvas ):
        cv2.rectangle(canvas, self.firstPoint, self.secondPoint, self.color, self.thickness)