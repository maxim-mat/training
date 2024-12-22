from typing import Dict

from Shapes.Circle import Circle
from Shapes.CompositeShape import CompositeShape
from Shapes.Line import Line
from Shapes.Point import Point
from Shapes.Rectangle import Rectangle
from Shapes.Shape import Shape
from Shapes.Triangle import Triangle


class ShapeFactoryFromJSON:

    def __init__(self):
        self._shape_classes = {
            "Point": Point,
            "Line": Line,
            "Triangle": Triangle,
            "Rectangle": Rectangle,
            "Circle": Circle}

    def build_shape_from_json(self, json_dict: Dict) -> Shape:
        """
        Builds a Shape object based on the provided JSON dictionary.
        :param json_dict: JSON dictionary describing the shape to build
        :return: A Shape object
        """
        shape_name = json_dict.get("shapeName")
        cleaned_dict = self._filter_relevant_keys(json_dict)
        if shape_name in self._shape_classes:
            return self._shape_classes[shape_name](**cleaned_dict)
        return CompositeShape()

    @staticmethod
    def _filter_relevant_keys(json_dict: Dict) -> Dict:
        """
        Removes keys unrelated to constructing a shape.
        :param json_dict: JSON dictionary to filter
        :return: A filtered dictionary with relevant keys only
        """
        keys_to_exclude = {"shapeName", "translationX", "translationY", "rotate_angle", "resize"}
        return {k: v for k, v in json_dict.items() if k not in keys_to_exclude}

