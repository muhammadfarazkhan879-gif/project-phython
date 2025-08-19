            # example 1
# import time
# from time import strftime
# name=input('Enter the name:')
# time = int(time.strftime("%H"))
# if(time>0 and time<12):
#     print("Good morning: " , name)
# elif(time>12 and time<17):
#     print("Good Afternoon: ", name)
# elif(time>17 and time<20):
#     print("Good evening:" ,name)
# else:
#     print("Good night", name)
#               example 3
# time = int("Enter a temprature")
# if(time>0 and time<12):
#     print("Good morning")
# elif(time>12 and time<17):
#     print("Good Afternoon")
# else:
#     print("Good night")


# num = int(input("enter thr number:"))
# if num> 0:
#       print("postive number")
# elif num ==0:
#     print("zero number")
# else:
#     print("negative number")
#
#   2-greter no find

#

# a =int(input("Enter the first number:"))
# b =int(input("Enter the second number:"))
#
# if a>b:
#     print("first number is greater")
# elif a<b:
#     print("second number is greater ")
# else:
#     print("both are equal")
# 3- leap year

# year = int(input("enter the year"))
# if(year % 4 ==0 and year % 100!=0) or   (year % 400 ==0):
#     print("leap year ")
# else:
#      print("not a leap year")

# # 4-print grade
#
# marks = int(input("enter thr marks:"))
# if  marks>=90:
#     print("grade:A")
# elif marks>=80:
#     print("garde :b")
# elif marks>=70:
#     print("grade:c")
# elif marks>=60:
#     print("grade:d")
# else:
#     print("grade;f")
#
year = int(input("enter the year:"))
if (year % 4 ==0 and year % 100!=0) or(year % 400==0):
    print("leap year")
else:
    print("not leap year")














