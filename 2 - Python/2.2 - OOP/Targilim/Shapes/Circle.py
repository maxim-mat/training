import cv2
from Shapes.BasicShape import BasicShape

class Circle(BasicShape):
    def __init__(self, points, radius, color, is_filled):
        """
        Initializes a Circle with the given properties.
        :param points: A list of dictionaries containing the center point coordinates (e.g., [{"x": x, "y": y}]).
        :param radius: The radius of the circle.
        :param color: A dictionary specifying the RGB color values (e.g., {"R": r, "G": g, "B": b}).
        :param is_filled: Boolean indicating if the circle should be filled.
        """
        super().__init__(points, color)
        self._radius = radius
        self._is_filled = is_filled

    def draw(self, image_to_draw_on):
        """
        Draws the circle on the given image canvas.
        :param image_to_draw_on: The image canvas to draw on.
        :return: The modified image with the circle drawn on it.
        """
        thickness = cv2.FILLED if self._is_filled else 1  # Default thickness for non-filled circles is 1
        return cv2.circle(image_to_draw_on, self._points[0], self._radius, self._color, thickness)
