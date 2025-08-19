# Ek program likho jo 1 se 10 tak ke numbers print kare using for loop.
for i in range(1, 11):
    print(i)

# Ek program likho jo 2 ke table ko for loop se print kare.
for i in range(1, 11):
    print(f"2 x {i} = {2 * i}")


# Ek program likho jo ek list ke tamam elements ko for loop se print kare.
fruits = ["apple", "banana", "mango", "orange", "grape"]
for fruit in fruits:
    print(fruit)

# Ek program likho jo 1 se 50 tak ke even numbers ko print kare using for loop.

for i in range(2, 51, 2):
    print(i)

# Ek program likho jo 1 se 50 tak ke even numbers ko print kare using for loop.

total = 0
for i in range(5):
    num = int(input("Enter number (i+1): "))
    total += num

print("Total sum is:", total)
