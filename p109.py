try:
    fp = open("D:\\Programing Language\\Internship_Phython\\Files\\p106\\f1.txt", "r")
    temp = fp.read()
    print(temp)
    fp.close()
except:
    try:
        fp = open("D:\\Programing Language\\Internship_Phython\\Files\\p106\\f3.txt","r")
        temp = fp.read()
        print(temp)
        fp.close()
    except:
        fp = open("D:\\Programing Language\\Internship_Phython\\Files\\p106\\f5.txt","r")
        temp = fp.read()
        print(temp)
        fp.close()
    else:
        fp = open("D:\\Programing Language\\Internship_Phython\\Files\\p106\\f4.txt", "r")
        temp = fp.read()
        print(temp)
        fp.close()
else:
    fp = open("D:\\Programing Language\\Internship_Phython\\Files\\p106\\f2.txt", "r")
    temp = fp.read()
    print(temp)
    fp.close()