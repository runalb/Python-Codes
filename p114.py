from tkinter import *
from xlwt import *

class signup(Frame):
    def __init__(self,m):
        super().__init__(m)
        self.l1=Label(text="UID")
        self.l2=Label(text="PSW")
        self.l3=Label(text="Cont")
        self.l4=Label(text="Mail id")
        top.geometry("400x400")
        self.e1=Entry()
        self.e2 = Entry()
        self.e3 = Entry()
        self.e4 = Entry()
        self.b1=Button(text="Submit",command=self.disp)
        self.l1.grid(row=0,column=0)
        self.l2.grid(row=1, column=0)
        self.l3.grid(row=2, column=0)
        self.l4.grid(row=3, column=0)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.e4.grid(row=3, column=1)
        self.b1.grid(row=4, column=1)

    def disp(self):
        self.u=self.e1.get()
        self.p = self.e2.get()
        self.c = self.e3.get()
        self.em = self.e4.get()

        wb = Workbook()
        s1 = wb.add_sheet("first.xls")
        s1.write(0, 0,self.u)
        s1.write(0, 1,self.p)
        s1.write(0,2,self.c)
        s1.write(0,3,self.em)
        wb.save("D:\\Programing Language\\Internship_Phython\\Files\\f2.xls")
        print("Data Saved........")


top=Tk()
obj=signup(top)
top.mainloop()
