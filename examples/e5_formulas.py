import openpyxl


def example():
    filename="test.xlsx"
    book=openpyxl.load_workbook(filename)
    sheet=book.active
    sheet["D25"].value='=SUM(D1:D22)'
    book.save(filename="test2.xlsx")