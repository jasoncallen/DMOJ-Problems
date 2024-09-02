
b = int(input())
s = int(input())
d = int(input())
de = int(input())
calories = 0
if b == 1:
    calories = calories + 461
elif b == 2:
    calories = calories + 431
elif b == 3:
    calories = calories + 420

if s == 1:
    calories = calories + 100
elif s == 2:
    calories = calories + 57
elif s == 3:
    calories = calories + 70

if d == 1:
    calories = calories + 130
elif d == 2:
    calories = calories + 160
elif d == 3:
    calories = calories + 118

if de == 1:
    calories = calories + 167
elif de == 2:
    calories = calories + 266
elif de == 3:
    calories = calories + 75
    
print( "Your total Calorie count is "+str(calories)+".")