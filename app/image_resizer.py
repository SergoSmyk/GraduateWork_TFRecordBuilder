import os
from PIL import Image
from app.csv_writer import write_ratio_after_image_resizing


def __print_progress(number, count):
    print("\rProgress:  {}/{}".format(number, count), end='')


def resize_images(in_dir, out_dir, ration_file_path, new_size):
    image_list = os.listdir(in_dir)
    images_count = len(image_list)
    number = 1
    ratio_dict = {}
    for img_name in image_list:
        __print_progress(number, images_count)
        in_path = os.path.join(in_dir, img_name)
        image = Image.open(in_path)
        in_w, in_h = image.size
        out_w, out_h = new_size
        ratio_dict[img_name] = (out_w / in_w, out_h / in_h)
        resized_image = image.resize(new_size)
        out_path = os.path.join(out_dir, img_name)
        resized_image.save(out_path)
        number += 1
    write_ratio_after_image_resizing(ratio_dict, ration_file_path)
    print()
