import pandas as pd

class excelDetails:
    def __init__(self):
        pass  

    def compare_excel_files(self, file1, file2):
        # Load the Excel files into pandas DataFrames
        try:
            xl1 = pd.ExcelFile(file1)
            xl2 = pd.ExcelFile(file2)
        except Exception as e:
            print(f"Error reading Excel files: {e}")
            return False
        
        # Compare the sheet names
        if xl1.sheet_names != xl2.sheet_names:
            print("Sheet names do not match.")
            return False

        # Compare the contents of each sheet
        for sheet in xl1.sheet_names:
            df1 = xl1.parse(sheet)
            df2 = xl2.parse(sheet)

            # Compare the shape of the DataFrames (rows, columns)
            if df1.shape != df2.shape:
                print(f"Sheet '{sheet}' has different shape (rows, columns).")
                return False

            # Compare the actual cell data (values)
            if not df1.equals(df2):
                print(f"Sheet '{sheet}' has different data.")
                return False

        # If all checks passed, the files are considered identical
        return True
