#user inputs string
sentence = input("Type in a sentence").lower()
#user inputs shift
shift = int(input("What is your shift?"))
#initialise empty list
cipheredmessage=""
#loop for every character in string
for ch in sentence:
    #cipher
    cipheredmessage+= chr(ord(ch) + shift) 
#end for
#output ciphered message
print(cipheredmessage)
