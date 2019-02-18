import filter.filter_handler as filter_handler
import fetch_combined_query
import display.display_handler as display_handler
import configrations
from gui import user_input_data


g_filters = []


def choose_filters():
    global g_filters
    filters = input(f"insert filters: {configrations.filters}").split(",")
    # filters = user_input_data.get_filters()
    g_filters = filter_handler.get_filters(filters)
    pathes, objs = fetch_combined_query.combine_query_get_pathes_from_db(g_filters)
    display_handler.use_display(pathes, objs)


def display_filters():
    global g_filters
    for filter in g_filters:
        filter.print()

    print("filter display finished\n")
    while (1):
        q = input("filter press q to exit\n")
        if q == "q":
            break


def change_filter():
    pass

