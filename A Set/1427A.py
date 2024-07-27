t = int(input())
for _ in range(t):
    w, h, n = map(int, input().split())
    pieces = 1
    while w % 2 == 0:
        w = w // 2
        pieces = pieces * 2
    while h % 2 == 0:
        h = h // 2
        pieces = pieces * 2
    if pieces >= n:
        print("YES")
    else:
        print("NO")