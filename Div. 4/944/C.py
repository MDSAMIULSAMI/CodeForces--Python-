t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    if (a < c < b and (d < a or d > b)) or (c < a < d and (b < c or b > d)):
        print("YES")
    else:
        print("NO")