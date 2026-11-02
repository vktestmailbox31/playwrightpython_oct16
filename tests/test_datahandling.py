import csv
import json
from pathlib import Path
from openpyxl import load_workbook
import pytest


@pytest.mark.dh
def test_jsonhandling():
    credentials_path = Path(__file__).resolve().parents[1] / "TestData" / "creds.json"
    with credentials_path.open(encoding="utf-8") as data:
        creds = json.load(data)
        print(creds)
        
        
@pytest.mark.dh
def test_csvhandling():
    credentials_path = Path(__file__).resolve().parents[1] / "TestData" / "credentials.csv"
    with credentials_path.open(encoding="utf-8", newline="") as data:
        creds = csv.DictReader(data)
        rows = list(creds)
        print(rows)
               
    
    
# pip install openpyxl
@pytest.mark.dh
def test_handlingExcel():
    workbook_path = Path(__file__).resolve().parents[1] / "TestData" / "sample_workbook.xlsx"
    workbook = load_workbook(workbook_path, read_only=True, data_only=True)
    try:
        sheet = workbook["vinay1"]
        rows = list(sheet.iter_rows(min_row=2, values_only=True))
    finally:
        workbook.close()

    for row in rows:
        print(row)


# @pytest.mark.dh
# def test_handlingExcelWrite():
#     workbook_path = Path(__file__).resolve().parents[1] / "TestData" / "sample_workbook.xlsx"
#     workbook = load_workbook(workbook_path)
#     sheetData = workbook["vinay1"]
#     sheetData["A4"] = "tripura"
#     sheetData.delete_rows(3, 4)
#     sheetData.append(["tripra123", "data123"])
#     workbook.save(workbook_path)
#     workbook.close()

@pytest.mark.dh
def test_handleexl():
    workbook = load_workbook("TestData\\sample_workbook.xlsx")
    sheetdata = workbook["vinay1"]
    l1  = []
    for i in sheetdata.iter_rows(min_row=2,values_only=True):
        l1.append(i)
    print(l1)    