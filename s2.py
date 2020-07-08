l=[2,3,4,5,6,7,8]

print(l)

for x in l:
    if(x%2==0):
        i=l.index(x)
        l[i]=x**2
print(l)

print()

'''
for x in l:
    if(x%2!=0):
        i=l.index(x)
        l[i]=x*x*x
print(l)
'''