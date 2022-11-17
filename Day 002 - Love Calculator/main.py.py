print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = name1 + name2
print (combined_name)

combined_name_lower = combined_name.lower()
print (combined_name_lower)

t = combined_name_lower.count('t')
r = combined_name_lower.count('r')
u = combined_name_lower.count('u')
e = combined_name_lower.count('e')
true = t + r + u + e
l = combined_name_lower.count('l')
o = combined_name_lower.count('o')
v = combined_name_lower.count('v')
e = combined_name_lower.count('e')
love = l + o + v + e
true_love = str(true) + str(love)
true_love = int (true_love)

print (true_love)

if (true_love < 10) or (true_love >90):
  print (f"your score is {true_love}, you go together like coke and mentos.")
elif (true_love > 40) and (true_love < 50):
  print (f"your score is {true_love}, you are alright together")
else:
  print (f"your score is {true_love}")