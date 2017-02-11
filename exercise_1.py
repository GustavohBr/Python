#Exercise 1

name = input("Enter your name: ")
age = int(input("Enter your age: "))
year = (100-age) + 2017

print (name, "you'll be 100  years old in",year)

#Extra 1 and 2

name = input("Enter your name: ")
age = int(input("Enter your age: "))
num = int(input("How many times do you want to see the message: "))
year = (100-age) + 2017

for i in range(0, num):
    print (name, "you'll be 100  years old in",year)
