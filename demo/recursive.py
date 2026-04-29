#sum of natural numbers using recursion
def sum(n):

    if n==1: #base condition
        return 1
    
    else: #recursive call
        return n+sum(n-1)
    
n=int(input("Enter a number:"))
print("sum of numbers from 1 to", n ,"is:", sum(n))

#factorial of a number using recursion
def fact(n):
    #base condition
    if n==0:
        return 1
    #recursive call
    else:
        return n*fact(n-1)
print("factorial of 5:", fact(5))