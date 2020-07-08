def prime(no):
    status = 0
    temp = no//2
    for x in range(2,no):
        if (no%x==0):
            status=1
    if (status == 1):
        print("Prime")
    else:
        print("Not")

no=int(input("Enter No: "))
prime(no)