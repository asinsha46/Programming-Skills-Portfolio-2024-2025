# List of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Ask the user for a search term
search_term = input("Enter the name you want to search for: ").strip()

# Check if the search term is in the list
if search_term in names:
    print(f"'{search_term}' was found in the list!")
else:
    print(f"'{search_term}' was not found in the list.")
