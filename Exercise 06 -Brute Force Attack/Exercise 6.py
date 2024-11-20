# Define the correct password and maximum attempts
correct_password = "12345"
max_attempts = 5

# Initialize the number of attempts
attempts = 0

# Password entry system with a maximum of 5 attempts
while attempts < max_attempts:
    password = input("Enter the password: ")
    attempts += 1  # Increment attempts
    
    if password == correct_password:
        print("Access granted!")
        break  # Exit the loop if the correct password is entered
    else:
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempt(s) remaining.")
        else:
            print("Incorrect password. Maximum attempts reached. Authorities have been alerted.")
