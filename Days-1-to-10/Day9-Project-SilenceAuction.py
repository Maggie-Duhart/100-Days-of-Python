import clear

#Find the highest bidder
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_value = bidding_record[bidder]
        if bid_value > highest_bid:
            highest_bid = bid_value
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    bidder_name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $"))
    bids[bidder_name] = bid_amount

    another_bidder = input(
        "Are there any other bidders? Type 'yes' or 'no'.").lower()
    if another_bidder == "yes":
        clear()
    else:
        bidding_finished = True
        find_highest_bidder(bids)
