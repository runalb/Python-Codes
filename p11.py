a1=input("Product: ")
a2=int(input("Value: "))
a3=(a2/100)*10
print("GST on",a1,"is",a3)
b1=input("Product: ")
b2=int(input("Value: "))
b3=(b2/100)*10
print("GST on",b1,"is",b3)
c1=input("Product: ")
c2=int(input("Value: "))
c3=(c2/100)*10
print("GST on",c1,"is",c3)
d1=input("Product: ")
d2=int(input("Value: "))
d3=(d2/100)*10
print("GST on",d1,"is",d3)
e1=input("Product:")
e2=int(input("Value: "))
e3=(e2/100)*10
print("GST on",e1,"is",e3)
totalprice=a2+b2+c2+d2+e2
print("Total Price: ",totalprice)
totalgst=a3+b3+c3+d3+e3
print("Total GST Amount: ",totalgst)
total=totalprice+totalgst
print("Total Bill Amount: ",total)
