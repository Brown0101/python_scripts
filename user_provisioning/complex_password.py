import random

complex = "1234567890!@#$%^&*()zxcvbnmlkjhgfdsaqwertyuiopQWERTYUIOPASDFGHJKLZXCVBNM"
new_pass = ""
length = input("Enter a number for the password length: ")

try:
    count = 0
    while count < int(length):
        num = random.randint(0, len(complex))
        new_pass += complex[num]
        count += 1
except ValueError as ve:
    print("{} is not a valid number!".format(length))

print(new_pass)
    
