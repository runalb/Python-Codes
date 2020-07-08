try:
    try:
        try:
            a=10/2
            fp=open("D:\\Programing Language\\Internship_Phython\\Files\\p106\\f3.txt","r")
            temp=fp.read()
            print(temp)
            fp.close()
        except FileNotFoundError:
         print("file h")
    except IndexError:
        print("file related h")
except KeyError:
    print("default")

