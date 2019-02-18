import numpy as np
from scipy import misc
from configrations import image_path
from display.load_path_figure import load_path


class Display:
    def __init__(self):
        self.picture = misc.imread(image_path)

    def load_path_figure(self, path):
        self.picture = load_path(self.picture, path)
