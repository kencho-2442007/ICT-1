appendFile=open("hello.txt", "a")
appendFile.write("\n\nDon't froget to smile today!")
appendFile.close()

with open("hello.txt", "r") as f:
    contents=f.read()
    print(contents)