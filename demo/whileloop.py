no_of_students=int(input("Enter the number of the students: "))
i=1
student_names={}
while i<=no_of_students:
    name=input("Enter the name of the students: " )
    print("The name of the student {} is {}". format(i, name))
    i+=1
    student_names[i]=name
print(student_names)
while True:
    print("this is an infinite loop. press Ctrl + C to stop it.")

