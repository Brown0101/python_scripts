import openpyxl
import os

# Setting up to use a relative path instead of a full path.
dirpath = os.path.dirname(__file__)  # Get the directory path.
filename = os.path.join(dirpath, "Employees.xlsx")  # Add path to filename location

# Lets work with our workbook.
workbook = openpyxl.load_workbook(filename)
print(workbook.properties)  # Returns basic information about the workbook
print(workbook.sheetnames)  # Display all workbook sheet names

# Activate workbook.
workbook.active
sheet = workbook["EmployeeData"]  # Sets the variable to the workbook EmployeeData
workbook.create_sheet("TestSheet")  # Creates a new worksheet
workbook.save(filename)  # Saves the workbook or you can save a new workbook
workbook.remove(sheet)  # Deletes the sheet.

print(sheet.title) # Returns the worksheet's title
print(sheet.active_cell)  # Returns the active cell
print(sheet.dimensions)  # Returns all cell dimensions being used.
print(sheet.sheet_format)  # Get parameters of a sheet
print(sheet.sheet_properties)  # Returns other parameters of the sheet.
print(sheet.sheet_state)  # Returns if the sheet is visible or hidden.
print(sheet.sheet_view)  # Returns more parameters on the sheet.

print(sheet.max_row)  # Returns the number of rows used in the sheet.
print(sheet.max_column)  # Returns the number of columns used in the sheet.

# Return all rows as tuples
for i in sheet.values:
    print(i)