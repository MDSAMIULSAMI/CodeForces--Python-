n, k = input().split()

k = int(k)
n = int(n)

point = []
point = [int(item) for item in input().split()]

counter = 0
for i in range(n):
    if point[i] >= point[k-1] :
        if point[i] != 0:
            counter = counter + 1
print(counter)