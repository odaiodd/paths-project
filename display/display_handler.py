import display.display_defualt as display_defualt
import display.display_steps as display_steps
from gui import user_input_data

def use_display(pathes, objs):
    mode = input("press 1 for normal display mode \npress 2 for display step mode\n")
    # mode = user_input_data.get_mode()
    mode = int(mode)
    if mode == 1:
        display_defualt.DisplayDefualt().display(pathes, objs)
    elif mode == 2:
        display_steps.DisplaySteps().display(pathes, objs)
