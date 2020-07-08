fp=open("D:/Programing Language/Internship_Phython/Files/file3.txt","r")
temp=fp.read()
print(temp)
str="a,e,i,o,u,A,E,I,O,U"
counter=0
for x in temp:
    if (x in str):
        counter=counter+1
print("No of vovels: ",counter)
fp.close()