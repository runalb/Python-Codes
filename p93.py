class customer:
    def __init__(self,a,b,c,d,e):
        self.c1=a
        self.c2 = b
        self.c3 = c
        self.c4 = d
        self.c5 = e

    def totalbill(self):
        self.tbill=(self.c1+self.c2+self.c3+self.c4+self.c5)

    def gst(self):
        self.tgst=((self.tbill*10/100)+self.tbill)

    def disp(self):
        print("Total bill:",self.tbill)
        print("Total bill with GST:",self.tgst)

if __name__ == '__main__':
    c1=customer(10,10,10,10,10)
    c2=customer(10,40,10,10,10)
    c3=customer(10,30,10,10,10)
    c4=customer(10,20,10,10,10)
    c5=customer(10,90,10,10,10)

    c1.totalbill()
    c2.totalbill()
    c3.totalbill()
    c4.totalbill()
    c5.totalbill()

    c1.gst()
    c2.gst()
    c3.gst()
    c4.gst()
    c5.gst()

    c1.disp()
    c2.disp()
    c3.disp()
    c4.disp()
    c5.disp()
