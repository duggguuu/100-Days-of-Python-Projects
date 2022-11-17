import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
n_letters= int(input("How many letters would you like in your password?\n")) 
n_symbols = int(input(f"How many symbols would you like?\n"))
n_numbers = int(input(f"How many numbers would you like?\n"))

n = n_letters + n_symbols + n_numbers
p=[]
for a in range(0, n_letters+1):
  char = random.choice(letters)
  p.append(char)
for b in range(0, n_symbols+1):
  sym = random.choice(symbols)
  p.append(sym)
for c in (0, n_numbers+1):
  num = random.choice(numbers)
  p.append(num)
random.shuffle(p)
password = ""
for x in p:
  password = password + x
print (f"you password is {password}")