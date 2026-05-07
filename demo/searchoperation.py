file = open('Students.xlsx', 'w')
file.write("Name, ID\n")
file.write("kencho, 001\n")
file.write("sonam, 002\n")
file.write("pema, 003\n")
file.write("tshering, 004\n")
file.write("tshagay, 005\n")
file.close()
file = open('Students.xlsx', 'r')
students = file.read()
print(students)
file.close()
searchN = input("Enter a name to search: ")
found = False
with open('Students.xlsx', 'r') as file:
    for student in file:
        if searchN.lower() in student.lower():
            print(student)
            found = True
            break
if not found:
    print("Name not found in the file.")
print()