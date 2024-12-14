from pathlib import Path

import openpyxl
from openpyxl import load_workbook
from openpyxl.styles import Font, Alignment


def write_rename_voc(path_to_file, image_info, shoot_id):
    # Create the file if it doesn't exist yet
    if not Path(path_to_file).is_file():
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "sheet_name"
        # wb.save(path_to_file)

    wb = load_workbook(path_to_file)
    ws = wb.create_sheet(shoot_id)
    ws.column_dimensions['A'].width = 18  # задаю ширину колонки
    ws.column_dimensions['B'].width = 18  # задаю ширину колонки
    ws.column_dimensions['C'].width = 10  # задаю ширину колонки
    ws.column_dimensions['D'].width = 70  # задаю ширину колонки
    ws.cell(row=1, column=1).value = "KSP name"
    ws.cell(row=1, column=2).value = "original file name"
    ws.cell(row=1, column=3).value = "published"
    ws.cell(row=1, column=4).value = "caption"
    last_line = ws.max_row
    for k in image_info:
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
            ws.cell(row=last_line, column=4).alignment = Alignment(horizontal='center',
                                                                             vertical='center',
                                                                             wrap_text=True)
    wb.save(path_to_file)


if __name__ == '__main__':
    write_rename_voc(
        # "../tests/test_files/shoot_story.xlsx",
        '/Users/evgeniy/Documents/Kommersant/shoot_rename/shoot_story.xlsx',
        {'k':"image_info"},
        "KSP_018281")
