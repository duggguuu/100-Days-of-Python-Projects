import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user = int( input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
pc = random.randint(0, 2)

if (pc == 0) and (user == 0):
  print ("You chose rock. Computer also chose rock. It's draw.")
elif (pc == 0) and (user == 1):
  print ("You chose paper. Computer chose rock. You win!!")
elif (pc == 0) and (user == 2):
  print ("You chose scissors. Computer chose rock. Computer wins :(")
elif (pc == 1) and (user == 0):
  print ("You chose rock. Computer chose paper. Computer wins :(")
elif (pc == 1) and (user == 1):
  print ("You chose paper. Computer also chose paper. It's a draw.")
elif (pc == 1) and (user == 2):
  print ("You chose scissors. Computer chose paper. You win!!")
elif (pc == 2) and (user == 0):
  print ("You chose rock. Computer chose scissors. You win!!")
elif (pc == 2) and (user == 1):
  print ("You chose paper. Computer chose scissors. Computer wins :(.")
elif (pc == 2) and (user == 2):
  print ("You chose scissors. Computer also scissors. It's a draw.")
else:
  print ("invalid")