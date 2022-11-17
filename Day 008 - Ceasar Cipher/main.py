alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text,shift_amount,shift_direction):
  end_text=""
  for char in start_text:
    if char in alphabet:
      position=alphabet.index(char)
      if shift_direction=="encode":
          new_position=position+shift_amount
      elif shift_direction=="decode":
          new_position=position-shift_amount
      else:
        print ("Wrong option chosen.")
        return
      new_letter=alphabet[new_position]
      end_text+=new_letter
    else:
      end_text+=char
  print(f"Here's the {direction}d result: {end_text}")

from art import logo
print(logo)
should_end=False
while not should_end:
  direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text=input("Type your message:\n").lower()
  shift=int(input("Type the shift number:\n"))
  shift=shift%26
  caesar (text,shift,direction)
  restart=input("Do you wish to go again. Type 'yes'. Otherwise type 'no'.\n").lower()
  if restart=="no":
    should_end=False
    print("Goodbye")