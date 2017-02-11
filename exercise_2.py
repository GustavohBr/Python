#Exercise 2

num = int (input("Enter a number: "))

if num%2 == 0:
    print ("The number is even")
else:
    print("The number is odd")

#Extra 1

num = int (input("Enter a number: "))
if num%4 == 0:
    print("This number is a multiple of 4")
elif num%2 == 0:
    print ("The number is even")
else:
    print("The number is odd")

#Extra 2

num, check = int (input("Enter a number: ")), int (input("Enter another number: "))
if num%check == 0:
    print(num, "divides evenly into",check)
else:
    print (num,"doesn't divide evenly into",check)
