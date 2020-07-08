def factorial(i):
    fact=1
    for i in range(1,i+1):
        fact=fact*i
    print("factorial is",fact)

a=int(input("Enter No: "))

factorial(a)