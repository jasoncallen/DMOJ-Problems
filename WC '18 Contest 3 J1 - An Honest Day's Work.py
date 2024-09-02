begin_litres = int(input())
req_litres = int(input())
dollars = int(input())

money = (begin_litres // req_litres * dollars) + begin_litres % req_litres
print(money)