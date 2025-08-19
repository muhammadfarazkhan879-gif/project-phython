def func1():
    try:
        l=[1, 5, 6, 7]
        i=int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
       print("some error occurred")
       return 0


    finally:
        print("I am allways executed")
  # print("I am allways executed")

x=func1()
print(x)
