# List of questions and answers (country: capital)
quiz_data = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Austria": "Vienna",
    "Sweden": "Stockholm",
    "Norway": "Oslo"
}

# Initialize the score
score = 0

# Loop through each question in the quiz
for country, capital in quiz_data.items():
    # Ask the user the question
    answer = input(f"What is the capital of {country}? ")
    
    # Check the answer (case-insensitive)
    if answer.strip().lower() == capital.lower():
        print("Correct!")
        score += 1  # Increment score for correct answer
    else:
        print(f"Wrong! The correct answer is {capital}.")

# Final score
print(f"\nQuiz complete! You scored {score} out of {len(quiz_data)}.")
