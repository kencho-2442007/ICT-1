#countdown
i=10
while i>=1:
    print(i)
    i-=1
print("Times up!")

#sum until zero
i = 0
while True:
    number = int(input("Enter an integer (0 to stop): "))
    if number == 0:
        break
    i+= number

print("The total sum:", i)

# Program to check username and password
correct_username = "admin"
correct_password = "1234"
attempts = 3

for i in range(attempts):
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    
    if username == correct_username and password == correct_password:
        print("Login Successful")
        break
    else:
        print(f"Wrong credentials! Attempts left: {attempts - i - 1}")
    
    # If the last attempt was reached
    if i == attempts - 1:
        print("Account Locked")



