from app.label_map_builder import build_label_map, read_label_dict
from app.image_resizer import resize_images
from app.csv_reader import read_input_lines
import app.paths as paths
from app.tf_record_builder import build_tf_record

RESIZED_IMAGES_SIZE = (300, 300)


def __resize_source_images():
    print("Resize Train images")
    resize_images(paths.TRAIN_SOURCE_IMAGES,
                  paths.TRAIN_RESIZED_IMAGES,
                  paths.TEST_RESIZED_IMAGES_RATIO,
                  RESIZED_IMAGES_SIZE)

    print("Resize Test images")
    resize_images(paths.TEST_SOURCE_IMAGES,
                  paths.TEST_RESIZED_IMAGES,
                  paths.TEST_RESIZED_IMAGES_RATIO,
                  RESIZED_IMAGES_SIZE)


def __build_record(csv_paths, resized_images_dir, resized_images_ratio_path, out_file_path):
    all_lines = []
    for file_path, item_id in csv_paths.items():
        lines = read_input_lines(file_path, resized_images_ratio_path, read_label_dict(paths.LABEL_MAP), item_id)
        all_lines += lines

    build_tf_record(out_file_path, resized_images_dir, all_lines)


def __build_train_record():
    print("\n Building Train record\n")
    __build_record(paths.TRAIN_CSV, paths.TRAIN_RESIZED_IMAGES, paths.TRAIN_RESIZED_IMAGES_RATIO, paths.TRAIN_OUT_PATH)


def __build_test_record():
    print("\n Building Test record\n")
    __build_record(paths.TEST_CSV, paths.TEST_RESIZED_IMAGES, paths.TEST_RESIZED_IMAGES_RATIO, paths.TEST_OUT_PATH)


def execute():
    if input("Need to resize images (y, n) : ") == 'y':
        __resize_source_images()

    build_label_map(paths.LABEL_MAP)
    __build_train_record()
    __build_test_record()
