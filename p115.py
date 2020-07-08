from tkinter import *
from xlrd import *

class signup(Frame):
    def __init__(self,m):
        super().__init__(m)
        self.l1=Label(text="UID")
        self.l2=Label(text="PSW")
        top.geometry("400x400")
        self.e1=Entry()
        self.e2 = Entry()
        self.b1=Button(text="Submit",command=self.disp)
        self.l1.grid(row=0,column=0)
        self.l2.grid(row=1, column=0)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.b1.grid(row=4, column=1)

    def disp(self):
        self.u=self.e1.get()
        self.p = self.e2.get()


        wb=open_workbook("D:\\Programing Language\\Internship_Phython\\Files\\f2.xls")
        sheet =wb.sheet_by_index(0)
        self.uid_file=sheet.cell_value(0,0)
        self.psw_file = sheet.cell_value(0,1)

        if(self.u==self.uid_file   and self.p==self.psw_file):
            print("Login Successful")
        else:
            print("Invild")


top=Tk()
obj=signup(top)
top.mainloop()
