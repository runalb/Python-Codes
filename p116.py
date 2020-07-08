from tkinter import *
class signup(Frame):
    def __init__(self,m):
        super().__init__(m)
        self.l00=Label(text="List Of ITEM")
        self.l10=Label(text="Laptop")
        self.l20=Label(text="Mouse")
        self.l30=Label(text="Keybord")
        self.l40=Label(text="Charger")
        self.l50=Label(text="RAM:")
        self.l60=Label(text="Total Price:")
        self.l70=Label(text="Total GST:")

        self.l01=Label(text="Price")
        self.l02=Label(text="GST")

        top.geometry("400x400")
        self.b1 = Button(text="Submit", command=self.disp)
        self.e11 = Entry()
        self.e21 = Entry()
        self.e31 = Entry()
        self.e41 = Entry()
        self.e51 = Entry()
        self.e61 = Entry()
        self.e71 = Entry()
        self.e12= Entry()
        self.e22 = Entry()
        self.e32 = Entry()
        self.e42 = Entry()
        self.e52 = Entry()


    ############ For label
        self.l00.grid(row=0,column=0)
        self.l10.grid(row=1, column=0)
        self.l20.grid(row=2,column=0)
        self.l30.grid(row=3, column=0)
        self.l40.grid(row=4, column=0)
        self.l50.grid(row=5, column=0)
        self.l60.grid(row=6, column=0)
        self.l70.grid(row=7, column=0)

        self.l01.grid(row=0, column=1)
        self.l02.grid(row=0, column=2)

    ############# for entry
        self.e11.grid(row=1,column=1)
        self.e21.grid(row=2,column=1)
        self.e31.grid(row=3,column=1)
        self.e41.grid(row=4,column=1)
        self.e51.grid(row=5,column=1)
        self.e61.grid(row=6,column=1)
        self.e71.grid(row=7,column=1)

        self.e12.grid(row=1, column=2)
        self.e22.grid(row=2, column=2)
        self.e32.grid(row=3, column=2)
        self.e42.grid(row=4, column=2)
        self.e52.grid(row=5, column=2)

        self.b1.grid(row=8,column=1)

    def cal(self):


    def disp(self):
        self.d1 = self.e11.get()
        self.d2 = self.e21.get()
        self.d3 = self.e31.get()
        self.d4 = self.e41.get()
        self.d5 = self.e51.get()
        self.d6 = self.e61.get()
        self.d7 = self.e71.get()
        self.dd1 = self.e12.get()
        self.dd2 = self.e22.get()
        self.dd3 = self.e32.get()
        self.dd4 = self.e42.get()
        self.dd5 = self.e52.get()



        self.totalbill=self.d1+self.d2+self.d3+self.d4+self.d5
        print(self.totalbill)

        print()
        print(self.d1)
        print(self.d2)
        print(self.d3)
        print(self.d4)
        print(self.d5)
        print(self.d6)
        print(self.d7)

        print(self.dd1)
        print(self.dd2)
        print(self.dd3)
        print(self.dd4)
        print(self.dd5)




top=Tk()
obj=signup(top)
top.mainloop()
