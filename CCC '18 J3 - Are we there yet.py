distances = [int(i) for i in input().split()]

for i in range(len(distances)+1):
    distances2 = distances.copy()
    distances2.insert(i,0)

    travel = 0
    for k in range(i,len(distances2)):
        travel += distances2[k]
        distances2[k] = travel

    travel2 = 0
    for j in range(i,-1,-1):
        travel2 += distances2[j]
        distances2[j] = travel2

    for i in distances2:
        print(i, end=" ")
    print()