class runal:
    p=200
    r=108
    n=2

    def Si(self):
        self.Si=(self.p*self.r*self.n/100)

    def Ci(self):
        self.Si=self.p*((1+self.r/100)**self.n)

    def disp(self):
        print(self.Si)
        print(self.Si)

if __name__ == '__main__':
    obj=runal()
    obj.Si()
    obj.Ci()
    obj.disp()