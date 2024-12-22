import matplotlib.pyplot as plt
from Parsers.JSONParser import JSONParser


class DrawerFromJSON:

    def __init__(self, image_to_draw_on):
        """
        Initializes the DrawerFromJSON instance.
        :param image_to_draw_on: The image canvas to draw on
        """
        self._image_to_draw_on = image_to_draw_on
        self._parser = JSONParser()

    def draw(self, json_file_path: str) -> None:
        """
        Draws the shapes described in the JSON file onto the image canvas.
        :param json_file_path: The path to the JSON file describing the shapes
        :return: None
        """
        # Parse the JSON file to get the shape to draw:
        shape_to_draw = self._parser.parse(json_file_path)

        # Translate the shape to center it on the image canvas:
        center_x = self._image_to_draw_on.shape[1] // 2
        center_y = self._image_to_draw_on.shape[0] // 2
        shape_to_draw.translate(center_x, center_y)

        # Render the shape on the image canvas and display it:
        rendered_image = shape_to_draw.draw(self._image_to_draw_on)
        plt.imshow(rendered_image)
        plt.axis("off")
        plt.show()
