newFile = open("newFile.txt","w")
print(newFile)
newFile.write("this is a new file created by python.")
newFile.close()

fileOverwrite= open("newFile.txt","w")
fileOverwrite.write("the contents of the newFile is now changed.")
fileOverwrite.close()

