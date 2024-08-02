k, n, w = map(int, input().split())
total_k = 0
for i in range(1, w+1):
    total_k = total_k + (k*i)
if total_k < n:
    print(0)
else:
    print(total_k-n)