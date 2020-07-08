a1=input("Product: ")
a2=int(input("Value: "))
a3=int(input("GST: "))

b1=input("Product: ")
b2=int(input("Value: "))
b3=int(input("GST: "))

c1=input("Product: ")
c2=int(input("Value: "))
c3=int(input("GST: "))

d1=input("Product: ")
d2=int(input("Value: "))
d3=int(input("GST: "))

e1=input("Product:")
e2=int(input("Value: "))
e3=int(input("GST: "))

totalprice=a2+b2+c2+d2+e2
print("Total Price: ",totalprice)

totalgst=a3+b3+c3+d3+e3
print("Total GST: ",totalgst)

total=totalprice+totalgst
print("Total Bill: ",total)