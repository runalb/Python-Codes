def rev(no):
    rem=0
    rev=0
    org=no
    while(no>0):
        rem=no%10
        rev=rev*10+rem
        no=no//10
    print(rev)

no=int(input("Enter No: "))

rev(no)