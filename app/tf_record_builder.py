from os import path
import tensorflow as tf
from PIL import Image
from random import shuffle


def int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))


def int64_list_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=value))


def bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


def bytes_list_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=value))


def float_list_feature(value):
    return tf.train.Feature(float_list=tf.train.FloatList(value=value))


def __get_image_info(image_path):
    with open(image_path, 'rb') as fid:
        encoded_image = fid.read()
        image = Image.open(image_path)
        width, height = image.size
        return encoded_image, width, height


def __group_by_filename(lines):
    grouped = {}
    filename = None
    items = []
    for line in sorted(lines, key=lambda item: item.filename):
        if line.filename != filename and filename is not None:
            grouped[filename] = items
            filename = line.filename
            items = [[line.x_min_coord], [line.x_max_coord], [line.y_min_coord], [line.y_max_coord],
                     [line.class_name.encode('utf8')],
                     [line.item_id]]
        elif filename is None:
            filename = line.filename
            items = [[line.x_min_coord], [line.x_max_coord], [line.y_min_coord], [line.y_max_coord],
                     [line.class_name.encode('utf8')],
                     [line.item_id]]
        else:
            items[0].append(line.x_min_coord)
            items[1].append(line.x_max_coord)
            items[2].append(line.y_min_coord)
            items[3].append(line.y_max_coord)
            items[4].append(line.class_name.encode('utf8'))
            items[5].append(line.item_id)
    grouped[filename] = items
    return grouped


def __build_tf_example(img_path, filename, items):
    encoded_image, width, height = __get_image_info(img_path)

    x_min = [min_x / width for min_x in items[0]]
    x_max = [max_x / width for max_x in items[1]]
    y_min = [min_y / height for min_y in items[2]]
    y_max = [max_y / height for max_y in items[3]]

    return tf.train.Example(features=tf.train.Features(feature={
        'image/height': int64_feature(height),
        'image/width': int64_feature(width),
        'image/filename': bytes_feature(filename.encode('utf8')),
        'image/source_id': bytes_feature(filename.encode('utf8')),
        'image/encoded': bytes_feature(encoded_image),
        'image/format': bytes_feature(b'jpg'),
        'image/object/bbox/xmin': float_list_feature(x_min),
        'image/object/bbox/xmax': float_list_feature(x_max),
        'image/object/bbox/ymin': float_list_feature(y_min),
        'image/object/bbox/ymax': float_list_feature(y_max),
        'image/object/class/text': bytes_list_feature(items[4]),
        'image/object/class/label': int64_list_feature(items[5]),
    }))


def build_tf_record(out_path, images_path, lines):
    writer = tf.io.TFRecordWriter(out_path)
    shuffle(lines)
    grouped = __group_by_filename(lines)
    for filename, items in grouped.items():
        img_path = path.join(images_path, filename)
        example = __build_tf_example(img_path, filename, items)
        writer.write(example.SerializeToString())
    writer.close()
