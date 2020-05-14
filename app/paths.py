CORE_INFO_PATH = "D:/Study/ObjectDetection/"
INFO_DIR = "input_data2"

# Output region
LABEL_MAP = CORE_INFO_PATH + INFO_DIR + "/label_map.pbtxt"

TRAIN_RESIZED_IMAGES = CORE_INFO_PATH + INFO_DIR + "/images/train"
TRAIN_RESIZED_IMAGES_RATIO = "{}/ratio.csv".format(TRAIN_RESIZED_IMAGES)

TEST_RESIZED_IMAGES = CORE_INFO_PATH + INFO_DIR + "/images/test"
TEST_RESIZED_IMAGES_RATIO = "{}/ratio.csv".format(TEST_RESIZED_IMAGES)

TEST_OUT_PATH = CORE_INFO_PATH + INFO_DIR + "/test.record"
TRAIN_OUT_PATH = CORE_INFO_PATH + INFO_DIR + "/train.record"


# end region

# Input region
def __path_builder(core_path, dir_name, type_dir):
    return "{}/{}/{}".format(core_path, dir_name, type_dir)


def __get_csv_paths_array(core_path, type_dir):
    dirs_with_id = {
        'danger': 2,
        'main_road': 3,
        'mandatory': 4,
        'blue_rect': 1,
        'blue_border': 1,
        'prohibitory': 5
    }
    return {__path_builder(core_path, dir_name, type_dir): item_id for dir_name, item_id in dirs_with_id.items()}


__CSV_CORE_PATH = CORE_INFO_PATH + "rtsd-d3-gt"
__TRAIN_CSV_DIR = "train_gt.csv"
__TEST_CSV_DIR = "test_gt.csv"

TRAIN_SOURCE_IMAGES = CORE_INFO_PATH + "rtsd-d3-frames/train"
TRAIN_CSV = __get_csv_paths_array(__CSV_CORE_PATH, __TRAIN_CSV_DIR)

TEST_SOURCE_IMAGES = CORE_INFO_PATH + "rtsd-d3-frames/test"
TEST_CSV = __get_csv_paths_array(__CSV_CORE_PATH, __TEST_CSV_DIR)

# end region
