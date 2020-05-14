LABEL_MAP_SIZE = 5


def build_label_map(label_map_path):
    print("Building Label map")
    with open(label_map_path, "w") as out:
        for index in range(1, 6):
            item_str = __build_label_map_item(index)
            out.write(item_str)
        out.close()


EMPTY = ''
LINE2_PART1 = "\tid: "
LINE3_PART1 = "\tname: '"
LINE3_PART2 = "'\n"


def __build_label_map_item(index):
    name = __get_item_name_by_index(index)
    return "item {{\n{}{}\n{}{}{}}}\n".format(LINE2_PART1, index, LINE3_PART1, name, LINE3_PART2)


def __get_item_name_by_index(index):
    if index == 1:
        return 'Information and indicative'
    elif index == 2:
        return 'Danger'
    elif index == 3:
        return 'Main road'
    elif index == 4:
        return 'Mandatory'
    else:
        return 'Prohibitory'


def read_label_dict(label_map_path):
    out_dict = dict()
    with open(label_map_path) as in_f:
        lines = in_f.readlines()
        _id, _name = None, None
        for line in lines:
            if line.startswith(LINE2_PART1):
                _id = int(line.replace(LINE2_PART1, EMPTY))
            elif line.startswith(LINE3_PART1):
                _name = line.replace(LINE3_PART1, EMPTY).replace(LINE3_PART2, EMPTY)
            if _id is not None and _name is not None:
                out_dict[_id] = _name
                _id, _name = None, None
        in_f.close()
    return out_dict
