import cv2
from JsonDataParser import JsonDataParser
from compositeShapes.CompositeShapes import CompShape
from paint.Canvas import Canvas
from shapes.ShapeFactory import ShapeFactory

BASE_FILE_NAME = 'data/data.json'

def draw_basic_shape(factory, shape, canvas):
    shape_to_draw = factory.create_shape(shape_type=shape['shape_name'], points=shape['points'])

    if not shape_to_draw:
        shape_to_draw = CompShape(shape['points'] , shape['shape_name'])

    if 'color' in shape:
        shape_to_draw.set_color(shape['color'])

    if 'filled' in shape and shape['filled']:
        shape_to_draw.set_thickness(-1)

    if 'scale' in shape:
        shape_to_draw.scale(shape['scale'])

    if 'rotate' in shape:
        shape_to_draw.rotate(shape['rotate'])

    shape_to_draw.draw(canvas)


canvas_instance = Canvas.get_canvas_instance()
canvas = canvas_instance.load_canvas()
factory = ShapeFactory()

shape_data = JsonDataParser.parse_data_from_file(BASE_FILE_NAME)

for shape in shape_data['shapes']:
    draw_basic_shape(factory , shape , canvas)

cv2.imshow('shapes', canvas_instance.image)
cv2.waitKey(0)







