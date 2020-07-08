class Cal:
    a=10
    b=20
    def add(self):
        print(self.a+self.b)

    def sub(self):
        print(self.a - self.b)

    def mul(self):
        print(self.a * self.b)

    def div(self):
        print(self.a / self.b)


if __name__ == '__main__':
    obj=Cal()
    obj.add()
    obj.sub()
    obj.mul()
    obj.div()