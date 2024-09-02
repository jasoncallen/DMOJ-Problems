string = input()
output = ""

i = 0

while i < len(string):
    output = output + string[i]
    if string[i] in "aeiou":
        i +=3
    else:
        i +=1

print(output)