n = int(input())
solve = 0
for i in range(n):
    p, v, t = input().split()
    pack = p, v, t
    counter = pack.count("1")
    if counter >= 2:
        solve = solve + 1
print(solve)