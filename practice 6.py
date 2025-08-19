# Write a program that uses single-line and multi-line comments
# to describe what the code is doing. The code should take a user’s name and
# age and print a greeting message.



name = input("Enter your name: ")
age = input("Enter your age: ")

age = int(age)

print("\nWelcome,", name)
print("Your age is:", age)
print("Your age next year will be:", age + 1)
