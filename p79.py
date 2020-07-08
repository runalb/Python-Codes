
fp=open("D:/Programing Language/Internship_Phython/Files/file1.txt","r")
temp=fp.read()
print("File is created",temp)
fp.close()


fp=open("D:/Programing Language/Internship_Phython/Files/file2.txt","w")
fp.write(temp)
print("File copied")
fp.close()
