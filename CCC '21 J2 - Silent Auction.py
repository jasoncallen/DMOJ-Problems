num_of_bids = int(input())
bidder = ""
max = 0
for _ in range(num_of_bids):
    bidder = input()
    bid = int(input())
    if bid > max:
        max = bid
        winner = bidder
print(winner)
