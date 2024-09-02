cards = [2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11]

numOfCards = int(input())
blackjack = 21
for i in range(numOfCards):
    drawnCard = int(input())
    cards.remove(drawnCard)
    blackjack = blackjack - drawnCard


lowerCards = 0
higherCards = 0
cards.sort()
print(cards)
if blackjack == 0:
    print('DOSTA')
else:
    for c in cards:
        if c > blackjack:
            higherCards = higherCards + 1
        if c <= blackjack:
            lowerCards = lowerCards + 1
    if higherCards >= lowerCards:
        print("DOSTA")
    else:
        print('VUCI')