from shapes.Circle import Circle
from shapes.Line import Line
from shapes.Point import Point
from shapes.Rectangle import Rectangle
from shapes.Triangle import Triangle

class ShapeFactory:
    def create_shape(self, shape_type, **kwargs ):
        if shape_type == 'point':
            return Point(kwargs['points'])
        elif shape_type == 'line':
            return Line(kwargs['points'])
        elif shape_type == 'triangle':
            return Triangle(kwargs['points'])
        elif shape_type == 'rectangle':
            return Rectangle(kwargs['points'])
        elif shape_type == 'circle':
            return Circle(kwargs['points'])
        else:
            return False
