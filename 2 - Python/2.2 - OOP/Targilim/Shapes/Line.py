import cv2
from Shapes.BasicShape import BasicShape


class Line(BasicShape):
    def __init__(self, points, color):
        super().__init__(points, color)
        self._points.append((points[1]["x"], points[1]["y"]))  # Add the second point to the list of points

    def draw(self, image_to_draw_on):
        return cv2.line(image_to_draw_on, self._points[0], self._points[1], self._color) # Draw the line on the image
