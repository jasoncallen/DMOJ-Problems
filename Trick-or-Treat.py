num_houses, total_time = map(int, input().split())
barter_times = list(map(int, input().split()))

barter_times.sort()

journey = 0
visited = 0

for i, house in enumerate(barter_times):
        if i == 0:
            next_house = house 
        else:
            next_house = house + 1 
        if journey + next_house <= total_time:
            journey = journey + next_house
            visited += 1
        else:
            break
print(visited)