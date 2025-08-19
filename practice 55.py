import random

def check_win(user, computer):
    """Return result based on Snake-Water-Gun rules"""
    if user == computer:
        return "It's a Tie!"


    if (user == "gun" and computer == "snake") \
       or (user == "water" and computer == "gun") \
       or (user == "snake" and computer == "water"):
        return "You Win!"
    else:
        return "Computer Wins!"


print("Welcome to Snake-Water-Gun Game!")
choices = ["snake", "water", "gun"]

user_choice = input("Enter your choice (snake/water/gun): ").lower()

if user_choice not in choices:
    print("Invalid choice! Please choose snake, water, or gun.")
else:
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    result = check_win(user_choice, computer_choice)
    print(result)
