password = input()

upper = 0
lower = 0
digit = 0
if len(password) < 8 or len(password) > 12:
    print("Invalid")
else:
    for char in password:
        if char.isnumeric():
            digit+=1
        elif char.isupper():
            upper += 1
        elif char.islower():
            lower += 1


    if lower >= 3 and upper >= 2 and digit >= 1:
        print("Valid")
    else:
        print("Invalid")