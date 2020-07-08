try:
    a=10/25
    fp=open("D:\\Programing Language\\Internship_Phython\\Files\\p106\\f3.txt","r")
    temp=fp.read()
    print(temp)
    fp.close()
except ArithmeticError:
    print("Art h")
except FileExistsError:
    print("file h")
except :
    print("default")

