class Student:
    def __init__(self,i,n):
        self.sid=i
        self.name=n

    def disp(self):
        print(self.sid)
        print(self.name)

if __name__ == '__main__':
    S1=Student(1,"name1")
    S2=Student(2,"name2")
    S1.disp()
    S2.disp()