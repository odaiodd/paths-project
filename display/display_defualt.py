import display.display as display
from pylab import *
import configrations


class DisplayDefualt(display.Display):

    def __init__(self):
        pass

    def display(self, pathes, objs):
        bg = imread(configrations.image_path)
        imshow(bg)
        for t, n in objs.iteritems():
            o = pathes.loc[t]
            plt.plot(o.x, o.y, label=n)
        show(block=False)
        input("press any key to continue\n")
        plt.close()
