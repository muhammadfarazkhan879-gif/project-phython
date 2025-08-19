#                  Example 1
# num=int(input("Enter the number: "))
# if num  >= 90:
#        print("grade A")
# elif num >= 80:
#      print("grade B")
# elif num >= 70:
#      print("grade c")
# elif num >= 60:
#      print("grade d")
# elif num <= 50:
#      print("grade f")
#              Example 2




year=int(input("Enter the Year: "))
if (year % 4 ==0 and year % 100!= 0 ) or (year %400==0):
     print("Leap year")
else:
          print("not a leap year")