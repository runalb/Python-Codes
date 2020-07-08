no=int(input("Enter Total no. of element: " ))
l=[]

for x in range(0,no):
    a=int(input("Enter NO: "))
    l.append(a)

print("Enterd list: ",l)

for x in l:
    if(x%2==0):
        print("Even: ",x)

for x in l:
    if(x%2!=0):
        print("odd: ",x)
