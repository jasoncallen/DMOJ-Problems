bowl1 = int(input())
bowl2 = int(input())
bowl3 = int(input())

if (bowl1 > bowl2 and bowl1 < bowl3) or (bowl1 < bowl2 and bowl1 > bowl3):
    print(bowl1)
if (bowl2 > bowl1 and bowl2 < bowl3) or (bowl2 < bowl1 and bowl2 > bowl3):
    print(bowl2)
if (bowl3 > bowl1 and bowl3 < bowl2) or (bowl3 < bowl1 and bowl3 > bowl2):
    print(bowl3)