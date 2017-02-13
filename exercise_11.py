#Exercise 11

def is_prime(x):
    for i in range (1, x+1):
        if i != 1 and i != x:
            if x%i == 0:
                return "The number is NOT prime"
            else:
                return "The number is prime"  

num = int (input("Enter a number: "))
print(is_prime(num))
