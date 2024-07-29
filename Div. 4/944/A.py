t = int(input())
for i in range(t):
    a, b = input().split()
    x = [a,b]
    x.sort()
    print(" ".join(x))