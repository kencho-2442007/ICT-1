name=input("enter your name:")
greet =lambda x: print("hello", x)
greet(name)

#condition checking
even_odd= lambda x: "even" if x%2 ==0 else "odd"
num= int(input("enter a number: "))
print(even_odd(num))

#return multiple result
arith= lambda x, y: (x+y, x-y, x*y, x/y)
num1= int(input("enter first number:"))
num2= int(input("enter second number:"))
print(arith(num1,num2))

#filter
mylist= [1,2,3,4,5,6]
even= filter(lambda x: x%2 ==0, mylist)
print(list(even))

#map
mylist= [1,2,3,4]
double= map (lambda x: x*2, mylist)
#print(list(double))

#convert result of double to my list
mynewlist= (list(double))
print(mynewlist)
decision = map (lambda x: x/2, mynewlist)
print(list(decision))