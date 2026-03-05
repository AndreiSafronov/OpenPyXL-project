import openpyxl
from openpyxl.chart import LineChart

def example():
    filename="test_styled.xlsx"
    book=openpyxl.load_workbook(filename)
    sheet=book.active
    chart=LineChart()
    
    chart.add_data("Преподаватели!D2:D22")
    book.save("test3.xlsx")