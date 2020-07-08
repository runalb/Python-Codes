no=int(input("Enter data: "))
sum=0
while(no>0):
    temp=no%10
    sum=sum+1
    no=no//10
print(sum)
