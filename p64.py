def calculate(a,b,op):
    if(op=="+"):
        c=a+b
        print("Add: ",c)

    elif(op == "-"):
        c = a - b
        print("Sub: ", c)

    elif (op == "*"):
        c = a * b
        print("Mul: ", c)

    else:
        c = a / b
        print("Div: ", c)


a=int(input("Enter value: "))
b=int(input("Enter value: "))
op=(input("Enter Operator: "))

calculate(a,b,op)