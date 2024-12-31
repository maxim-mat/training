import cv2

class Canvas:
    _instance = None
    image = None

    @staticmethod
    def get_canvas_instance():
        if Canvas._instance is None:
            Canvas._instance = Canvas()
        return Canvas._instance

    def load_canvas(self):
        WIDTH = 1000
        HEIGHT = 600

        path = r'C:\Users\liorl\Downloads\backgroundCanvas.jpeg'
        self.image = cv2.imread(path)
        self.image = cv2.resize(self.image, (WIDTH, HEIGHT))

        # convert colors in image from bgr to rgb
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

        return self.image

