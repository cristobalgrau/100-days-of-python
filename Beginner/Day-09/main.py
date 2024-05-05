import art
from IPython.display import clear_output

def update_bids (bidder_name, bid_amount):
    temporary_dic = {}
    temporary_dic["name"] = bidder_name
    temporary_dic["bid"] = bid_amount
    master_bids.append(temporary_dic)

def find_winner ():
    highest_bid = 0
    winner = ""
    for key in master_bids:
        if  key["bid"] > highest_bid:
            highest_bid = key ["bid"]
            winner = key ["name"]
    
    print (f"The winner is {winner} with a bid of ${highest_bid}.")


master_bids = []

repeat = "yes"
while repeat == "yes":
    clear_output()
    print (art.logo)
    print ("Welcome to the secret auction program.")
    name = input ("What is your name?: ")
    bid = int(input ("What is your bid?: $"))
    update_bids (name, bid)
    repeat = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

if repeat == "no":
    find_winner()
