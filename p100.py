#DATA Hiding

class demo:
    def __init__(self):
        self.__temp=20

if __name__ == '__main__':
    obj=demo()
    print(obj.temp)