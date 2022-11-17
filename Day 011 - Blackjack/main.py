import random
from replit import clear
from art import logo

def deal_cards():
  """Choose a random card from the deck."""
  cards=[11,1,2,3,4,5,6,7,8,9,10,10,10]
  new_card=random.choice(cards)
  return new_card

def check_card(x):
  """Check which card is drawn."""
  if x==11:
    print("Ace was drawn")
  elif x==10:
    jqk(x)
  else:
    print(f"{x} was drawn.")

def check_initial_card(z):
  """Check which card is drawn(for initial cards)."""
  if z==10:
    return jqk_i(z)
  elif z==11:
    return "Ace"
  else:
    return z

def jqk(y):
  """Deciding Jack/Queen/King if the card chosen is a 10."""
  tens_cards=["Jack","Queen","King"]
  new_tens_card=random.choice(tens_cards)
  print (f"{new_tens_card} was drawn")

def jqk_i(a):
  """Deciding Jack/Queen/King if the card chosen is a 10 (for initial cards)."""
  tens_cards=["Jack","Queen","King"]
  new_tens_card=random.choice(tens_cards)
  return new_tens_card

def start_cards():
  """Distributing starting cards."""
  u_first_card=deal_cards()
  u_checked_first_card=check_initial_card(u_first_card)
  u_second_card=deal_cards()
  u_checked_second_card=check_initial_card(u_second_card)
  u_initial_total=u_first_card+u_second_card
  print(f"Your starting cards are: {u_checked_first_card} and {u_checked_second_card}. Your total is {u_initial_total}")
  if u_initial_total==21:
    print("It's a Blackjack")
  d_first_card=deal_cards()
  d_second_card=deal_cards()
  d_initial_total=d_first_card+d_second_card
  print(f"Dealer's starting cards are: {d_first_card} and the second card is hidden. Dealer's visible total is {d_first_card}")
  return u_initial_total, d_second_card, d_initial_total

def hit():
  """When user wants to Hit."""
  u_new_card=deal_cards()
  u_new_total=u_initial_total+u_new_card
  check_card(u_new_card)
  if u_new_total>21:
    print("Busted! Your total crossed 21. Better luck next time.")
    return
  elif u_new_total<16:
    print(f"Your new total is {u_new_total}. This is less than 16, hence you have to Hit again.")
    next_move()
  else:
    print (f"Your new total is {u_new_total}.")
    next_move()

def stand():
  """When user wants to Stand. Over to the dealer now."""
  print(f"Dealer's second card is: {d_second_card} and the total is {d_initial_total}")
  u_new_total=u_initial_total
  d_new_total=d_initial_total
  if d_new_total>u_new_total and d_new_total<21:
    print(f"The Dealer won! Better luck next time.")
    return
  elif d_new_total==u_new_total and d_new_total>21:
    print(f"Dealer also got busted. That was a tie.")
    return
  elif d_new_total<u_new_total and d_new_total<21:
    stand_next_move(d_new_total,u_new_total)
    
def stand_next_move(d_new_total,u_new_total):
  """When dealer has to Hit."""
  print ("Dealer is Hitting.")
  d_new_card=deal_cards()
  d_new_total=d_new_total+d_new_card
  check_card(d_new_card)
  print(f"Dealer's new total is: {d_new_total}")
  if d_new_total>21:
    print("Since the total crossed 21, the delaer lost!! You got crazy luck.")
    return
  elif d_new_total>u_new_total and d_new_total<21:
    print(f"The Dealer won! Better luck next time.")
    return
  else:
    stand_next_move(d_new_total,u_new_total)

def next_move():
  """Checking what user wants to do."""
  u_choice=input(print("Enter 'h' to gor for another Hit. Enter 's' to for a stand. Enter 'd' to double the bet.")).lower()
  if u_choice=="h":
    hit()
  elif u_choice=="s":
    stand()
  else:
    print("Wrong choice. The dealer got pissed. Game over.")


def play_game():
  """The game sequence."""
  print("Let's play Balckjack!!")
  print(logo)
  u_initial_total, d_second_card, d_initial_total=start_cards()
  next_move()

play=input(print("Enter 'y' to play. Enter 'n' to stop.")).lower()
"""Checking if user wants to play?"""
if play=="y":
  clear()
  play_game()
elif play=="n":
  clear()
  print ("Thank you for playing")