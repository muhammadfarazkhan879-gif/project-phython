# a=input("Enter the number:")
#
# print(f"Multiplication table of {a} is:")
#
# try:
#     for i in range (1,11):
#         print(f"{int(a)}*{i}={int(a)*i}")
#
# except:
#     print("invalid input!")
#
# print("some imp lines of code")
# print("End of program")


try:
    num = int(input("Enter an integer:"))
    a=[6,3]
    print(a[num])
except valueError:
    print("Number entered is not an integer.")
except valueError:
    print("index Error")
