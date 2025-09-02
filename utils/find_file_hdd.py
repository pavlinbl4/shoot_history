import os


def find_no_ext(file_name_no_extension: str, path: str) -> list:
    """
    Find files with the given name (without extension) in the specified path.
    Only checks files with extensions: dng, nef, orf, jpg, jpeg.

    Args:
        file_name_no_extension: File name without extension to search for
        path: Directory path to search in

    Returns:
        List of full paths to matching files
    """
    result = []
    valid_extensions = {'dng', 'nef', 'orf', 'jpg', 'jpeg'}

    for root, _, files in os.walk(path):
        for file in files:
            # Split filename and extension
            name, ext = os.path.splitext(file)
            ext = ext[1:].lower()  # Remove dot and convert to lowercase

            if ext in valid_extensions and name == file_name_no_extension:
                result.append(os.path.join(root, file))

    return result
