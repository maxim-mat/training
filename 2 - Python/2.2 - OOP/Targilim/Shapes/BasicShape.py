import abc
from Geo.Geometric import Geometrics
from Shapes.Shape import Shape


class BasicShape(Shape, metaclass=abc.ABCMeta):
    def __init__(self, points, color):
        """
        Initializes a BasicShape with points and color.
        :param points: A list of dictionaries containing point coordinates (e.g., [{"x": x, "y": y}]).
        :param color: A dictionary specifying the RGB color values (e.g., {"R": r, "G": g, "B": b}).
        """
        self._points = [(points[0]["x"], points[0]["y"])]
        self._color = (color["R"], color["G"], color["B"])

    @abc.abstractmethod
    def draw(self, image_to_draw_on):
        """
        Abstract method to be implemented by subclasses to draw the shape.
        :param image_to_draw_on: The image canvas to draw on.
        """
        pass

    def rotate(self, angle, center=(0, 0)):
        """
        Rotates the shape around a center point by a given angle.
        :param angle: The angle in radians for the rotation.
        :param center: The center point for rotation (default is origin).
        """
        self._points = [
            tuple(map(int, map(round, Geometrics.rotate(center, point, angle))))
            for point in self._points]

    def translate(self, horizontal, vertical):
        """
        Translates the shape by a horizontal and vertical offset.
        :param horizontal: The horizontal translation offset.
        :param vertical: The vertical translation offset.
        """
        self._points = [
            Geometrics.translate(point, horizontal, vertical)
            for point in self._points]

    def resize(self, factor, center=(0, 0)):
        """
        Resizes the shape relative to a center point by a given factor.
        :param factor: The resizing factor.
        :param center: The center point for resizing (default is origin).
        """
        self._points = [
            tuple(map(int, map(round, Geometrics.resize(center, point, factor))))
            for point in self._points]
