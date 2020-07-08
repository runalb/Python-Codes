class demo:
    def __init__(self):
        self.__temp=20

    def setter(self):
        self.__temp=120

    def getter(self):
        print(self.__temp)
if __name__ == '__main__':
    obj=demo()
    obj.getter()
    obj.setter()
    obj.getter()