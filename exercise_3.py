#Exercise 3

a = [1,1,2,3,5,8,13,21,34,55,89]
for num in a:
    if num < 5:
        print (num)

#Extra 1

a = [1,1,2,3,5,8,13,21,34,55,89]
b = []
for num in a:
    if num < 5:
        b.append(num)
print(b)

#Extra 2

print([x for x in [1,1,2,3,5,8,13,21,34,55,89] if x < 5])

#Extra 3

a = [1,1,2,3,5,8,13,21,34,55,89]
b = []
i = int(input("Enter a number: "))
for num in a:
    if num < i:
        b.append(num)
print("Numbers smaller than",i,":",b)
