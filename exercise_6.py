#Exercise 6
word = str(input("Enter a word: "))
test = list(word)
rev = []
index = len(test)-1
for i in range(0, len(test)):
    rev.append(test[index-i])
if rev == test:
    print(word,"is a palindrome!")
else:
    print(word,"is not a palindrome.")
