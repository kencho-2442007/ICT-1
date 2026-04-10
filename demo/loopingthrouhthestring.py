name=input("Enter your name: ")
for i in name:
    print(i)

li=["Python Programming", "Python fundamentaks", "Python Interview Question"]
for x in li:
    print(x)

lenli=len(li) 
for x in range(lenli):
    print(li[x])

tupleli=tuple(li)
for x in range(len(tupleli)):
    print(tupleli[x])

setli=set(li)
for x in range(len(setli)):
    print(x)
    
tup=("John Smith","Jane Doe","Alice Johnson")
for x in tup:
    print(x)

set1={10,20,30}
for x in set1:
    print(x)

BookDetails=dict({"python programming": "john smith", "Python Fundamentals": "alice johnson", "python interview questions":"john doe"})
for keys in BookDetails:
    print(keys, BookDetails[keys])


