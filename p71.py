def fynosis(no):
    n1=0
    n2=1
    print(n1)
    print(n2)
    for x in range(3,no+1):
        n3=n1+n2
        print(n3)
        n1=n2
        n2=n3

no=int(input("Enter No: "))

fynosis(no)
