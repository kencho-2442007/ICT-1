# Initialize empty list and dictionary
students_list = []
students_dict = {}

# Input student information
name = input("Enter student name: ")
age = input("Enter student age: ")
grade = input("Enter student grade: ")

# Store in list and dictionary
students_list.append(name)
students_dict[name] = {"age": age, "grade": grade}

# Success message
print("Student information added successfully!")

# Display dictionary items
print("\nStudent Details:")
for key, value in students_dict.items():
    print("Name:", key)
    print("Age:", value["age"])
    print("Grade:", value["grade"])

# Search for a student by name

search_name = input("Enter student name to search: ")

if search_name in students_dict:
    print("Student Found!")
    print("Name:", search_name)
    print("Age:", students_dict[search_name]["age"])
    print("Grade:", students_dict[search_name]["grade"])
else:
    print("Student not found!")

# Remove a student by name

remove_name = input("Enter student name to remove: ")

if remove_name in students_dict:
    students_list.remove(remove_name)
    del students_dict[remove_name]
    print("Student removed successfully!")
else:
    print("Student not found!")