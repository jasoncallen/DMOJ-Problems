obeys = input()
n = int(input())

obeyed = obeys

for i in range(n):
    line = input()
    winner = line[0]
    loser = line[2]
    if obeys == loser:
        obeys = winner
        if not winner in obeyed:
            obeyed = obeyed + winner

print(obeys)
print(len(obeyed))