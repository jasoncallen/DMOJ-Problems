spaces = int(input())
prev_day = input()
today = input()
occup = 0
for space in range (0,spaces):
    if prev_day[space] == today[space] and prev_day[space] == "C":
        occup += 1
print(occup)