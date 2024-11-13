import pytest
from object.excel_details_object import excelDetails

class TestCompareExcelFiles:

    def test_compare_excel_identical(self):
        file_comparer = excelDetails()

        file1 = 'dataFile/sample1.xlsx'
        file2 = 'dataFile/sample1.xlsx'

        result = file_comparer.compare_excel_files(file1, file2)

        assert result is True, f"Excel files {file1} and {file2} are not identical. "

    def test_compare_excel_different(self):
        file_comparer = excelDetails()

        file1 = 'dataFile/sample1.xlsx'
        file2 = 'dataFile/sample2.xlsx'

        result = file_comparer.compare_excel_files(file1, file2)

        assert result is False, f"Excel files {file1} and {file2} are unexpectedly identical."
