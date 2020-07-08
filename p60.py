l=[10,2,20,13,40,50]
for x in l:
    status=0
    temp=x//2
    for y in range(2,temp+1):
        if(x%y==0):
            status=1
    if(status==0):
        print("Prime")
    else:
        print("Not Prime")

