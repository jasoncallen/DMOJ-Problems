full_bar = int(input())
apples = int(input())
seconds = int(input())
current_bar = 0
if full_bar <= current_bar + apples:
    current_bar = full_bar
else:
    current_bar = apples
hunger = current_bar - seconds
if hunger <0:
    hunger = 0
print(hunger)