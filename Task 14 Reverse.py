#get user to input string
word = input("Input any word")
#calculate the length of the string
stringlength = len(word)
#slice
reverseofword = word[stringlength::-1]
#output reverse of string
print(reverseofword)

