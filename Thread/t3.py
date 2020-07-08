from threading import *

class A(Thread):
    def run(self):
        for x in range(50):
            print("Hi1")

class B(Thread):
    def run(self):
        for x in range(100):
            print("Hi")

if __name__ == '__main__':
    t1=A()
    t2=B()
    t1.start()
    t2.start()