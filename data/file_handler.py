import pandas as pa

def make_me_smaller(pf):
    return pf.astype(
        {'x': 'uint16', 'y': 'uint16', 'objectNum': 'uint16', 'sequenceNum': 'uint16', 'filename': 'category',
         'boxNumber': 'uint8', })


def load_file(path):
    de = pa.read_pickle(path)
    de = make_me_smaller(de)
    return de
