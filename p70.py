#pal or not
def pal(no):
    rem=0
    rev=0
    org=no
    while(no>0):
        rem=no%10
        rev=rev*10+rem
        no=no//10
    if(org==rev):
        print("pal")

    else:
        print("not pal")

#arm or not

no=int(input("Enter No: "))

pal(no)
