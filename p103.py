class demo:
    def disp(self):
        print("non para")

    def disp(self,a):
        print("1 para")

    def disp(self,a,b):
        print("2 para")

class B(demo):
    pass

if __name__ == '__main__':
    obj=demo()
    obj.disp(10)