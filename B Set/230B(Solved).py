import math

n = int(input())
t = list(map(int, input().split()))

limit = 10**6
primes = [True] * (limit + 1)
p = 2
while p * p <= limit:
    if primes[p]:
        for i in range(p * p, limit + 1, p):
            primes[i] = False
    p += 1

prime_set = {i for i in range(2, limit + 1) if primes[i]}

for i in range(n):
    sqrt_val = math.sqrt(t[i])
    if sqrt_val.is_integer():
        int_sqrt = int(sqrt_val)
        if int_sqrt in prime_set:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
