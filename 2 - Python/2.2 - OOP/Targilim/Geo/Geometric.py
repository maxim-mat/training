import math
from typing import Tuple


class Geometrics:

    @staticmethod
    def rotate(center: Tuple[float, float], point: Tuple[float, float], angle_rad: float) -> Tuple[float, float]:
        """
        Rotates a point around another point by a specified angle (in radians).
        :param center: The point around which to rotate.
        :param point: The point to rotate.
        :param angle_rad: The angle of rotation in radians (clockwise).
        :return: The rotated point as a tuple (x, y).
        """
        if center == point:
            return point

        cos_theta = math.cos(angle_rad)
        sin_theta = math.sin(angle_rad)

        # Translate point to origin:
        translated_x = point[0] - center[0]
        translated_y = point[1] - center[1]

        # Perform rotation:
        rotated_x = translated_x * cos_theta - translated_y * sin_theta
        rotated_y = translated_x * sin_theta + translated_y * cos_theta

        # Translate back to original position:
        result_x = rotated_x + center[0]
        result_y = rotated_y + center[1]

        return result_x, result_y

    @staticmethod
    def resize(center: Tuple[float, float], point: Tuple[float, float], factor: float) -> Tuple[float, float]:
        """
        Resizes the distance of a point from a center by a specified factor.
        :param center: The point around which resizing occurs.
        :param point: The point to resize.
        :param factor: The resize factor.
        :return: The resized point as a tuple (x, y).
        """
        delta_x = point[0] - center[0]
        delta_y = point[1] - center[1]

        resized_x = center[0] + factor * delta_x
        resized_y = center[1] + factor * delta_y

        return resized_x, resized_y

    @staticmethod
    def translate(point: Tuple[float, float], delta_x: float, delta_y: float) -> Tuple[float, float]:
        """
        Translates a point by specified horizontal and vertical distances.
        :param point: The point to translate.
        :param delta_x: The horizontal translation distance.
        :param delta_y: The vertical translation distance.
        :return: The translated point as a tuple (x, y).
        """
        translated_x = point[0] + delta_x
        translated_y = point[1] + delta_y

        return translated_x, translated_y
