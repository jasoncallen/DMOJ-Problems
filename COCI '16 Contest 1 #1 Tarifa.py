plan = int(input())
months = int(input())
next_month_plan = 0
for month in range (0,months):
    usage =int(input())
    next_month_plan = next_month_plan+ (plan - usage)
next_month_plan = next_month_plan + plan
print(next_month_plan)