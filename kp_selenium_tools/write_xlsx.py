from pathlib import Path
from loguru import logger

import openpyxl
from openpyxl import load_workbook
from openpyxl.styles import Font


def write_rename_voc(path_to_file, image_info, shoot_id):
    # Create the file if it doesn't exist yet
    if not Path(path_to_file).is_file():
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "sheet_name"
        # set_column_widths(ws, columns_header_names)
        wb.save(path_to_file)

    wb = load_workbook(path_to_file)
    ws = wb.create_sheet(shoot_id)
    ws.column_dimensions['A'].width = 20  # задаю ширину колонки
    ws.column_dimensions['B'].width = 20  # задаю шрину колонки
    ws.column_dimensions['C'].width = 10  # задаю шрину колонки
    ws.column_dimensions['D'].width = 60  # задаю шрину колонки
    ws.cell(row=1, column=1).value = "KSP name"
    ws.cell(row=1, column=2).value = "original file name"
    ws.cell(row=1, column=3).value = "published"
    ws.cell(row=1, column=4).value = "caption"
    last_line = ws.max_row
    logger.info( f'{image_info = }')
    for k in image_info:
        logger.info(f'{k = }')
        last_line += 1
        ws.cell(row=last_line, column=1).value = k
        ws.cell(row=last_line, column=2).value = image_info[k][0]
        if len(image_info[k]) >= 2:
            ws.cell(row=last_line, column=3).value = image_info[k][1]
            ws.cell(row=last_line, column=4).value = image_info[k][2]
            ws.cell(row=last_line, column=1).font = Font(color="FF0000")
            ws.cell(row=last_line, column=2).font = Font(color="FF0000")
            ws.cell(row=last_line, column=3).font = Font(color="FF0000")
            ws.cell(row=last_line, column=4).font = Font(color="FF0000")
    wb.save(path_to_file)


if __name__ == '__main__':
    write_rename_voc(
        # "../tests/test_files/shoot_story.xlsx",
        '/Users/evgeniy/Documents/Kommersant/shoot_rename/shoot_story.xlsx',
        {'k':"image_info"},
        "KSP_018281")
