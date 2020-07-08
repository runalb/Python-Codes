class A:
    def __init__(self):
        print("Count from A")

class B(A):
    def __init__(self):
        super().__init__()
        print("count from B")

if __name__ == '__main__':
    obj=B()