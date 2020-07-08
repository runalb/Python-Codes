from tkinter import *
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

        fp=open("D://Programing Language//Internship_Phython//Files//t1.txt","r")
        self.uid_file=fp.read()
        fp.close()
        fp = open("D://Programing Language//Internship_Phython//Files//t2.txt", "r")
        self.psw_file = fp.read()
        fp.close()

        if(self.u==self.uid_file   and self.p==self.psw_file):
            print("Login Successful")
        else:
            print("Invild")


top=Tk()
obj=signup(top)
top.mainloop()
