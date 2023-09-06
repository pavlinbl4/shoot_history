from openpyxl import load_workbook
from openpyxl.styles import Font


def write_rename_voc(path_to_file, image_info, shoot_id):
    wb = load_workbook(path_to_file)
    ws = wb.create_sheet(shoot_id)
    ws.column_dimensions['A'].width = 50  # задаю шрину колонки
    ws.column_dimensions['B'].width = 50  # задаю шрину колонки
    ws.column_dimensions['C'].width = 40  # задаю шрину колонки
    ws.cell(row=1, column=1).value = "KSP name"
    ws.cell(row=1, column=2).value = "original file name"
    ws.cell(row=1, column=3).value = "published"
    last_line = ws.max_row
    for k in image_info:
        last_line += 1
        ws.cell(row=last_line, column=1).value = k
        ws.cell(row=last_line, column=2).value = image_info[k][0]
        if len(image_info[k]) == 2:
            ws.cell(row=last_line, column=3).value = image_info[k][1]
            ws.cell(row=last_line, column=1).font = Font(color="FF0000")
            ws.cell(row=last_line, column=2).font = Font(color="FF0000")
            ws.cell(row=last_line, column=3).font = Font(color="FF0000")
    wb.save(path_to_file)
