num_of_bids = int(input())
bidders = {}
for _ in range(num_of_bids):
    bidder = input()
    bid = int(input())
    bidders[bidder] = bid
bid = -1
winner = ""
for k,v in bidders.items():
    if v > bid:
        bid = v
        winner = k
print(winner)