from JsonDataParser import JsonDataParser
from shapes.ShapeFactory import ShapeFactory
from shapes.Shapes import AbsShapes
from compositeShapes.CompShapeDict import composite_shapes


class CompShape(AbsShapes):
    def __init__(self, points , name):
        super().__init__()
        self.pointX = points[0]["x"]
        self.pointY = points[0]["y"]
        self.name = name
        self.shapes = []
        self.create_comp_shape()

    def create_comp_shape(self):
        factory = ShapeFactory()
        data = JsonDataParser.parse_data_from_file(composite_shapes[self.name])

        for shape in data['shapes']:
            shape_to_draw = factory.create_shape(shape_type=shape['shape_name'], points=shape['points'])

            if not shape_to_draw:
                shape_to_draw = CompShape(shape['points'], shape['shape_name'])

            if 'color' in shape:
                shape_to_draw.set_color(shape['color'])

            if 'filled' in shape and shape['filled']:
                shape_to_draw.set_thickness(-1)

            if 'scale' in shape:
                shape_to_draw.scale(shape['scale'])

            if 'rotate' in shape:
                shape_to_draw.rotate(shape['rotate'])

            shape_to_draw.translate((self.pointX, self.pointY))
            self.shapes.append(shape_to_draw)

    def draw(self , canvas):
        for shape in self.shapes:
            shape.draw(canvas)

    def set_thickness(self, thickness):
        super().set_thickness(thickness)

    def scale(self, scale_factor):
        for shape in self.shapes:
            shape.scale(scale_factor)

    def set_color(self, color):
        super().set_color(color)

    def rotate(self, angle):
        for shape in self.shapes:
            shape.rotate(angle)

    def translate(self, points):
        for shape in self.shapes:
            shape.translate((points[0] , points[1]))






