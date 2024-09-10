num_of_num = int(input())
num_list = []
for _ in range(num_of_num):
    num_list.append(int(input()))
num_list.sort()
for n in num_list:
    print(n)