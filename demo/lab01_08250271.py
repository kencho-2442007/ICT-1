# Student Information Management System
# Create an empty list to store student names as this will help us keep a simple collection of all students
students_list = []
# Create an empty dictionary to store student details
# Key = student name(each students name will be key), Value = dictionary (age and grade)
students_dict = {}

# add the student information
name = input("Enter student name: ")
age = input("Enter student age: ")
grade = input("Enter student grade: ")

# Add students name to the list and store the students full information in dictionary
#the name acts as a unique key and the age and grade are stored as values inside another dictionary
#Add student details to dictionary
students_list.append(name)
students_dict[name] = {"age": age, "grade": grade}

#confirm that the student has been added
print("Student information added successfully!")

# Display dictionary items
print("Student Details:")
for key, value in students_dict.items():
# #the key in here represents student name and the value is another dictionary containing age and grade of students
    print("Name:", key)
    print("Age:", value["age"])
    print("Grade:", value["grade"])

# Search for a student by name

search_name = input("Enter student name to search: ")#here enter the name of the student you want to search

if search_name in students_dict:#it will print out the message "student found!" if the student name and details are added
    print("Student Found!")
    print("Name:", search_name)
    print("Age:", students_dict[search_name]["age"])
    print("Grade:", students_dict[search_name]["grade"])
else:
    print("Student not found!") #it will print out the message as "Student not found!" if the student was not added and couldnt found

# Remove a student by name 

remove_name = input("Enter student name to remove: ") #enter the name of the student to remove the students detail

if remove_name in students_dict:
    students_list.remove(remove_name)
    del students_dict[remove_name]
    print("Student removed successfully!") # it will print out message "Student removed successfully!"if removed successfully
else:
    print("Student not found!") #it will print out the message "Student not found!" if the name you entered was wrong and couldnt be found in there