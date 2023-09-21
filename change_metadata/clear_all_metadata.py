import subprocess
import os



def clear_metadata(path_to_image_file):
    # Use exiftool to clear all metadata
    subprocess.run(['exiftool', '-all=', path_to_image_file])

    # Verify metadata is cleared
    metadata = subprocess.check_output(['exiftool', path_to_image_file])
    if len(metadata) == 0:
        print('Metadata cleared successfully')
    else:
        print('Failed to clear metadata')

if __name__ == '__main__':
    clear_metadata('/Volumes/big4photo-4/EDITED_JPEG_ARCHIV/Downloaded_from_fotoagency/Deleted_shoots/KSP_017120/KSP_017120_00016_1h.jpg')