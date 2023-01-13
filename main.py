from replit import clear
from art import logo
print(logo)

roof = True
bids = {}
name = []
price = []
top_price = 0

def auction(user_name, user_price):
    bids["name"] = user_name
    bids["price"] = user_price
  
while roof:
  name.append(input("What is your name? "))
  price.append(input("What is your bid $"))
  auction(user_name = name, user_price = price)
  more_person = input("Is there more person? ")
  if more_person == "yes":
    clear()
    roof = True
  elif more_person == "no":
    roof = False
    for n in range(0, len(bids["price"])):
      if int(bids["price"][n]) > int(top_price):
        top_price = bids["price"][n]
        bought_person = bids["name"][n]
    print(f"The winnser is {bought_person} with a bid of {top_price}")
      
