month = int(input())
day = int(input())
if month < 3:
    if month <2:
        print("Before")
    if month == 2:
        if day <18:
            print("Before")
        elif day > 19:
            print("After")
        else:
            print("Special")
else:
    print("After")