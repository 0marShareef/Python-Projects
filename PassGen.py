import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Creating a list of characters to be used in password - "pass_list":
pass_list = []
for i in range(nr_letters):
    letter_choice = random.choice(letters)
    pass_list.append(letter_choice)
for i in range(nr_symbols):
    symbol_choice = random.choice(symbols)
    pass_list.append(symbol_choice)
for i in range(nr_numbers):
    number_choice = random.choice(numbers)
    pass_list.append(number_choice)

# Randomising the list of characters and storing in new list - "password":
password = random.sample(pass_list, len(pass_list))

# Converting password list into string:
final_password = ""
for i in password:
    final_password = final_password + i

print(f"Here is your password: {final_password}")
