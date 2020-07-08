class A:
    def __init__(self):
        print("Count from A")

    def disp(self):
        print("Display from A")

class B(A):
    def __init__(self):
        super().disp()
        print("count from B")

if __name__ == '__main__':
    obj=B()