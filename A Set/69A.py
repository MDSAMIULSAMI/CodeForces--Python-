n = int(input())

memo_x = []
memo_y = []
memo_z = []

sum_x = 0
sum_y = 0
sum_z = 0
for i in range(n):
    x, y, z = input().split()

    memo_x.append(x)
    memo_y.append(y)
    memo_z.append(z)

    sum_x = int(sum_x)+ int(memo_x[int(i)])
    sum_y = int(sum_y)+ int(memo_y[int(i)])
    sum_z = int(sum_z)+ int(memo_z[int(i)])

if sum_x == 0 and sum_y == 0 and sum_z == 0:
    print("YES")
else:
    print("NO")