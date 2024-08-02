n = int(input())
a = list(map(int, input().strip().split()))[:n]
# print(a)
flag = 0
for i in a:
    if i == 1:
        flag = 1
if flag == 1:
    print("HARD")
else:
    print("EASY")

