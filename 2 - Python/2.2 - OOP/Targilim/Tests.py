import unittest
import numpy as np
from Shapes.Point import Point
from Parsers.JSONParser import JSONParser
from unittest.mock import MagicMock
from Shapes.CompositeShape import CompositeShape
from Geo.Geometric import Geometrics
import math
import sys
sys.path+=['..']
from Parsers.DrawerFromJSON import DrawerFromJSON

class Tests(unittest.TestCase):
    def test_house_json(self):
        parser = JSONParser()
        shape = parser.parse('C:/Users/Maxim/PycharmProjects/Targilim/DataForTest/House.json')
        self.assertEqual(-160, shape._child_shapes[0]._points[0][0])
        self.assertEqual(-55, shape._child_shapes[0]._points[0][1])
        self.assertEqual(160, shape._child_shapes[0]._points[1][0])
        self.assertEqual(-55, shape._child_shapes[0]._points[1][1])
        self.assertEqual(0, shape._child_shapes[0]._points[2][0])
        self.assertEqual(-265, shape._child_shapes[0]._points[2][1])

    def test_point_construct(self):
        point = Point([{"x": 5, "y": 5}], {"R": 255, "G": 0, "B": 0})
        self.assertEqual((5, 5), point._points[0])
        self.assertEqual(1, len(point._points))
        self.assertEqual((255, 0, 0), point._color)

    def test_draw_point_in_image_center(self):
        image_to_draw_on = np.ones((11, 11, 3), np.uint8) * 255
        point_to_draw = Point([{"x": 5, "y": 5}], {"R": 255, "G": 0, "B": 0})
        expected_image = np.ones((11, 11, 3), np.uint8) * 255
        expected_image[5, 5, 1:3] = 0
        expected_image[4, 5, 1:3] = 0
        expected_image[5, 4, 1:3] = 0
        expected_image[6, 5, 1:3] = 0
        expected_image[5, 6, 1:3] = 0
        self.assertTrue(np.array_equal(expected_image, point_to_draw.draw(image_to_draw_on)))

    def test_draw_point_in_image_corner(self):
        image_to_draw_on = np.ones((11, 11, 3), np.uint8) * 255
        point_to_draw = Point([{"x": 0, "y": 0}], {"R": 255, "G": 0, "B": 0})
        expected_image = np.ones((11, 11, 3), np.uint8) * 255
        expected_image[0, 0, 1:3] = 0
        expected_image[0, 1, 1:3] = 0
        expected_image[1, 0, 1:3] = 0
        self.assertTrue(np.array_equal(expected_image, point_to_draw.draw(image_to_draw_on)))

    def test_empty_composite(self):
        shape = CompositeShape()
        self.assertEqual([], shape._child_shapes)

    def test_composite_with_1_basic_shape(self):
        mock_rectangle = MagicMock()
        mock_rectangle._points = [(5, 5), (-5, 5), (-5, -5), (5, -5)]
        comp_shape = CompositeShape()
        comp_shape.add_shape(mock_rectangle)
        self.assertEqual((5, 5), comp_shape._child_shapes[0]._points[0])
        self.assertEqual((-5, 5), comp_shape._child_shapes[0]._points[1])
        self.assertEqual((-5, -5), comp_shape._child_shapes[0]._points[2])
        self.assertEqual((5, -5), comp_shape._child_shapes[0]._points[3])

    def test_composite_1_basic_shape_rotate(self):
        mock_rectangle = MagicMock()
        comp_shape = CompositeShape()
        comp_shape.add_shape(mock_rectangle)
        comp_shape.rotate(315)
        mock_rectangle.rotate.assert_called_with(315, (0, 0))

    def test_composite_2_basic_shape_rotate(self):
        mock_rectangle1 = MagicMock()
        mock_rectangle2 = MagicMock()
        comp_shape = CompositeShape()
        comp_shape.add_shape(mock_rectangle1)
        comp_shape.add_shape(mock_rectangle2)
        comp_shape.rotate(315)
        mock_rectangle1.rotate.assert_called_with(315, (0, 0))
        mock_rectangle2.rotate.assert_called_with(315, (0, 0))

    def test_composite_1_basic_shape_resize(self):
        mock_rectangle = MagicMock()
        comp_shape = CompositeShape()
        comp_shape.add_shape(mock_rectangle)
        comp_shape.resize(2)
        mock_rectangle.resize.assert_called_with(2, (0, 0))

    def test_composite_nested_rotate(self):
        mock_rectangle1 = MagicMock()
        mock_rectangle2 = MagicMock()
        comp_shape1 = CompositeShape()
        comp_shape1.add_shape(mock_rectangle1)
        comp_shape1.add_shape(mock_rectangle2)

        mock_rectangle3 = MagicMock()
        mock_rectangle4 = MagicMock()
        comp_shape2 = CompositeShape()
        comp_shape2.add_shape(mock_rectangle3)
        comp_shape2.add_shape(mock_rectangle4)

        comp_shape = CompositeShape()
        comp_shape.add_shape(comp_shape1)
        comp_shape.add_shape(comp_shape2)

        comp_shape.rotate(315)
        mock_rectangle1.rotate.assert_called_with(315, (0, 0))
        mock_rectangle2.rotate.assert_called_with(315, (0, 0))
        mock_rectangle3.rotate.assert_called_with(315, (0, 0))
        mock_rectangle4.rotate.assert_called_with(315, (0, 0))

    def test_composite_nested_resize(self):
        mock_rectangle1 = MagicMock()
        mock_rectangle2 = MagicMock()
        comp_shape1 = CompositeShape()
        comp_shape1.add_shape(mock_rectangle1)
        comp_shape1.add_shape(mock_rectangle2)

        mock_rectangle3 = MagicMock()
        mock_rectangle4 = MagicMock()
        comp_shape2 = CompositeShape()
        comp_shape2.add_shape(mock_rectangle3)
        comp_shape2.add_shape(mock_rectangle4)

        comp_shape = CompositeShape()
        comp_shape.add_shape(comp_shape1)
        comp_shape.add_shape(comp_shape2)

        comp_shape.resize(2)
        mock_rectangle1.resize.assert_called_with(2, (0, 0))
        mock_rectangle2.resize.assert_called_with(2, (0, 0))
        mock_rectangle3.resize.assert_called_with(2, (0, 0))
        mock_rectangle4.resize.assert_called_with(2, (0, 0))

    def test_composite_nested_translate(self):
        mock_rectangle1 = MagicMock()
        mock_rectangle2 = MagicMock()
        comp_shape1 = CompositeShape()
        comp_shape1.add_shape(mock_rectangle1)
        comp_shape1.add_shape(mock_rectangle2)

        mock_rectangle3 = MagicMock()
        mock_rectangle4 = MagicMock()
        comp_shape2 = CompositeShape()
        comp_shape2.add_shape(mock_rectangle3)
        comp_shape2.add_shape(mock_rectangle4)

        comp_shape = CompositeShape()
        comp_shape.add_shape(comp_shape1)
        comp_shape.add_shape(comp_shape2)

        comp_shape.translate(2, 2)
        mock_rectangle1.translate.assert_called_with(2, 2)
        mock_rectangle2.translate.assert_called_with(2, 2)
        mock_rectangle3.translate.assert_called_with(2, 2)
        mock_rectangle4.translate.assert_called_with(2, 2)

    def test_rotate1(self):
        center = (0, 0)
        point_to_rotate = (-3, 3)
        new_point = Geometrics.rotate(center, point_to_rotate, math.pi / 4)
        self.assertAlmostEqual(-4.2426, new_point[0], places=4)
        self.assertAlmostEqual(0, new_point[1], places=4)

    def test_rotate2(self):
        center = (0, 0)
        point_to_rotate = (-3, 3)
        new_point = Geometrics.rotate(center, point_to_rotate, (2 * math.pi) - (math.pi / 4))
        self.assertAlmostEqual(0, new_point[0], places=4)
        self.assertAlmostEqual(4.2426, new_point[1], places=4)

    def test_rotate3(self):
        center = (0, 0)
        point_to_rotate = (-4, 2)
        new_point = Geometrics.rotate(center, point_to_rotate, (math.pi / 3.3879099684))
        self.assertAlmostEqual(-4, new_point[0], places=4)
        self.assertAlmostEqual(-2, new_point[1], places=4)

    def test_rotate4(self):
        center = (0, 0)
        point_to_rotate = (-4, 2)
        new_point = Geometrics.rotate(center, point_to_rotate, (2 * math.pi) - (math.pi / 3.3879099684))
        self.assertAlmostEqual(-0.8, new_point[0], places=4)
        self.assertAlmostEqual(4.4, new_point[1], places=4)

    def test_rotate5(self):
        center = (-1, 1)
        point_to_rotate = (-5, 3)
        new_point = Geometrics.rotate(center, point_to_rotate, (math.pi / 3.3879099684))
        self.assertAlmostEqual(-5, new_point[0], places=4)
        self.assertAlmostEqual(-1, new_point[1], places=4)

    def test_rotate6(self):
        center = (-1, 1)
        point_to_rotate = (-5, 3)
        new_point = Geometrics.rotate(center, point_to_rotate, (2 * math.pi) - (math.pi / 3.3879099684))
        self.assertAlmostEqual(-1.8, new_point[0], places=4)
        self.assertAlmostEqual(5.4, new_point[1], places=4)

    def test_resize1(self):
        center = (0, 0)
        point_to_move = (-3, 3)
        new_point = Geometrics.resize(center, point_to_move, 2)
        self.assertAlmostEqual(-6, new_point[0], places=4)
        self.assertAlmostEqual(6, new_point[1], places=4)

    def test_resize2(self):
        center = (-1, 1)
        point_to_move = (-3, 3)
        new_point = Geometrics.resize(center, point_to_move, 2)
        self.assertAlmostEqual(-5, new_point[0], places=4)
        self.assertAlmostEqual(5, new_point[1], places=4)

    def test_resize3(self):
        center = (-1, 1)
        point_to_move = (-3, 3)
        new_point = Geometrics.resize(center, point_to_move, 0.5)
        self.assertAlmostEqual(-2, new_point[0], places=4)
        self.assertAlmostEqual(2, new_point[1], places=4)

    def test_resize4(self):
        center = (0, 0)
        point_to_move = (-3, 3)
        new_point = Geometrics.resize(center, point_to_move, 0.5)
        self.assertAlmostEqual(-1.5, new_point[0], places=4)
        self.assertAlmostEqual(1.5, new_point[1], places=4)

    def test_translate1(self):
        point = (0, 0)
        new_point = Geometrics.translate(point, 2, 2)
        self.assertEqual((2, 2), new_point)

    def test_translate2(self):
        point = (0, 0)
        new_point = Geometrics.translate(point, -2, -2)
        self.assertEqual((-2, -2), new_point)

    def draw_city(self):
        json_img_to_draw_on3 = np.ones((500, 500, 3), np.uint8) * 255
        drawer = DrawerFromJSON(json_img_to_draw_on3)
        drawer.draw('../DataForTest/TrafficLightAndTriangleRotated.json')

        json_img_to_draw_on4 = np.ones((3000, 2100, 3), np.uint8) * 195
        drawer = DrawerFromJSON(json_img_to_draw_on4)
        drawer.draw('../DataForTest/City.json')

if __name__ == '__main__':
    unittest.main()