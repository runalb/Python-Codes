no=int(input("Enter Total no. of element: " ))
l=[]

for x in range(0,no):
    a=int(input("Enter NO: "))
    l.append(a)

print("Enterd list: ")
print(l)

#find max by logic
max=l[0]
for x in range(1,len(l)):
    if(l[x]>max):
        max=l[x]
print("max: ",max)

# Max by logic
min=l[0]
for x in range(1,len(l)):
    if(l[x]<min):
        min=l[x]
print("min",min)

#find index of
i=l.index(max)
print("max index: ",i)

# addd min-1 at max
l[i]=min-1

print(l)
