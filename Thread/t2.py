import threading

def disp():
    print("disp method")

t1=threading.Thread(target=disp)
t1.start()