import filter.path_filter as filter


class Sepecific_path_filter(filter.path_filter):

    def __init__(self, boxes):
        self.boxes = boxes
        self.name = "boxes filter"

    def get_query(self, df):
        data_boxes = None
        for index, box in enumerate(self.boxes):
            if index == 0:
                data_boxes = df.loc[(df.boxNumber == box)]
            else:
                data_boxes = data_boxes.append(df.loc[(df.boxNumber == box)])
        return data_boxes

    def print(self):
        print(f"{self.name}\n boxes numbers{self.boxes} \n ")
