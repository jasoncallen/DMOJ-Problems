word = input()
word_count = 0
position = 0
for char in word:
    if position == 0:
        match = "H"
    elif position == 1:
        match = "O"
    elif position == 2:
        match = "N"
    else:
        match = "I"
    if char == match:
        position = position + 1
        if position == 4:
            position = 0
            word_count += 1
print(word_count)