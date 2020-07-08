fp=open("D:/Programing Language/Internship_Phython/Files/file1.txt","r")
temp1=fp.read()
print("File1 copied:",temp1)
fp.close()


fp=open("D:/Programing Language/Internship_Phython/Files/file2.txt","r")
temp2=fp.read()
print("File2 copied:",temp2)
fp.close()

fp=open("D:/Programing Language/Internship_Phython/Files/file3.txt","w")
fp.write(temp1.upper())
fp.write(temp2.upper())
print("fp.close()File3 created with content of File-1&2")
