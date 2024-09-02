nOfCities = int(input())
listOfCities = []

for i in range(nOfCities):
    listOfCities.append(int(input()))

listOfCities.sort()
left = (listOfCities[1] - listOfCities[0]) /2
right = (listOfCities[2] - listOfCities[1]) /2
minSize = left + right
for i in range(2,nOfCities-1):
    left = (listOfCities[i] - listOfCities[i-1]) /2
    right = (listOfCities[i+1] - listOfCities[i]) /2
    size = left + right
    if size < minSize:
        minSize = size
print(minSize)