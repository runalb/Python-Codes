from threading import *

class Demo(Thread):
    def run(self):
        print("run method from demo")

if __name__ == '__main__':
    obj=Demo()
    obj.start()