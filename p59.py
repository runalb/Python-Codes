l=[10,20,30,40,50,60]
print(l)
print()

#alternate swap position ele 1to2 & 3to4 and so on
for x in range(0,len(l)-1,2):
    temp=l[x]
    l[x]=l[x+1]
    l[x+1]=temp
print("Alternate Swap ")
print(l)