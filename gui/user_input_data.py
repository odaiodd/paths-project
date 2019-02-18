import configrations

dic_user_input = {
    "command": 0,
    "filters_args": {
        1: "",
        2: "",
        3: "",
    },
    "mode": 0,
    "file_path": configrations.file_path,
    "image_path": configrations.image_path,
}


def get_command():
    return dic_user_input["command"]


def get_filters():
    return None


def get_filter_args(filter_num):
    return None


def get_mode():
    return None


def get_file_path():
    return None


def get_image_path():
    return None
