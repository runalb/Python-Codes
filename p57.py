l=[2,3,4,5,6,7,8,9,10]

for x in l:
    if(x%2!=0):
        i=l.index(x)
        l[i]=x*x*x
print(l)
