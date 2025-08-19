menu = {
    "burger": 100,
    "tea": 150,
    "coffee": 200,
    "cake": 250
}
print("\t*** Welcome To The Khan Restaurants ***\n")
print( " burger: Rs 100", "\n tea: RS 150","\n coffee: RS 200","\n cake: RS 250", )
total_price = 0

user_order1 = input("\nEnter your first order: ").lower()
if user_order1 in menu:
    print(f"\nYour ordered item *{user_order1}* has been added to your list.")
    total_price += menu[user_order1]
else:
    print(f"\nSorry, your ordered item *{user_order1}* is not available.")


user_decision = input("Would you like to order anything else? (yes/no): ").lower()
if user_decision == "yes":
    user_order2 = input("Enter your second order: ").lower()
    if user_order2 in menu:
        print(f"\nYour ordered item *{user_order2}* has been added to your list.")
        total_price += menu[user_order2]
    else:
        print(f"\nSorry, your ordered item *{user_order2}* is not available.")


    user_decision = input("Would you like to order anything else? (yes/no): ").lower()
    if user_decision == "yes":
        user_order3 = input("Enter your third order: ").lower()
        if user_order3 in menu:
            print(f"\nYour ordered item *{user_order3}* has been added to your list.")
            total_price += menu[user_order3]
        else:
            print(f"\nSorry, your ordered item *{user_order3}* is not available.")


print("\n*")
print("Your bill is ready...")
print(f"Your total amount is Rs {total_price} to pay.")
user_pay = int(input("Enter your payment amount: "))


if user_pay < total_price:
    print("\nSorry sir, the entered amount is less than the total amount.")
elif user_pay > total_price:
    balance = user_pay - total_price
    print(f"\nThank you! Your balance Rs {balance} will be returned.")
else:
    print("\n==>> Okay sir, have a good day!")