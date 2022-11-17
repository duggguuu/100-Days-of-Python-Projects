from replit import clear
from art import logo
print(logo)
bidding_finished=False
bids={}
    
def find_highest_bidder(bidding_record):
  highest_bid=0
  for bidder in bidding_record:
    bid_amount=bidding_record[bidder]
    if bid_amount>highest_bid:
      highest_bid=bid_amount
      winner=bidder
  print(f"The winner is: {bidder} with a bid of INR {highest_bid}")

while not bidding_finished:
  name=input("What is your name?: ").lower()
  price=int(input("What is your bid?: INR _"))
  bids[name]=price
  bidding_over=input("Are there any more bidders? Type 'yes' or 'no'")
  if bidding_over=="no":
    bidding_finished==True
    find_highest_bidder(bids)
  elif bidding_over=="yes":
    clear()