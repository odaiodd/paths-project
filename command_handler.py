import controller


def run_command(m_command):
    if m_command == 1:
        controller.choose_filters()
    elif m_command == 2:
        controller.change_filter()
    elif m_command == 3:
        controller.display_filters()
