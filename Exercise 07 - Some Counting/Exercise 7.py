# Loop 1: Count up from 0 to 50 in increments of 1
print("Counting up from 0 to 50 in increments of 1:")
for i in range(0, 51):  # range(start, stop) - stop is exclusive, so use 51
    print(i)

print("\n")  # Separate outputs for readability

# Loop 2: Count down from 50 to 0 in decrements of 1
print("Counting down from 50 to 0 in decrements of 1:")
for i in range(50, -1, -1):  # range(start, stop, step)
    print(i)

print("\n")

# Loop 3: Count up from 30 to 50 in increments of 1
print("Counting up from 30 to 50 in increments of 1:")
for i in range(30, 51):  # range(start, stop)
    print(i)

print("\n")

# Loop 4: Count down from 50 to 10 in decrements of 2
print("Counting down from 50 to 10 in decrements of 2:")
for i in range(50, 9, -2):  # range(start, stop, step)
    print(i)

print("\n")

# Loop 5: Count up from 100 to 200 in increments of 5
print("Counting up from 100 to 200 in increments of 5:")
for i in range(100, 201, 5):  # range(start, stop, step)
    print(i)
