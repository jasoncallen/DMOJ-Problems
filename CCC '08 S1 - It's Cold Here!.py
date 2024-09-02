city_temp_dict ={}
while True:
    city,tempstr = input().split(" ")
    
    temp = int(tempstr)
    city_temp_dict[city] = temp
    if city =="Waterloo":
        break
coldestcitytemp = 200
if len(city_temp_dict) != 1:
    for c,t in city_temp_dict.items():
        if t < coldestcitytemp:
            coldestcity = c
            coldestcitytemp = t
else:
    for c,t in city_temp_dict.items():
        coldestcity = c
print(coldestcity)