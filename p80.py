fp=open("D:/Programing Language/Internship_Phython/Files/file1.txt","r")
temp1=fp.read()
print("File1 copied")
fp.close()


fp=open("D:/Programing Language/Internship_Phython/Files/file2.txt","r")
temp2=fp.read()
print("File2 copied")
fp.close()

fp=open("D:/Programing Language/Internship_Phython/Files/file3.txt","a")
fp.write(temp1)
fp.write(temp2)
print("File3 created with content of File-1&2")
fp.close()
