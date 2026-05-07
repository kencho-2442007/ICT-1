# Search Operation Program

# Step 1: Create a file and store student details
file = open("students.txt", "w")

file.write("08250271 kencho\n")
file.write("08250272 sonam\n")
file.write("08250273 chundu\n")
file.write("08250273 Dema\n")
file.write("08250274 Tshagay\n")

file.close()
print("students.txt file created successfully!")

# Step 2: Read the file
file = open("students.txt", "r")

print("\nStudent Records:")
print(file.read())

file.close()

# Step 3: Ask user to input a student name
search_name = input("Enter student name to search: ")

# Step 4: Check whether the name exists or not
file = open("students.txt", "r")

found = False

for line in file:
    if search_name.lower() in line.lower():
        found = True
        break

file.close()

# Step 5: Display result

if found:
    print(search_name, "exists in the file.")
else:
    print(search_name, "does not exist in the file.")