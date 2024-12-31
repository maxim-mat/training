import cv2
import numpy as np
from shapes.Shapes import AbsShapes

class Triangle(AbsShapes):
    def __init__(self , points):
        self.firstPoint = (points[0]["x"] , points[0]["y"])
        self.secondPoint = (points[1]["x"], points[1]["y"])
        self.thirdPoint =( points[2]["x"] , points[2]["y"])
        super().__init__()

    def scale(self , scale_factor):
        triangle_center = ((self.firstPoint[0] + self.secondPoint[0] + self.thirdPoint[0])
                           / 3, (self.firstPoint[1] + self.secondPoint[1] + self.thirdPoint[1]) / 3)
        self.firstPoint = (round(triangle_center[0] + (self.firstPoint[0] - triangle_center[0]) * scale_factor) ,
                           round(triangle_center[1] + (self.firstPoint[1] - triangle_center[1]) * scale_factor))

        self.secondPoint = (round(triangle_center[0] + (self.secondPoint[0] - triangle_center[0]) * scale_factor) ,
                           round(triangle_center[1] + (self.secondPoint[1] - triangle_center[1]) * scale_factor))

        self.thirdPoint = (round(triangle_center[0] + (self.thirdPoint[0] - triangle_center[0]) * scale_factor),
                            round(triangle_center[1] + (self.thirdPoint[1] - triangle_center[1]) * scale_factor))

    def rotate(self, angle):
        self.firstPoint = AbsShapes.rotate_point(self.firstPoint , angle)
        self.secondPoint = AbsShapes.rotate_point(self.secondPoint, angle)
        self.thirdPoint = AbsShapes.rotate_point(self.thirdPoint , angle)

    def translate(self, points):
        self.firstPoint = (points[0] + self.firstPoint[0],
                          points[1] + self.firstPoint[1])

        self.secondPoint = (points[0] + self.secondPoint[0],
                            points[1] + self.secondPoint[1])

        self.thirdPoint = (points[0] + self.thirdPoint[0],
                         points[1] + self.thirdPoint[1])

    def draw(self , canvas ):
        triangle_cnt = np.array([self.firstPoint , self.secondPoint , self.thirdPoint])
        cv2.drawContours(canvas, [triangle_cnt] , 0, self.color , self.thickness)