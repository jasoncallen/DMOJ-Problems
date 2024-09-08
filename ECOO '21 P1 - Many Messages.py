start_min= int(input())
interval = int(input())
message_time = int(input())
check_time= start_min + interval
checked = 0
while True:
    if checked > 2:
        print("Who knows...")
        break
    elif check_time >= message_time:
        print(check_time)
        break
    check_time = check_time + interval
    checked += 1