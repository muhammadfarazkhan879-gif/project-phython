questions = [
    {
        "question": "1. How many players are there in a standard cricket team??",
        "options": ["A. 9", "B. 10", "C. 11", "D. 12"],
        "answer": "C",
        "amount": 10000
    },
    {
        "question": "2. Which country won the ICC Cricket World Cup 2019?",
        "options": ["A. india", "B. Australia", "C. England", "D. New Zealand"],
        "answer": "C",
        "amount": 20000
    },
    {
        "question": "3. Who was the captain of Pakistan cricket team during the 1992 World Cup?",
        "options": ["A. Wasim Akram", "B. Javed Miandad", "C. Imran Khan", "D. Inazamam-ul-Haq"],
        "answer": "C",
        "amount": 30000
    }
]

total_amount = 0
print(" Welcome to KBC  ")
for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)

    user_answer = (input("Enter your answer (A/B/C/D): ")).upper()

    if user_answer == q["answer"]:
        print(" Correct Answer!")
        total_amount += q["amount"]
    else:
        print(" Wrong Answer! Game Over.")
        break

print(f"You have won Rs. {total_amount}. Thanks for playing!")
