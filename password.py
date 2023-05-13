import random
import argparse
import string

password_length = int(input("How long do you want you password to be? "))

password_style = int(input("Please type what you want your password to consist of?\n\n(1) Only numbers,\n(2) Only letters,\n(3) Letters and numbers,\n(4) Letters, numbers and special characters: "))

def numbers_password(password_length):
    select_numbers = [random.randint(0,9) for x in range(password_length)]
    if password_style == 1:
        return "".join(map(str, select_numbers))

def letters_password(password_length):
    letters = string.ascii_letters
    select_letters = [random.choice(letters) for x in range(password_length)]
    if password_style == 2:
        return "".join(map(str, select_letters))

def letters_and_numbers(password_length):
    letters_numbers = string.ascii_letters + string.digits
    if password_style == 3:
        return "".join(random.choice(letters_numbers) for x in range(password_length))

def letters_numbers_special(password_length):
    letters_numbers_special = string.ascii_letters + string.digits + string.punctuation
    if password_style == 4:
        return "".join(random.choice(letters_numbers_special) for x in range(password_length))

if password_style == 1:
    password = numbers_password(password_length)
elif password_style == 2:
    password = letters_password(password_length)
elif password_style == 3:
    password = letters_and_numbers(password_length)
elif password_style == 4:
    password = letters_numbers_special(password_length)
print()
print("**************************")
print("* Here is your password: *")
print("**************************")
print()
print(password)
print()