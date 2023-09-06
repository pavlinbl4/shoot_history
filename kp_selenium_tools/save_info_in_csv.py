import os
import csv

from kp_selenium_tools.check_file_exist import create_file_if_not_exists


def csv_writer(info, columns_name, csv_file_path):
    def write_csv_file(info, csv_file_path):
        with open(csv_file_path, 'a') as input_file:
            writer = csv.writer(input_file)
            writer.writerow(info)

    if os.path.exists(csv_file_path):
        write_csv_file(info, csv_file_path)
    else:
        info = columns_name
        write_csv_file(info, csv_file_path)


def write_lost_files_info(original_file_name, photo_id):
    csv_file = create_file_if_not_exists('Kommersant/shoot_rename', 'lost_images.csv')
    columns_name = ['original_file_name', 'photo_id']
    info = [original_file_name, photo_id]
    csv_writer(info, columns_name, csv_file)






