width = int(input())
cheese = int(input())

if width == 3 and cheese >= 95:
    mood = "absolutely"
elif width == 1 and cheese <= 50:
    mood = 'fairly'
else:
    mood = "very"
print('C.C. is '+mood+' satisfied with her pizza.')
