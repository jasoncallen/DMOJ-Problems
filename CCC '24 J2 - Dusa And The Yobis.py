dusaSize = int(input())

while True:
    yobis = int(input())
    if dusaSize <= yobis:
        break
    dusaSize = dusaSize + yobis

print(dusaSize)