import os
import stat
import exiftool
from loguru import logger
import time
import shutil
import subprocess


def color_to_rating(color):
    mapping = {"Red": 1, "Yellow": 2, "Green": 3, "Blue": 4, "Purple": 5}
    return mapping.get(color, 0)


def wait_for_usb_disk(volume_path, timeout=10):
    """Ожидает появления USB-диска в системе"""
    start_time = time.time()
    while time.time() - start_time < timeout:
        if os.path.exists(volume_path):
            return True
        time.sleep(1)
    return False


def safe_file_operation(path_to_file, operation, max_retries=3, delay=1):
    """Повторяет операцию при возникновении ошибок"""
    for attempt in range(max_retries):
        try:
            return operation(path_to_file)
        except (FileNotFoundError, PermissionError, OSError) as e:
            if attempt == max_retries - 1:
                raise
            logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay} sec...")
            time.sleep(delay)


def change_color_class(path_to_file, photo_id, image_caption, color):
    # Получаем абсолютный путь с разрешением символических ссылок
    path_to_file = os.path.realpath(path_to_file)
    logger.info(f'Absolute real path: {path_to_file}')

    # Извлекаем путь к точке монтирования
    volume_path = os.path.join('/', *path_to_file.split(os.sep)[:3])

    # Ожидаем появление USB-диска
    if not wait_for_usb_disk(volume_path):
        logger.error(f"USB disk not found at {volume_path}")
        return

    # Проверяем доступность файла с повторными попытками
    try:
        safe_file_operation(path_to_file, lambda x: None)
    except Exception as e:
        logger.error(f"File inaccessible: {e}")
        return

    # Создаем временную копию файла на внутреннем диске
    temp_dir = os.path.join(os.path.expanduser('~'), 'temp_exif_edit')
    os.makedirs(temp_dir, exist_ok=True)
    temp_path = os.path.join(temp_dir, os.path.basename(path_to_file))

    try:
        # Копируем файл на внутренний диск
        safe_file_operation(path_to_file, lambda src: shutil.copy2(src, temp_path))

        # Работаем с локальной копией
        with exiftool.ExifToolHelper() as et:
            et.set_tags(
                [temp_path],
                tags={
                    "XMP:Title": photo_id,
                    "IPTC:ObjectName": photo_id,
                    "XMP:Description": image_caption,
                    "IPTC:Caption-Abstract": image_caption,
                    "XMP:Creator": 'Eugene Pavlenko',
                    "XMP:Label": color,
                    "XMP:Rating": color_to_rating(color),
                    "XMP:ColorLabel": color
                },
                params=[
                    "-P",
                    "-overwrite_original",
                    "-E",
                    "-ec",
                    "-charset", "iptc=UTF-8"
                ]
            )

        # Копируем измененный файл обратно на USB
        safe_file_operation(temp_path, lambda src: shutil.copy2(src, path_to_file))

        logger.success("Metadata updated successfully on USB drive")
    except Exception as e:
        logger.error(f"Operation failed: {e}")
    finally:
        # Удаляем временную копию
        if os.path.exists(temp_path):
            os.remove(temp_path)
        if os.path.exists(temp_dir):
            os.rmdir(temp_dir)


if __name__ == '__main__':
    # Используем сырую строку и явно задаем путь
    raw_path = r'/Volumes/big4photo-2/2025/20250519_Юридический форум/20250519PEV_2976.NEF'

    change_color_class(
        raw_path,
        'KSP_018418_00001',
        '19.05.2025 Россия, Санкт-Петербург  XIII Петербургский международный юридический форум (ПМЮФ) в конгрессно-выставочном центре (КВЦ) "Экспофорум"',
        "Red"
    )
