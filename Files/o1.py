x=int(input("Enter needed rate: "))
rp=int(input("Enter required rate per threds: "))

x1=(x//rp)
print("Total threds: ",x1)

tot=rp*x1
print("Total amount of rates for",x1,"threads =",tot)

rem=(x-tot)
print("Reaming rate amount: ",rem)





