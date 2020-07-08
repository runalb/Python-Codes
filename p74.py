def cal(a,b,c):
    if(c=="+"):
        r=a+b
        return r
    elif(c=="-"):
        r=a-b
        return r
    elif(c=="/"):
        r=a/b
        return r
    elif (c == "*"):
        r=a*b
        return r
    elif(c=="//"):
        r=a//b
        return r
    elif(c=="%"):
        r=a%b
        return r
    elif(c=="**"):
        r=a**b
        return r

def disp(r):
    print(r)

a=int(input("Enter 1st value: "))
b=int(input("Enter 2nd value: "))
c=(input("Operator: "))

res=cal(a,b,c)

disp(res)