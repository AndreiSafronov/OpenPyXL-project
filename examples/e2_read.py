import openpyxl


def example():
    book1 = openpyxl.load_workbook(filename="test.xlsx")
    sheet1 = book1["Персонал"]
    sheet2 = book1["Студенты"]
    sheet3 = book1["Преподаватели"]
    # for row in sheet1.iter_rows():
    #     for cell in row:
    #         print(cell.value)
