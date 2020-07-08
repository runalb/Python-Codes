from threading import *
import time

class A(Thread):
    def run(self):
        for x in range(50):
            print("Hi1")
            time.sleep(2)


if __name__ == '__main__':
    t1=A()
    t1.start()
