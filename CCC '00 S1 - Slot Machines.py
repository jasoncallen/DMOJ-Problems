button =0
song = "ABCDE"
while button != 4:
    button = int(input())
    presses = int(input())
    for i in range(presses):
        if button == 1:
            song = song[1:] + song[0]
        if button == 2:
            song = song[-1] + song[:-1]
        if button == 3:
            song = song[1] + song[0] + song[2:]

output = ""
for char in song:
    output = output + char + " "

print(output[:-1])
