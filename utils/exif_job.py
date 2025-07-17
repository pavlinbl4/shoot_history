
import os
import subprocess

import exiftool
from loguru import logger


def color_to_rating(color):
    mapping = {"Red": 1, "Yellow": 2, "Green": 3, "Blue": 4, "Purple": 5}
    return mapping.get(color, 0)


def change_color_class(path_to_file, photo_id, image_caption, color):
    # Нормализуем путь: заменяем двойные пробелы на одинарные
    path_to_file = path_to_file.replace("  ", " ")
    logger.info(f'Normalized path: {path_to_file}')
    logger.info(f'{photo_id = }')
    logger.info(f'{image_caption = }')

    # Проверяем существование файла
    if not os.path.exists(path_to_file):
        logger.error(f"File does not exist: {path_to_file}")
        return

    # 1. Удаляем расширенные атрибуты macOS (если применимо)
    try:
        # Проверяем, что файловая система поддерживает xattr
        if os.path.ismount('/Volumes/Backup_2025_photo'):
            subprocess.run(['xattr', '-c', path_to_file], check=True)
            logger.info("Extended attributes removed")
    except Exception as e:
        logger.warning(f"xattr warning: {str(e)}")

    # 2. Устанавливаем временные права на запись
    try:
        os.chmod(path_to_file, 0o766)  # rwxrw-rw-
        logger.info("Permissions updated for write access")
    except Exception as e:
        logger.error(f"Permission change error: {e}")
        return

    # 3. Записываем метаданные с правильным экранированием
    try:
        with exiftool.ExifToolHelper() as et:
            # Формируем параметры с экранированием пробелов
            params = [
                "-P",
                "-overwrite_original",
                "-E",
                "-ec",
                "-charset", "iptc=UTF-8"
            ]

            et.set_tags(
                [path_to_file],
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
                params=params
            )
        logger.success("Metadata updated successfully")
    except Exception as e:
        logger.error(f"ExifTool error: {e}")
        return

    # 4. Восстанавливаем исходные права
    try:
        os.chmod(path_to_file, 0o706)  # rwx---rw-
        logger.info("Original permissions restored")
    except Exception as e:
        logger.error(f"Permission restore error: {e}")


if __name__ == '__main__':
    # Используем сырую строку и явно задаем путь
    raw_path = r'/Volumes/Backup_2025_photo/2025_originals/05_May/20250519_Юридический  форум/20250519PEV_3721.NEF'

    change_color_class(
        raw_path,
        'KMO_204282_00034',
        '18.06.2025 Россия, Санкт-Петербург  XXVIII Петербургский международный экономический форум (ПМЭФ) 2025 в конгрессно-выставочном центре "Экспофорум". Фигура робота-пчелы на стенде Башкортостана.',
        "Red"
    )
