import pandas as pd

def get_sheet(excel_path, sheet):
    sheet = pd.read_excel(excel_path, sheet_name=sheet)
    return sheet

def get_total_rows(excel_path, sheet):
    sheet = get_sheet(excel_path, sheet)
    rows = sheet.shape[0]
    return rows

def read_excel_data(excel_path, sheet, row_number, column_name):
    sheet = get_sheet(excel_path, sheet)
    data = sheet.loc[row_number, column_name]
    return data

def write_to_excel(excel_path, sheetname, row_number, column_name, 
                   value_to_enter):
    sheet = get_sheet(excel_path, sheetname)
    sheet.loc[row_number, column_name] = value_to_enter
    write = pd.ExcelWriter(excel_path)
    sheet.to_excel(write, sheet_name=sheetname, index=False)
    write.save()