class empolyee:
    def __init__(self,s,t,d):
        self.sal=s
        self.ta=t
        self.da=d

    def pak(self):
        self.pack=(self.sal+self.ta+self.da)*12

    def disp(self):
        print(self.pack)

    def max(self):
        if(e1.pack>e2.pack>e3.pack):
            print("e1 max")

if __name__ == '__main__':
    e1=empolyee(20,40,0)
    e2=empolyee(50,0,23)
    e3=empolyee(100,200,400)
    e1.pak()
    e2.pak()
    e3.pak()
    e1.disp()
    e2.disp()
    e3.disp()
    



