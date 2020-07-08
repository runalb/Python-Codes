def game(a,b):
    res1="1st Player Won!!!.."
    res2="2nd Player Won!!!.."

    ########   1st    ###########

    if (a=="Rock" and b=="Scissor"):
        print(res1)

    elif (a=="Rock" and b=="Paper"):
        print(res1)

    elif (a=="Rock" and b=="Rock"):
        print(res2)

    ########   2nd    ###########

    elif (a=="Paper" and b=="Scissor"):
        print(res1)

    elif (a=="Paper" and b=="Rock"):
        print("2st Player Won!!!..")

    elif (a=="Paper" and b=="Paper"):
        print("2st Player Won!!!..")

    ########   3RD    ###########

    elif (a=="Scissor" and b=="Scissor"):
        print("2st Player Won!!!..")

    elif (a=="Scissor" and b=="Rock"):
        print("2st Player Won!!!..")

    elif (a=="Scissor" and b=="Paper"):
        print("2st Player Won!!!..")

    else:
        print("Wrong Input")



print("Enter Rock, Papper, Scissor")
p1=input("1st Player: ")
p2=input("2st Player: ")

game(p1,p2)

