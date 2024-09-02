
year = int(input())

def findYear(year):
    yearInt = year
    while True:
        yearInt+=1 
        yearStr = str(yearInt)
        a = list(yearStr)
        s = set(a)
        if len(s) == len(a):
            return yearInt

print(findYear(year))