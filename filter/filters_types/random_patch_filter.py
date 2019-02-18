import filter.path_filter as filter
from pylab import *
import configrations


class RandomPatch(filter.path_filter):

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.name = "Random Patch filter"

    def get_query(self, df):
        dx = df[df.x.between(int(self.x1), int(self.x2))]
        dy = dx[dx.y.between(int(self.y1), int(self.y2))]
        return dy


    def print(self):
        print(f"{self.name}\nrectangle : most left ({self.x1},{self.x1}) , most buttom right ({self.x2},{self.x2}) \n ")
