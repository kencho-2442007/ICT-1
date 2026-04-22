 #Inputting marks for 3 subjects from the user
# Using float() to allow decimal marks if necessary
mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))


# Function to calculate the total of three marks
def calculate_total(m1, m2, m3):
    return m1+m2+m3
print("The total of m1, m2 and m3 is:",calculate_total(mark1,mark2,mark3))

def calculate_average(m1,m2,m3):
    return (m1+m2+m3)/3
print("The average of m1, m2 and m3 is:",calculate_average(mark1,mark2,mark3))

def check_result(average):
    if average >= 50:
        return "pass"
    else:
        return "fail"
average = calculate_average(mark1, mark2, mark3)
print("The result if average >= 50:", check_result(average))




