l=[2,3,4,5,6]

print(l)

#find and replace even ele and make it square in list
for x in l:
    if(x%2==0):
        i=l.index(x)
        l[i]=x**3
print(l)

'''
#find and replace odd ele and make it cube
for x in l:
    if(x%2!=0):
        i=l.index(x)
        l[i]=x*x*x
print(l)
'''
