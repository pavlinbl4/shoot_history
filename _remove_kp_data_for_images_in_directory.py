from kp_selenium_tools.tk_tools import select_folder_via_gui
from shoot_history.exif_job import clear_image_metadata_from_kp_info
from shoot_history.find_file_hdd import action_with_image_files_in_directory


def main():
    # select directory
    initial_dir = '/Volumes/big4photo-4/EDITED_JPEG_ARCHIV/Downloaded_from_fotoagency'
    path_to_folder = select_folder_via_gui(initial_dir)

    action_with_image_files_in_directory(path_to_folder, clear_image_metadata_from_kp_info)


if __name__ == '__main__':
    main()
