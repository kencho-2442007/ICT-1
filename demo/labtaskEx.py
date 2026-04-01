student_name = input("Enter student name: ")
days_borrowed = int(input("Enter number of days the book was borrowed: "))
days_late = int(input("Enter number of days late (0 if returned on time): "))

# Initialize fine
fine = 0

# Calculate fine based on rules
if days_late == 0:
    fine = 0
elif 1 <= days_late <= 5:
    fine = days_late * 5
elif 6 <= days_late <= 10:
    fine = days_late * 10
else:
    fine = days_late * 20

# Warning message
warning = ""
if days_borrowed > 30:
    warning = "Library privileges may be restricted"

# Display output
print("\n--- Library Fine Details ---")
print(f"Student Name : {student_name}")
print(f"Days Borrowed: {days_borrowed}")
print(f"Days Late    : {days_late}")
print(f"Total Fine   : Nu. {fine}")

if warning:
    print(f"Warning      : {warning}")

