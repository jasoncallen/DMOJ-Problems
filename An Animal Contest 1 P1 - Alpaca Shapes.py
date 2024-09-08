user_in = input().split(" ")
s = int(user_in[0])
r = int(user_in[1])
s_a = s ** 2
r_a = 3.14 * (r ** 2)
if s_a > r_a:
    print("SQUARE")
else:
    print("CIRCLE")