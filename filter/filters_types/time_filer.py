import pandas as pa
import filter.path_filter as filter

class Time_filter(filter.path_filter):

    def __init__(self, from_time, to_time, date):
        self.from_time = from_time
        self.to_time = to_time
        self.name = "Time - Date filter"
        if date == '0':
            self.date = 0
        else:
            self.date = pa.to_datetime(date)

    def get_query(self, df):
        if self.date == 0:
            tf = df[df.time.dt.hour.between(int(self.from_time), int(self.to_time))]
        else:
            tf = df[
                df.time.dt.hour.between(int(self.from_time), int(self.to_time)) & (df.time.dt.date == self.date.date())]

        return tf

    def print(self):
        if self.date == 0:
            print(f"name : {self.name} \n from : {self.from_time} \n to : {self.to_time}\n all dates\n")
        else:
            print( f"name : {self.name} \n from : {self.from_time} \n to : {self.to_time}\n date : {self.date.date()}\n")
