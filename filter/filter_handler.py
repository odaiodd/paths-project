import filter.filters_types.random_patch_filter as random_patch_filter
import filter.filters_types.time_filer as time_filter
import filter.filters_types.specific_patch_filter as specific_patch_filter

from gui import user_input_data


def filter_factory(filter_num):
    if filter_num == 1:
        args = input("insert : [from Hour] [to Hour] [date] : date format YYYY-MM-DD(0 for all dates)\n").split()
        # args = user_input_data.get_filter_args(filter_num)
        filter = time_filter.Time_filter(args[0], args[1], args[2])
        return filter

    if filter_num == 2:
        args = input("insert : [x1] [y1] [x2] [y2] : date format YYYY-MM-DD(0 for all dates)\n").split()
        # args = user_input_data.get_filter_args(filter_num)
        filter = random_patch_filter.RandomPatch(int(args[0]), int(args[1]), int(args[2]), int(args[3]))
        return filter

    if filter_num == 3:
        args = input("insert : [box number1] [box number2] ... [box number20] : format integers)\n").split()
        filter = specific_patch_filter.Sepecific_path_filter([int(box) for box in args])
        return filter


def get_filters(filters):
    filter_list = []
    for num_filter in filters:
        filter_list.append(filter_factory(int(num_filter)))
    return filter_list
