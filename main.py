# import library which will be used to clean the screen
from replit import clear
# import the logo from art package
from art import logo
print(logo)

# For auction's bidder comparison.
def auction():
    for the_bid in range(len(bidders)):
        highest_bidder = auction_winner["winners_bid"]
        bidder_now = bidders[the_bid]["bidders_bid"]
        if bidder_now > highest_bidder:
            auction_winner["winner"] = bidders[the_bid]["bidders_name"]
            auction_winner["winners_bid"] = bidders[the_bid]["bidders_bid"]

# Dictionary of the bidder.
bidders = []
# Dictionary of the winner of the auction.
auction_winner = {
    "winner" : "",
    "winners_bid": 0
}

# Looping for the program to keep running.
auction_continues = True
while auction_continues:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    # If the input is wrong, this code will keep looping until the input is right.
    while other_bidders != "yes" and other_bidders != "no":
        print("Type the right input!")
        other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.").lower()

    # Condition for ending the program.
    if other_bidders == "no":
        auction_continues = False
    
    # For adding the list of bidders.
    bidders.append({
            "bidders_name": name,
            "bidders_bid": bid
        })
    # Starting the auction function.
    auction()
    # Clear the screen.
    clear()

# Print the winner of the auction at the last screen.
print(f"The winner is {auction_winner['winner']} with a bid of ${auction_winner['winners_bid']}")