#Non-Parametersied Constructor
class demo:
    def __init__(self):
        print("hi from non-para")

if __name__ == '__main__':
    o1=demo()
    o1=demo()

print()

#Parametersied Constructor

class demo:
    def __init__(self,a,b):
        print("hi fom para constructor")


if __name__ == '__main__':
    o1 = demo(20,23)
    o1 = demo(39,98)
