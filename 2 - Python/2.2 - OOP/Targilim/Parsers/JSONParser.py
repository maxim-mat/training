import copy
import json
import math
from typing import Dict

from Parsers.ShapeFactoryFromJSON import ShapeFactoryFromJSON
from Shapes.Shape import Shape


class JSONParser:

    def __init__(self):
        self._shape_factory = ShapeFactoryFromJSON()
        self._shapes_cache = {}

    def _parse_dict(self, json_dict: Dict) -> Shape:
        """
        Parses a JSON dictionary into a Shape object.
        :param json_dict: JSON dictionary to parse
        :return: Top-level Shape object
        """
        if 'shapeJsonPath' in json_dict:
            shape = self.parse(json_dict['shapeJsonPath'])
        else:
            shape = self._shape_factory.build_shape_from_json(json_dict)
            for sub_json in json_dict.get("shapes", []):
                sub_shape = self._parse_dict(sub_json)
                shape.add_shape(sub_shape)
        self._apply_transformations(shape, json_dict)
        return shape

    def parse(self, shape_json_path: str) -> Shape:
        """
        Parses a JSON file and returns the corresponding Shape object.
        :param shape_json_path: Path to the JSON file
        :return: Parsed Shape object
        """
        if shape_json_path in self._shapes_cache:
            return copy.deepcopy(self._shapes_cache[shape_json_path])
        with open(shape_json_path, 'r') as file:
            json_dict = json.load(file)
            shape = self._parse_dict(json_dict)
            self._shapes_cache[shape_json_path] = copy.deepcopy(shape)
            return shape

    @staticmethod
    def _apply_transformations(shape: Shape, json_dict: Dict) -> None:
        """
        Applies transformations (translation, rotation, resizing) to the Shape based on JSON data.
        :param shape: Shape object to transform
        :param json_dict: JSON dictionary containing transformation data
        """
        JSONParser._apply_translation(shape, json_dict)
        JSONParser._apply_rotation(shape, json_dict)
        JSONParser._apply_resizing(shape, json_dict)

    @staticmethod
    def _apply_translation(shape: Shape, json_dict: Dict) -> None:
        """
        Applies translation to the Shape.
        :param shape: Shape to translate
        :param json_dict: JSON dictionary containing translation data
        """
        translation_x = json_dict.get("translationX")
        translation_y = json_dict.get("translationY")
        if translation_x is not None and translation_y is not None:
            shape.translate(translation_x, translation_y)

    @staticmethod
    def _apply_rotation(shape: Shape, json_dict: Dict) -> None:
        """
        Applies rotation to the Shape.
        :param shape: Shape to rotate
        :param json_dict: JSON dictionary containing rotation data
        """
        rotate_angle = json_dict.get("rotate_angle")
        if rotate_angle is not None:
            shape.rotate(math.radians(rotate_angle))

    @staticmethod
    def _apply_resizing(shape: Shape, json_dict: Dict) -> None:
        """
        Applies resizing to the Shape.

        :param shape: Shape to resize
        :param json_dict: JSON dictionary containing resizing data
        """
        resize_factor = json_dict.get("resize")
        if resize_factor is not None:
            shape.resize(resize_factor)