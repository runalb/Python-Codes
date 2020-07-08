no=int(input("Enter no: "))

while(no>0):
    temp=no%10
    if(temp%2==0):
        print("even no: ", temp)
    else:
        print("odd no: ", temp)
    no=no//10