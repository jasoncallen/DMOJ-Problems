abc = "abcdefghijklmnopqrstuvwxyz"
count = 0
num_of_lines = int(input())
for _ in range(num_of_lines):
    for char in input():
        if char in abc:
            count += 1
        else:
            break

    if count == 26:
        print("OK.")
    else:
        print("Nope.")

    count = 0