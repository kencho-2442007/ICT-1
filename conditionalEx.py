Marks1=float(input("Enter the marks of first subject: "))
Marks2=float(input("Enter the marks of second subject: "))
Marks3=float(input("Enter the marks of third subject: "))
average=(Marks1+Marks2+Marks3)/3
if(average>=90 and Marks1>=50 and Marks2>=50 and Marks3>=50): 
    print("Grade:A")
elif(average>=80 and Marks1>=50 and Marks2>=50 and Marks3>=50):
    print("Grade:B")   
elif(average>=70 and Marks1>=50 and Marks2>=50 and Marks3>=50):
    print("Grade:C")   
elif(average>=60 and Marks1>=50 and Marks2>=50 and Marks3>=50):
    print("Grade:D")   
elif(average>=50 and Marks1>=50 and Marks2>=50 and Marks3>=50):
    print("Grade:E")  
else:
    print("You need to work harder.") 