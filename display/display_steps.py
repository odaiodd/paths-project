import display.display as display
from pylab import *
import configrations


class DisplaySteps(display.Display):

    def __init__(self):
        pass

    def display(self, pathes, objs):
        bg = imread(configrations.image_path)
        for t, n in objs.iteritems():
            imshow(bg)
            o = pathes.loc[t]
            plt.plot(o.x, o.y, label=n)
            show(block=False)
            q = input("press any key to continue to next path\npress q to close\n")
            if q == "q":
                plt.close()
                break
            else:
                plt.close()
