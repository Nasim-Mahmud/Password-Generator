#Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the Password Generator.")

user_letters= int(input("How many letters would you like in your password?\n")) 
user_symbols = int(input(f"How many symbols would you like?\n"))
user_numbers = int(input(f"How many numbers would you like?\n"))


password = ""
for letter in range(0, user_letters):
  letter = random.choice(letters)
  password += str(letter)
# print(password1)
for sym in range(0, user_symbols):
  sym = random.choice(symbols)
  password += str(sym)
# print(password2)
for num in range(0, user_numbers):
  num = random.choice(numbers)
  password += str(num)
# print(password3)

a =  ''.join(random.sample(password,len(password)))
print(a)