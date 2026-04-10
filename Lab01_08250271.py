# Student Information Management System
# Create an empty list to store student names as this will help us keep a simple collection of all students
students_list = []

# Create an empty dictionary to store student details
# Key = student name(each students name will be key), Value = dictionary (age and grade)
students_dict = {}

# Start an infinite loop so the program keeps running until user exits
while True:

    # Display the menu options to the user
    print("Student Management System")
    print("1. Add Student") #option to add new student
    print("2. Search Student") #option to find student details
    print("3. Remove Student") #option to delete a student
    print("4. Exit") #option to terminate program

    # Take input from user choice
    choice = input("Enter your choice: ")

    # OPTION 1: ADD STUDENT
    if choice == "1":
        # Ask the user to enter student details
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        grade = input("Enter student grade: ")

        # Add students name to the list
        #this keeps track of all student name separately
        students_list.append(name)
           
        #store the students full information in dictionary
        #the name acts as a unique key
        #age and grade are stored as values inside another dictionary
        # Add student details to dictionary
        students_dict[name] = {"age": age, "grade": grade}

        # confirm that the student has been added
        print("Student added successfully!")

        # print out all students record after adding
        print("Current Student Records:")

        # and loop through dictionary and then print each students data
        for key, value in students_dict.items():
            #the key in here represents student name
            #and the value is another dictionary containing age and grade of students
            print(f"Name: {key}, Age: {value['age']}, Grade: {value['grade']}")

    # OPTION 2: SEARCH STUDENT
    elif choice == "2":
        # here ask the user to enter the name of the student inorder search
        name = input("Enter student name to search: ")

        # then check if the student exists in the dictionary
        if name in students_dict:
            # If the student is found then display confirmation message
            print("Student Found!")

            # then retrieve and display the students details from dictionary
            print(f"Name: {name}")
            print(f"Age: {students_dict[name]['age']}")
            print(f"Grade: {students_dict[name]['grade']}")
        else:
            # and if student is not found, inform the user
            print("Student not found!")

    # OPTION 3: REMOVE STUDENT
    elif choice == "3":
        # Ask the user to enter the name of the student to remove
        name = input("Enter student name to remove: ")

        # Check if the student exists before attempting removal
        if name in students_dict:
           # Remove student data from dictionary
           # This deletes the key and its associated values
            del students_dict[name]

           # Also remove the student name from the list
            students_list.remove(name)

            # Confirm successful deletion
            print("Student removed successfully!")
        else:
            # If the student does not exist, display the message
            print("Student not found!")

    # OPTION 4: EXIT PROGRAM
    elif choice == "4":
        #show exit message
        print("Exiting program...")
        break  # then stop the loop and end program.

    # INVALID INPUT
    else:
        #If then user enters anything other than 1–4 then 
        print("Invalid choice! Please try again.")