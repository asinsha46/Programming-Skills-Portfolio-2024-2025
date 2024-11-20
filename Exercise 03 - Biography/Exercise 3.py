# Collect user information
name = input("What is your full name? ")
hometown = input("Where are you from? ")
age_input = input("How old are you? ")

# Handle invalid age input
try:
    age = int(age_input)
except ValueError:
    print("Age must be a number.")
    age = None

# Store the user's details
user_info = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# Display the information
print("\nHere are your details:")
print(f"Name: {user_info['name']}")
print(f"Hometown: {user_info['hometown']}")
print(f"Age: {user_info['age'] if age is not None else 'Invalid input'}")
