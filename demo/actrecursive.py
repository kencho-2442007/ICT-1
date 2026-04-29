def fun1(x,y):
    #base condition
    if (x)==0:
        return y
    #recursive call
    else:
        return fun1(x-1, x+y)
x=int(input("Enter a number:"))
y=int(input("Enter a number:"))

result=fun1(x,y)
print("result:", result)