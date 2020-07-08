class A:
    def __init__(self,p,r,n):
        self.a=p
        self.b = r
        self.c = n

    def SI(self):
        self.si=((self.a*self.b*self.c)/100)

    def disp(self):
        print(self.si)

class B(A):
    pass

if __name__ == '__main__':
    obj=B(100,20,400)
    obj.SI()
    obj.disp()