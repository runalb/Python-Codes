a=int(input("Enter no: "))
l=a%10
print("last digit:", l)
while(a>=10):
    a=a//10
print("first: ",a)
print("addition: ",a+l)
