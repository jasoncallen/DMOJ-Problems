lines = int(input())
english = 0
french = 0
count = 0
while count < lines:
    line = input()
    english = english + line.count("t") + line.count("T")
    french = french + line.count("s") + line.count("S")
    count = count + 1
if english == french:
    print("French")
elif english > french:
    print("English")
else:
    print("French")