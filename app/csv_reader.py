import csv

_FILENAME_KEY = 'filename'
_X_FROM_KEY = 'x_from'
_Y_FROM_KEY = 'y_from'
_WIDTH_KEY = 'width'
_HEIGHT_KEY = 'height'
_SIGN_CLASS_KEY = 'sign_class'

_RATIO_X_KEY = 'ratio_x'
_RATIO_Y_KEY = 'ratio_y'


class Line:

    def _generate_fields(self, ratio):
        ratio_x, ratio_y = ratio
        self.x_min_coord = self._x_from * ratio_x
        self.y_min_coord = self._y_from * ratio_y
        self.x_max_coord = (self._x_from + self._width) * ratio_x
        self.y_max_coord = (self._y_from + self._height) * ratio_y

    def __init__(self, row, ratio, item_id, class_name):
        self.filename = row[_FILENAME_KEY]
        self.item_id = item_id
        self.class_name = class_name
        self._x_from = int(row[_X_FROM_KEY])
        self._y_from = int(row[_Y_FROM_KEY])
        self._width = int(row[_WIDTH_KEY])
        self._height = int(row[_HEIGHT_KEY])
        self._sign_class = row[_SIGN_CLASS_KEY]
        self._generate_fields(ratio)


def __read_ration_dict(ratio_path):
    ratio_dict = {}
    with open(ratio_path, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            filename = row[_FILENAME_KEY]
            ratio_x = float(row[_RATIO_X_KEY])
            ratio_y = float(row[_RATIO_Y_KEY])
            ratio_dict[filename] = (ratio_x, ratio_y)
    return ratio_dict


def read_input_lines(in_path, ratio_path, label_map, item_id):
    output = []  # Array of lines
    class_name = label_map[item_id]
    ratio_dict = __read_ration_dict(ratio_path)
    with open(in_path, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            ratio = ratio_dict[row[_FILENAME_KEY]]
            line = Line(row, ratio, item_id, class_name)
            output.append(line)
    print("Read {} items of {} class".format(len(output), class_name))
    return output
