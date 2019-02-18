from m_parser import parse_command as p
import command_handler
import configrations
import sys
from gui import user_input_data



def get_command():
    """function gets commands from user and parse it"""
    user_command = input("enter your command\n")
    # user_command = user_input_data.get_command()
    return p.parse(user_command)


def run(m_command):
    """function that runs a command"""
    command_handler.run_command(m_command)
    pass


def main():
    configrations.file_path = sys.argv[1]
    configrations.image_path = sys.argv[2]

    while 1:
        print(configrations.commands)
        my_command = get_command()
        if my_command == 4:
            break

        run(my_command)


if __name__ == '__main__':
    main()
