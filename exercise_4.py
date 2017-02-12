#Exercise 4

num = int (input("Enter a number: "))
b = []
for i in range(1, num+1):
    if num%i == 0:
        b.append(i)
print("The divisors of",num,"are:",b)
