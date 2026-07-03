from pathlib import Path
import openpyxl

class ExcelReader:
    @staticmethod
    def read(file_name, sheet_name):
        print("excel file:",Path(__file__))
        excel_path = (Path(__file__).parent.parent / "data" / file_name)
        workbook = openpyxl.load_workbook(excel_path)
        sheet = workbook[sheet_name]
        data = []
        headers = []

        for cell in sheet[1]:
            headers.append(cell.value)

        for row in sheet.iter_rows(min_row=2, values_only=True):
            row_data = {}
            for key, value in zip(headers, row):
                row_data[key] = value
            data.append(row_data)
        return data