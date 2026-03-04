import openpyxl
from examples.data_faker import data_samples


def example(filename="report.xlsx"):
    book = openpyxl.Workbook()
    sheet = book.active

    sheet.append(["ФИО", "Адрес", "Дата рождения", "Город", "ID/Рейтинг"])

    for row in data_samples():
        sheet.append(row)

    book.save(filename)
    print(f"Файл {filename} успешно создан!")
