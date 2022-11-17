from random import randint
from art import logo
from replit import clear

def lets_guess(answer, turns):
  print (answer)
  for x in range(turns):
    if turns==0:
      print("You are out guesses. Zzzzzz.")
    else:
      print(f"You have {turns} attempts left to guess the number.")
      guess=int(input(print("Make a guess.")))
      if guess>answer:
        if guess>=2*answer:
          print ("Guess is too high.")
        elif guess>=1.5*answer and guess<=2*answer:
          print ("Guess is slightly high.")
        else:
          print("Guess is high but you're pretty close.")
      elif guess<answer:
        if guess<=2*answer:
          print ("Guess is too low.")
        elif guess<=1.5*answer and guess>=2*answer:
          print ("Guess is slightly low.")
        else:
          print("Guess is low but you're pretty close.")
      elif guess==answer:
        print("You got it. Your guess is right!!")
        return
      turns=turns-1

repeat="yes"
while repeat != "no":
  print (logo)
  print("Welcome to the Number Guessing Game!")
  print("I am thinking of a number between 1 and 100.")
  answer=randint(1,100)
  difficulty=input("Choose a difficulty. Type 'easy' or 'hard.'")
  if difficulty=="easy":
    turns=10
    lets_guess(answer,turns)
  elif difficulty=="hard":
    turns=5
    lets_guess(answer,turns)
  else:
    print ("Wrong choice.")
  repeat=input(print("Type 'yes' to play again. Type 'no' to stop playing."))
  if repeat=="yes":
    clear()
  elif repeat!="no" and repeat!="yes":
    print ("Wrogng choice. Zzzzzz.")