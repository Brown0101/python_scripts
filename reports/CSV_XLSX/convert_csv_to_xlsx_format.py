import sys
import csv
import os
import xlsxwriter

# Get file name without extension
file_name = os.path.splitext(os.path.basename(r"<file_location.csv>"))[0] + '.xlsx'
# if we read f.csv we will write f.xlsx
wb = xlsxwriter.Workbook("<filename_you_choose.xlsx")
ws = wb.add_worksheet(file_name)    # your worksheet title here
# add background format color
format1 = wb.add_format({'bg_color' : '#000033', 'bold': True, 'font_size' : 16, 'font_color': 'white', 'valign': 'vcenter'}) 
format2 = wb.add_format({'bg_color' : '#F0F0F0'})

# use this to determine the format to be used.
flag =  'format2'

with open(r'<file_location.csv>','r') as csvfile:
    table = csv.reader(csvfile)
    i = 0
    # write each row from the csv file as text into the excel file
    # this may be adjusted to use 'excel types' explicitly (see xlsxwriter doc)
    for row in table:
        if '<Spreadsheet_Title_Name>' in row:
            ws.merge_range('A1:H1', "", format1)
            ws.write_row(i, 0, row, format1)
        elif not row:
            continue
        else:
            if flag == 'format2':
                ws.write_row(i, 0, row, format2)
                flag = ''
            else:
                ws.write_row(i, 0, row)
                flag = 'format2'
        i += 1
wb.close()
