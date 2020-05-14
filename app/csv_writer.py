import csv
from app.csv_reader import _FILENAME_KEY, _RATIO_X_KEY, _RATIO_Y_KEY


def write_ratio_after_image_resizing(radio_dict, out_path):
    headers = [_FILENAME_KEY, _RATIO_X_KEY, _RATIO_Y_KEY]
    with open(out_path, 'w', newline='') as out_file:
        writer = csv.DictWriter(out_file, fieldnames=headers)

        writer.writeheader()
        for filename, ratio in radio_dict.items():
            ratio_x, ratio_y = ratio
            writer.writerow({headers[0]: filename, headers[1]: ratio_x, headers[2]: ratio_y})
