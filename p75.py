def vaild(a,b):
    userid="Runal"
    password="123"
    if (a==userid and b==password):
        return "Valid"
    else:
        return "invalid"

def disp(r):
    print(r)

a=input("Enter User Id: ")
b=input("Enter Password: ")

res=vaild(a,b)
disp(res)