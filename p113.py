from xlwt import *

wb=Workbook()
s1=wb.add_sheet("first.xls")
s1.write(0,0,"Runal")
s1.write(0,1,"Runal2")
wb.save("D:\\Programing Language\\Internship_Phython\\Files\\f1.xls")
print("Data Saved........")