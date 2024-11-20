# Function to determine if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."

# Main function
def main():
    # Ask the user for a number
    try:
        user_input = int(input("Enter a number: "))  # Convert input to an integer
        # Pass the number to the function and get the result
        result = check_even_odd(user_input)
        # Print the result
        print(result)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
