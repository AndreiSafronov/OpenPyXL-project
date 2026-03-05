import openpyxl


def example():
    filename="test.xlsx"
    book1=openpyxl.load_workbook(filename)
    sheet= book1.worksheets[0]
    # sheet.insert_cols(1)
    # sheet.insert_rows(0)
    sheet["A1"].value="ФИО"
    sheet["B1"].value="Адрес"
    sheet["C1"].value="Город"
    sheet["D1"].value="Статус"
    # sheet.delete_rows(2)
    book1.save("test1.xlsx")

