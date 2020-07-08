class A:
    def __init__(self):
        print("Count from A")

class B(A):
    pass

if __name__ == '__main__':
    obj=B()